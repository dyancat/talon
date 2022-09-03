tag: user.vim
-
#-------------------
#-- Basic actions --
#-------------------
line insert: 'I'
line append: 'A'
#reset: key(esc:3)

#------------------
#-- Text actions --
#------------------
# Word/line motions
# e.g. 'change 2 words'
{user.text_operator} [<number>] {user.text_motion}: "{text_operator}{number or ''}{text_motion}"

# Letter motions
# e.g. 'change 2nd brace'
jump [<user.ordinals>] {user.character}: "{ordinals or ''}f{character}"
{user.text_operator} (over|on) [<user.ordinals>]: "{text_operator}{ordinals or ''}f"
{user.text_operator} before [<user.ordinals>]: "{text_operator}{ordinals or ''}t"
{user.text_operator} back [over|on] [<user.ordinals>]: "{text_operator}{ordinals or ''}F"
{user.text_operator} back after [<user.ordinals>]: "{text_operator}{ordinals or ''}T"

#--------------------
#-- Object actions --
#--------------------
# e.g. 'delete block'
{user.object_operator} {user.object_motion_default_modifier}:
	"{object_operator}{object_motion_default_modifier}"

# e.g. 'change around brack'
{user.object_operator} {user.object_motion_modifier} {user.object_motion}:
	"{object_operator}{object_motion_modifier}{object_motion}"

#------------------
#-- Line actions --
#------------------
# e.g. 'change line'
{user.line_operator} [<number>] (line | lines): "{number or ''}{line_operator}"

#-------------------
#-- Miscellaneous --
#-------------------
wrap {user.object_motion_modifier} {user.object_motion}: "ys{object_motion_modifier}{object_motion}"
wrap selection: "S"

reselect: 'gv'
register {user.character}: '"{character}'

go definition: 'gd'

view top: 'zt'
view middle: 'zz'
view bottom: 'zb'

#----------------
#-- Easymotion --
#----------------
jump letter: "\\\\s"
jump word: "\\\\\\bdw"

#-----------
#-- Sneak --
#-----------
sneak {user.character} {user.character}: 's{character_1}{character_2}'
sneak back {user.character} {user.character}: 'S{character_1}{character_2}'
sneak: 's'
sneak back: 'S'

#------------------------------------
#-- Overriding line_commands.talon --
#------------------------------------
go <number>: '{number}G'
go <number> end: '{number}G$'