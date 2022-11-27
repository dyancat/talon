from talon import Context, actions, ctrl, ui
import time

ctx = Context()
ctx.matches = r"""
tag: browser
browser.url: /yande\.re\/post?(\/.*)?/
"""

@ctx.action_class("user")
class Actions:
    def pedal_left():
        """Executes when pedal left is pressed"""
        actions.insert("[[")

    def pedal_left_up():
        """Executes when pedal left is released"""

    # def pedal_middle():
    #     """Executes when pedal middle is pressed"""

    # def pedal_middle_up():
    #     """Executes when pedal middle is released"""

    def pedal_right():
        """Executes when pedal right is pressed"""
        actions.insert("]]")

    def pedal_right_up():
        """Executes when pedal right is released"""