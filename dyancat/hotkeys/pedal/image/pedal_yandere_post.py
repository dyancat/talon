from talon import Context, actions, ctrl, ui
import time

ctx = Context()
ctx.matches = r"""
tag: browser
browser.url: /yande\.re\/post\/show\/\d+/
browser.url: /files\.yande\.re/
"""

@ctx.action_class("user")
class Actions:
    def pedal_left():
        """Executes when pedal left is pressed"""
        actions.user.tab_close_wrapper()

    def pedal_left_up():
        """Executes when pedal left is released"""

    def pedal_middle():
        """Executes when pedal middle is pressed"""
        actions.key("3")
        rect = ui.active_window().rect
        ctrl.mouse_move(rect.left + rect.width / 2, rect.top + 650)

    def pedal_middle_up():
        """Executes when pedal middle is released"""

    def pedal_right():
        """Executes when pedal right is pressed"""
        ctrl.mouse_click(button=1)
        time.sleep(0.2)
        actions.key("down")
        time.sleep(0.1)
        actions.key("down")
        time.sleep(0.1)
        actions.key("enter")
        time.sleep(1)
        actions.key("enter")

    def pedal_right_up():
        """Executes when pedal right is released"""