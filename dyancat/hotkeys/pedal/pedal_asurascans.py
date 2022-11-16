from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: browser
browser.host: /asurascans\.com/
browser.host: /asura\.gg/
"""

@ctx.action_class("user")
class Actions:
    def function20():
        """Executes when F20 is pressed"""
        actions.insert("[[")

    def function20_up():
        """Executes when F20 is released"""

    def function22():
        """Executes when F22 is pressed"""
        actions.insert("]]")

    def function22_up():
        """Executes when F22 is released"""