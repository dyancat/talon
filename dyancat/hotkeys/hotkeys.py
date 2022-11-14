from talon import Module, Context, actions

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def function20():
        """Executes when F20 is pressed"""

    def function20_up():
        """Executes when F20 is released"""

    def function21():
        """Executes when F21 is pressed"""

    def function21_up():
        """Executes when F21 is released"""

    def function22():
        """Executes when F22 is pressed"""

    def function22_up():
        """Executes when F22 is released"""

@ctx.action_class("user")
class Actions:
    def function20():
        """Executes when F20 is pressed"""
        actions.key("left")

    def function20_up():
        """Executes when F20 is released"""

    def function21():
        """Executes when F21 is pressed"""
        actions.user.mouse_center_active_window()
        actions.user.scroll_on()

    def function21_up():
        """Executes when F21 is released"""
        actions.user.scroll_off()

    def function22():
        """Executes when F22 is pressed"""
        actions.key("right")

    def function22_up():
        """Executes when F22 is released"""