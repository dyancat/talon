from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: browser
browser.url: /reddit.com(.*comments.*)/
"""

@ctx.action_class("user")
class Actions:
    def pedal_left():
        """Executes when pedal left is pressed"""
        actions.user.tab_close_wrapper()

    # def pedal_left_up():
    #     """Executes when pedal left is released"""

    # def pedal_middle():
    #     """Executes when pedal middle is pressed"""

    # def pedal_middle_up():
    #     """Executes when pedal middle is released"""

    # def pedal_right():
    #     """Executes when pedal right is pressed"""

    # def pedal_right_up():
    #     """Executes when pedal right is released"""