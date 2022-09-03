from talon import Context, actions, ui, Module, app, clip

ctx = Context()
mod = Module()
mod.apps.xplorer2 = """
os: windows
and app.exe: xplorer2.exe
os: windows
and app.exe: xplorer2_64.exe
"""

ctx.matches = r"""
app: xplorer2
"""