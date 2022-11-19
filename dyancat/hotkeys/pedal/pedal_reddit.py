from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: browser
browser.url: /reddit.com(?!.*comments.*)/
browser.url: /reddit.com\/r\/\w+(?!.*comments.*)/
"""

@ctx.action_class("user")
class Actions:
    def pedal_left():
        """Executes when F20 is pressed"""
        actions.key("a")

    def pedal_left_up():
        """Executes when F20 is released"""

    def pedal_middle():
        """Executes when F21 is pressed"""
        actions.key("j")

    def pedal_middle_up():
        """Executes when F21 is released"""

    def pedal_right():
        """Executes when F22 is pressed"""
        actions.key("E")

    def pedal_right_up():
        """Executes when F22 is released"""