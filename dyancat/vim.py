from talon import Context, actions, ui, Module, app, clip

from ..code.keys import alphabet
from ..code.keys import symbol_key_words
from ..code.keys import punctuation_words

mod = Module()
mod.tag("vim", "commands for vim editors")
mod.list("text_operator", desc="Text operator")
mod.list("text_motion", desc="Text motion")
mod.list("object_operator", desc="Object operator")
mod.list("object_motion", desc="Object motion")
mod.list("object_motion_modifier", desc="Object motion modifier")
mod.list("object_motion_default_modifier", desc="Object motion with default modifier")
mod.list("line_operator", desc="Line operator")
mod.list("character", desc="Character")

ctx = Context()
ctx.matches = r"""
tag: user.vim
"""

text_or_object_operator = {
    "change": "c",
    "delete": "d",
    "visual": "v",
    "yank": "y",
    "comment": "gC"
}

text_operator = {
    **text_or_object_operator,
    "jump": "",
}

object_operator = {
    **text_or_object_operator,
    "tab": ">",
    "retab": "<",
}

text_motion = {
    "word": "w",
    "words": "w",
    "letter": "l",
    "letters": "l",
    "end": "e",
    "word end": "e",
    "words end": "e",
    "word back": "b",
    "words back": "b",
    "line end": "$",
}

object_motion_modifier = {
    "around": "a",
    "inner": "i",
    "inside": "i",
    "surrounding": "s",
}

object_motion = {
    "arg": "a",
    "argument": "a",
    "tag": "t",
    "word": "w",
    "quote": "'",
    "quotes": "'",
    "dubquote": '"',
    "dubquotes": '"',
    "double quote": '"',
    "double quotes": '"',
    "list": "[",
    "square": "[",
    "squares": "[",
    "paren": "(",
    "parens": "(",
    "block": "{",
    # "brack": "{",
    # "bracks": "{",
    "curly": "{",
    "angle": "<",
    "angles": "<",
    "grave": "`",
    "graves": "`",
}

object_motion_default_modifier = {
    **object_motion,
    "arg": "aa",
    "argument": "aa",
    "tag": "it",
    "quote": "i'",
    "quotes": "i'",
    "dubquote": 'i"',
    "dubquotes": 'i"',
    "double quote": 'i"',
    "double quotes": 'i"',
    "list": "i[",
    "square": "i[",
    "squares": "i[",
    "paren": "i(",
    "parens": "i(",
    "block": "i{",
    # "brack": "i{",
    # "bracks": "i{",
    "curly": "i{",
    "angle": "i<",
    "angles": "i<",
}


line_operator = {
    "change": "cc",
    "delete": "dd",
    "visual": "V",
    "yank": "yy",
    "tab": ">>",
    "retab": "<<",
    "comment": "gcc",
}


default_digits = "zero one two three four five six seven eight nine".split(" ")
numbers = [str(i) for i in range(10)]
number_key_words = dict(zip(default_digits, numbers))
uppercase_alphabet = {
    **{f'ship {code}': letter.upper() for (code, letter) in alphabet.items()},
    **{f'upper {code}': letter.upper() for (code, letter) in alphabet.items()},
    **{f'big {code}': letter.upper() for (code, letter) in alphabet.items()},
}

character = {
    "space": " "
}
character.update(alphabet)
character.update(uppercase_alphabet)
character.update(number_key_words)
character.update(symbol_key_words)
character.update(punctuation_words)

ctx.lists["user.text_operator"] = text_operator
ctx.lists["user.text_motion"] = text_motion
ctx.lists["user.object_operator"] = object_operator
ctx.lists["user.object_motion_modifier"] = object_motion_modifier
ctx.lists["user.object_motion"] = object_motion
ctx.lists["user.object_motion_default_modifier"] = object_motion_default_modifier
ctx.lists["user.line_operator"] = line_operator
ctx.lists["user.character"] = character
