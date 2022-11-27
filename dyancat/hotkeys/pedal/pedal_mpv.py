from talon import Context, actions, cron
from datetime import datetime

ctx = Context()
ctx.matches = r"""
os: windows
and app.name: mpv
os: windows
and app.exe: mpv.exe
"""

@ctx.action_class("user")
class Actions:
    def pedal_middle():
        """Executes when pedal middle is pressed"""
        actions.key("space")

    def pedal_middle_up():
        """Executes when pedal middle is released"""
