from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: browser
browser.url: /youtube\.com\/watch/
"""

@ctx.action_class("user")
class Actions:
    def function20():
        """Executes when F20 is pressed"""
        actions.key("j")

    def function20_up():
        """Executes when F20 is released"""

    def function21():
        """Executes when F21 is pressed"""
        actions.key("space")

    def function21_up():
        """Executes when F21 is released"""

    def function22():
        """Executes when F22 is pressed"""
        actions.key("l")

    def function22_up():
        """Executes when F22 is released"""