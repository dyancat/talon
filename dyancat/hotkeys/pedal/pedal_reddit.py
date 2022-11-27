from talon import Context, actions, cron
from datetime import datetime

ctx = Context()
ctx.matches = r"""
tag: browser
browser.url: /reddit.com(?!.*comments.*)/
browser.url: /reddit.com\/r\/\w+(?!.*comments.*)/
"""

left_long_pressed = False

def on_left_long_pressed():
    global left_long_pressed
    actions.key("k")
    left_long_pressed = True

@ctx.action_class("user")
class Actions:
    def pedal_left():
        """Executes when pedal left is pressed"""
        global left_pressed_job
        left_pressed_job = cron.after("300ms", on_left_long_pressed)

    def pedal_left_up():
        """Executes when pedal left is released"""
        global left_pressed_job, left_long_pressed

        if left_pressed_job:
            cron.cancel(left_pressed_job)

        if not left_long_pressed:
            actions.key("a")

        left_long_pressed = False

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