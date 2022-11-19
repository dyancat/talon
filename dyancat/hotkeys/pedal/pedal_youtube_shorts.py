from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: browser
browser.url: /youtube\.com\/shorts/
"""

@ctx.action_class("user")
class Actions:
    def pedal_left():
        """Executes when F20 is pressed"""
        actions.key("up")

    def pedal_left_up():
        """Executes when F20 is released"""

    def pedal_middle():
        """Executes when F21 is pressed"""
        actions.key("space")

    def pedal_middle_up():
        """Executes when F21 is released"""

    def pedal_right():
        """Executes when F22 is pressed"""
        actions.key("down")

    def pedal_right_up():
        """Executes when F22 is released"""