from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: browser
browser.url: /asura\.gg\/manga/
browser.url: /mm-scans\.org\/manga\/\w+\/?$/
browser.url: /mangadex\.org\/title/
browser.url: /webtoons\.com\/.*\/list/
browser.url: /reaperscans\.com\/comics\/(?!.*chapters.*)/
"""

@ctx.action_class("user")
class Actions:
    def pedal_left():
        """Executes when pedal left is pressed"""
        actions.user.tab_close_wrapper()

    # def pedal_left_up():
    #     """Executes when pedal left is released"""

    # def pedal_right():
    #     """Executes when pedal right is pressed"""
    #     actions.insert("]]")

    # def pedal_right_up():
    #     """Executes when pedal right is released"""