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
        """Executes when pedal left is pressed"""
        actions.key("a")

    def pedal_left_up():
        """Executes when pedal left is released"""

    def pedal_middle():
        """Executes when pedal middle is pressed"""
        actions.key("j")

    def pedal_middle_up():
        """Executes when pedal middle is released"""

    def pedal_right():
        """Executes when pedal right is pressed"""
        actions.key("E")
        actions.sleep("180ms")
        actions.app.tab_next()

    def pedal_right_up():
        """Executes when pedal right is released"""