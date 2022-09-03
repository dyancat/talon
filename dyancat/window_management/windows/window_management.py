from ....code.screen import get_sorted_screens
from talon import Context, actions, ui, Module, app, clip, ctrl, cron
from talon.canvas import Canvas

mod = Module()
ctx = Context()
ctx.matches = r"""
os:windows
"""

import sys
if sys.platform == 'win32':
    import win32gui, win32con, win32api, win32process

    from ctypes import *
    import ctypes
    import ctypes.wintypes
    from ctypes import (
        Structure
    )
    from ctypes.wintypes import (
        HWND,
        DWORD,
        WORD,
        RECT,
        UINT,
        ATOM
    )

dwmapi = ctypes.WinDLL("dwmapi")

class tagTITLEBARINFO(Structure):
    pass
tagTITLEBARINFO._fields_ = [
    ('cbSize', DWORD),
    ('rcTitleBar', RECT),
    ('rgstate', DWORD * 6),
]
TITLEBARINFO = tagTITLEBARINFO

def activate_window(hwnd):
    if not win32gui.IsWindow(hwnd):
        return

    fgwin = win32gui.GetForegroundWindow()
    fg = win32process.GetWindowThreadProcessId(fgwin)
    current = win32api.GetCurrentThreadId()

    try:
        attached = False
        if current != fg and fg:
            try:
                attached = win32process.AttachThreadInput(fg, current, True)
            except:
                pass

        for fn in [
            win32gui.BringWindowToTop,
            win32gui.SetForegroundWindow,
            win32gui.SetActiveWindow,
            # win32gui.SetFocus
        ]:
            try:
                fn(hwnd)
            except Exception as e:
                print(str(e))
    except Exception as e:
        print(str(e))
    finally:
        if attached:
            win32process.AttachThreadInput(fg, win32api.GetCurrentThreadId(), False)
        #else:
            #win32gui.SetForegroundWindow(hwnd)


def is_alt_tab_window(hwnd, debug = False):
    """Check whether a window is shown in alt-tab.
    See http://stackoverflow.com/a/7292674/238472 for details.
    """

    def print_debug(message):
        if debug == True: print(message)

    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)

    if not win32gui.IsWindowVisible(hwnd) or not win32gui.IsWindow(hwnd) or not window_title(hwnd):
        return False

    print_debug(f'Window text: {window_text}')
    print_debug(f'    Class name: {class_name}')

    hwnd_walk = win32con.NULL
    hwnd_try = ctypes.windll.user32.GetAncestor(hwnd, win32con.GA_ROOTOWNER)
    while hwnd_try != hwnd_walk:
        hwnd_walk = hwnd_try
        hwnd_try = ctypes.windll.user32.GetLastActivePopup(hwnd_walk)
        if win32gui.IsWindowVisible(hwnd_try):
            break

    if hwnd_walk != hwnd:
        print_debug(f'    Returns False due to hwnd_walk != hwnd')
        return False

    if class_name == 'Windows.UI.Core.CoreWindow':
        print_debug(f'    Returns False due to class_name == Windows.UI.Core.CoreWindow')
        return False

    # the following removes some task tray programs and "Program Manager"
    # ti = TITLEBARINFO()
    # ti.cbSize = ctypes.sizeof(ti)
    # ctypes.windll.user32.GetTitleBarInfo(hwnd, ctypes.byref(ti))
    # if ti.rgstate[0] & win32con.STATE_SYSTEM_INVISIBLE:
    #     print_debug(f'    Returns False due to win32con.STATE_SYSTEM_INVISIBLE')
    #     return False

    # Tool windows should not be displayed either, these do not appear in the
    # task bar.
    if win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) & win32con.WS_EX_TOOLWINDOW:
        print_debug(f'    Returns False due to win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) & win32con.WS_EX_TOOLWINDOW')
        return False

    pwi = WINDOWINFO()
    windll.user32.GetWindowInfo(hwnd, byref(pwi))
    # A top-level window created with this style does not become the foreground
    # window when the user clicks it. The system does not bring this window to
    # the foreground when the user minimizes or closes the foreground window.
    # The window does not appear on the taskbar by default.
    if pwi.dwExStyle & win32con.WS_EX_NOACTIVATE:
        print_debug(f'    Returns False due to win32con.WS_EX_NOACTIVATE')
        return False

    print_debug(f'    Returns True')
    return True

class tagWINDOWINFO(Structure):

    def __str__(self):
        return '\n'.join([key + ':' + str(getattr(self, key)) for key, value in self._fields_])

tagWINDOWINFO._fields_ = [
    ('cbSize', DWORD),
    ('rcWindow', RECT),
    ('rcClient', RECT),
    ('dwStyle', DWORD),
    ('dwExStyle', DWORD),
    ('dwWindowStatus', DWORD),
    ('cxWindowBorders', UINT),
    ('cyWindowBorders', UINT),
    ('atomWindowType', ATOM),
    ('wCreatorVersion', WORD),
]
WINDOWINFO = tagWINDOWINFO

def window_title(hwnd):
    return win32gui.GetWindowText(hwnd)

def top_level_windows():
    """ Returns the top level windows in a list of hwnds."""
    windows = []
    win32gui.EnumWindows(_window_enum_top_level, windows)
    return windows

def _window_enum_top_level(hwnd, windows):
    """ Window Enum function for getTopLevelWindows """
    if is_alt_tab_window(hwnd):
        windows.append(hwnd)

def highlight_window(hwnd):
    def on_draw(c):
        paint = c.paint
        paint.style = paint.Style.FILL
        paint.color = (0, 125, 0, 86)
        c.draw_rect(c.rect)

        cron.after("300ms", canvas.close)


    windowRect = RECT()
    DMWA_EXTENDED_FRAME_BOUNDS = 9
    dwmapi.DwmGetWindowAttribute(HWND(hwnd), DWORD(DMWA_EXTENDED_FRAME_BOUNDS), ctypes.byref(windowRect), ctypes.sizeof(windowRect))
    rect = ui.Rect(windowRect.left, windowRect.top, windowRect.right - windowRect.left, windowRect.bottom - windowRect.top)
    canvas = Canvas.from_rect(rect)
    canvas.register("draw", on_draw)
    canvas.freeze()

def get_screen_for_window(hwnd, screens) -> int:
    windowRect = win32gui.GetWindowRect(hwnd)
    [windowX1, windowY1, windowX2, windowY2] = windowRect
    windowArea = (windowX2 - windowX1) * (windowY2 - windowY1)

    if(windowArea == 0):
        return 0

    maxCoverage = 0
    screenNumberWithMaxCoverage = 0

    for screen in screens:
        [screenX1, screenY1, screenW, screenH] = screen.rect
        screenX2 = screenX1 + screenW
        screenY2 = screenY1 + screenH

        overlapX = min(screenX2, windowX2) - max(screenX1, windowX1)
        overlapY = min(screenY2, windowY2) - max(screenY1, windowY1)
        overlapArea = overlapX * overlapY if overlapX > 0 and overlapY > 0 else 0
        coverage = overlapArea / windowArea

        if coverage > maxCoverage:
            maxCoverage = coverage
            screenNumberWithMaxCoverage = screens.index(screen) + 1

    return screenNumberWithMaxCoverage

@mod.action_class
class Actions:
    def window_max():
        """Maximize active window"""
        hWnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hWnd, win32con.SW_MAXIMIZE)

    def window_min():
        """Minimize active window"""
        hWnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hWnd, win32con.SW_MINIMIZE)

    def window_restore():
        """Restore active window"""
        hWnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hWnd, win32con.SW_RESTORE)

    def window_highlight():
        """Highlight active window"""
        hWnd = win32gui.GetForegroundWindow()
        highlight_window(hWnd)

    def focus_screen(screen_num: int):
        """Focuses the top level window on a specific screen"""
        windows = top_level_windows()
        screens = get_sorted_screens()

        for window in windows:
            screenNumber = get_screen_for_window(window, screens)
            if(screen_num is screenNumber):
                print(f'Activating {window_title(window)} on screen {screenNumber}')
                activate_window(window)
                highlight_window(window)
                actions.sleep("100ms")
                break

    def debug_screen():
        """Debug screens"""
        windows = top_level_windows()
        screens = get_sorted_screens()

        for window in windows:
            screenNumber = get_screen_for_window(window, screens)
            print(f'Screen {screenNumber}: {window_title(window)}')


