from talon import Module, Context, actions

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def pedal_left():
        """Executes when F20 is pressed"""

    def pedal_left_up():
        """Executes when F20 is released"""

    def pedal_middle():
        """Executes when F21 is pressed"""

    def pedal_middle_up():
        """Executes when F21 is released"""

    def pedal_right():
        """Executes when F22 is pressed"""

    def pedal_right_up():
        """Executes when F22 is released"""

@ctx.action_class("user")
class Actions:
    def pedal_left():
        """Executes when F20 is pressed"""
        actions.key("left")

    def pedal_left_up():
        """Executes when F20 is released"""

    def pedal_middle():
        """Executes when F21 is pressed"""
        actions.user.mouse_center_active_window()
        actions.user.scroll_on()

    def pedal_middle_up():
        """Executes when F21 is released"""
        actions.user.scroll_off()

    def pedal_right():
        """Executes when F22 is pressed"""
        actions.key("right")

    def pedal_right_up():
        """Executes when F22 is released"""