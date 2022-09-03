from talon import Context, actions, ui, Module, app, clip

mod = Module()

ctx = Context()
ctx.matches = r"""
app: vscode
"""

@ctx.action_class("user")
class UserActions:
    pass
    # def code_comment():
    #     actions.user.vscode("editor.action.commentLine")
    #     actions.key('esc')
    #     actions.key('esc')

    # def select_range(line_start: int, line_end: int):
    #     """Selects lines from line_start to line line_end"""
    #     actions.insert(str(line_start) + 'G')
    #     actions.insert('V')
    #     actions.insert(str(line_end) + 'G')

@ctx.action_class('edit')
class EditActions:
    pass
    # def delete():
    #     actions.insert('d')
    # def delete_line():
    #     actions.edit.select_line()
    #     actions.key('ctrl-backspace')
    # def delete_word():
    #     actions.insert('diw')
    # def indent_less():
    #     actions.insert('<<')
    # def indent_more():
    #     actions.insert('>>')
    # def select_line(n: int=None):
    #     actions.key('home')
    #     actions.key('shift-end')
    # def select_none():
    #     actions.key('esc')
    # def select_word():
    #     actions.insert('viw')
    # def undo():
    #     actions.key('esc')
    #     actions.key('ctrl-z')
    #     actions.key('esc')
    #     actions.key('esc')

    def line_clone():
        actions.user.vscode("editor.action.copyLinesDownAction")