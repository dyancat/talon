from talon import Module, Context, actions, cron

mod = Module()
ctx = Context()

left_long_pressed = False

def on_left_long_pressed():
    global left_long_pressed
    actions.user.mouse_center_active_window()
    actions.user.scroll_on("UP")
    left_long_pressed = True

@mod.action_class
class Actions:
    def pedal_left():
        """Executes when pedal left is pressed"""

    def pedal_left_up():
        """Executes when pedal left is released"""

    def pedal_middle():
        """Executes when pedal middle is pressed"""

    def pedal_middle_up():
        """Executes when pedal middle is released"""

    def pedal_right():
        """Executes when pedal right is pressed"""

    def pedal_right_up():
        """Executes when pedal right is released"""

@ctx.action_class("user")
class Actions:
    def pedal_left():
        """Executes when pedal left is pressed"""
        global left_pressed_job
        left_pressed_job = cron.after("200ms", on_left_long_pressed)

    def pedal_left_up():
        """Executes when pedal left is released"""
        global left_pressed_job, left_long_pressed

        if left_pressed_job:
            cron.cancel(left_pressed_job)

        if not left_long_pressed:
            actions.key("left")

        left_long_pressed = False
        actions.user.scroll_off()

    def pedal_middle():
        """Executes when pedal middle is pressed"""
        actions.user.mouse_center_active_window()
        actions.user.scroll_on("DOWN")

    def pedal_middle_up():
        """Executes when pedal middle is released"""
        actions.user.scroll_off()

    def pedal_right():
        """Executes when pedal right is pressed"""
        actions.key("right")

    def pedal_right_up():
        """Executes when pedal right is released"""