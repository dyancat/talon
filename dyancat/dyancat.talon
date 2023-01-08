# override repeat commands when said independently
^<number_small> times$: core.repeat_command(number_small)

#ordinals get confused sometimes, implement them manually
#^<user.ordinals>$: core.repeat_command(ordinals)
^twice$: core.repeat_command(2)
^third$: core.repeat_command(3)
^fourth$: core.repeat_command(4)
twice: core.repeat_command(1)
third: core.repeat_command(2)
fourth: core.repeat_command(3)

(gain|again): core.repeat_command(1)

semi: ';'
break: key(escape)
void: key(space)
^launch$: key(alt-space)

left: edit.left()
right: edit.right()
up: edit.up()
down: edit.down()

mic reset: user.reset_mic()