from talon import Module, Context, actions

mod = Module()
ctx = Context()

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
        actions.key("left")

    def pedal_left_up():
        """Executes when pedal left is released"""

    def pedal_middle():
        """Executes when pedal middle is pressed"""
        actions.user.mouse_center_active_window()
        actions.user.scroll_on()

    def pedal_middle_up():
        """Executes when pedal middle is released"""
        actions.user.scroll_off()

    def pedal_right():
        """Executes when pedal right is pressed"""
        actions.key("right")

    def pedal_right_up():
        """Executes when pedal right is released"""