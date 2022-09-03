from talon import Context, actions, ui, Module, app, clip, ctrl, canvas
import threading

from dataclasses import dataclass
import threading
import time

class Config:
    radius_px = 100
    # show_ms = 400
    # hide_ms = 250
    show_ms = 0
    hide_ms = 0
    bg_alpha = 0x77

@dataclass
class Animation:
    start_ts:  float
    target_ts: float
    start_value:  float
    target_value: float

    def __init__(self, duration: float, start: float, target: float):
        now = time.perf_counter()
        self.start_ts = now
        self.target_ts = now + duration
        self.start_value = start
        self.target_value = target

    @property
    def progress(self) -> float:
        now = time.perf_counter()
        return max(0.0, min(1.0, ((now - self.start_ts) / (self.target_ts - self.start_ts + 1e-9))))

    @property
    def value(self) -> float:
        return self.start_value + (self.target_value - self.start_value) * self.progress


class MouseHalo:
    def __init__(self):
        self.lock = threading.RLock()
        self.showing = False
        self.hiding = False
        # self.radius_anim = Animation(0, 0, 1000)
        # self.bg_anim = Animation(0, 0, 0)

    def show(self):
        if self.showing:
            return

        canvas.register('overlay', self.draw)
        self.showing = True
        # with self.lock:
        #     now = time.perf_counter()
        #     show_s = Config.show_ms / 1000
        #     if self.hiding:
        #         self.hiding = False
        #     elif self.showing:
        #         return
        #     else:
        #         canvas.register('overlay', self.draw)
        #     self.showing = True
        #     self.radius_anim = Animation(
        #         show_s, self.radius_anim.value, Config.radius_px)
        #     self.bg_anim = Animation(
        #         show_s, self.bg_anim.value,    Config.bg_alpha)

    def hide(self):
        canvas.unregister('overlay', self.draw)
        self.showing = False
        # with self.lock:
        #     if self.hiding or not self.showing:
        #         return
        #     now = time.perf_counter()
        #     self.hiding = True
        #     hide_s = Config.hide_ms / 1000
        #     # self.radius_anim = Animation(hide_s, self.radius_anim.value, 1000)
        #     # self.bg_anim = Animation(hide_s, self.bg_anim.value,  0)

    def _hide(self):
        with self.lock:
            canvas.unregister('overlay', self.draw)
            self.showing = False
            self.hiding = False
            return

    def draw(self, canvas):
        now = time.perf_counter()
        bg_alpha = int(Config.bg_alpha)
        radius_px = Config.radius_px
        # bg_alpha = int(self.bg_anim.value)
        # radius_px = self.radius_anim.value
        # if self.hiding and bg_alpha == 0:
        #     self._hide()
        #     return
        paint = canvas.paint

        paint.style = paint.Style.FILL

        # draw background
        paint.color = (0, 0, 0, bg_alpha)
        canvas.draw_rect(canvas.rect)

        # draw mouse circle
        paint.color = (0, 0, 0, 0)
        paint.blendmode = paint.Blend.SRC
        x, y = ctrl.mouse_pos()
        canvas.draw_circle(x, y, radius_px)

        # # draw mouse circle
        # x, y = ctrl.mouse_pos()

        # paint.style = paint.Style.FILL
        # paint.color = (255, 255, 255, 50)
        # canvas.draw_circle(x, y, radius_px)

        # paint.style = paint.Style.STROKE
        # paint.color = (255, 0, 0, 255)
        # canvas.draw_circle(x, y, radius_px)


halo = MouseHalo()
mod = Module()

MOUSE_NUDGE_AMOUNT = 10

@mod.action_class
class Actions:
    def mouse_center_screen(screen_num: int = None):
        """Moves mouse to center of screen"""
        screens = ui.screens()
        screen_index = screen_num - 1 if screen_num is not None else 0
        screen = screens[screen_index]
        rect = screen.rect
        ctrl.mouse_move(*rect.center)

    def mouse_center_active_window():
        """Moves mouse to center of the current window"""
        rect = ui.active_window().rect
        ctrl.mouse_move(*rect.center)

    def mouse_nudge(directions: str):
        """Moves mouse a fixed amount in the specified direction"""
        x, y = ctrl.mouse_pos()

        for direction in directions.split():
            if direction == "up":
                y -= MOUSE_NUDGE_AMOUNT
            elif direction ==  "down":
                y += MOUSE_NUDGE_AMOUNT
            elif direction ==  "left":
                x -= MOUSE_NUDGE_AMOUNT
            elif direction ==  "right":
                x += MOUSE_NUDGE_AMOUNT

        ctrl.mouse_move(x, y)

    def halo_show():
        "Show mouse halo"
        halo.show()

    def halo_hide():
        "Show mouse halo"
        halo.hide()
