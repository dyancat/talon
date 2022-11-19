from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: browser
browser.host: /asurascans\.com/
browser.host: /asura\.gg/
"""

@ctx.action_class("user")
class Actions:
    def pedal_left():
        """Executes when F20 is pressed"""
        actions.insert("[[")

    def pedal_left_up():
        """Executes when F20 is released"""

    def pedal_right():
        """Executes when F22 is pressed"""
        actions.insert("]]")

    def pedal_right_up():
        """Executes when F22 is released"""