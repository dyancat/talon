mode: all
-
drowse:
	speech.disable()
drowse all:
	speech.disable()
	key(alt-.)
undrowse:
	speech.enable()
	user.window_highlight()
undrowse all:
	speech.enable()
	key(alt-.)
	user.window_highlight()

press control: key(ctrl)

sound speakers:
	speech.disable()
	app.notify("Speakers", "Output device")
	key(f18)

sound headphones:
	speech.enable()
	app.notify("Headphones", "Output device")
	key(f19)