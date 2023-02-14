from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: browser
browser.url: /jpdb\.io\/review/
"""

@ctx.action_class("user")
class Actions:
    def pedal_left():
        """Executes when pedal left is pressed"""
        actions.key("shift-tab")

    def pedal_middle():
        """Executes when pedal middle is pressed"""
        actions.key("space")

    def pedal_right():
        """Executes when pedal right is pressed"""
        actions.key("tab")