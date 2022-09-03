os: windows
-
alter tablet:
	key(alt-tab)
	sleep(50ms)
	user.window_highlight()
snap full: user.window_max()
snap min:
	user.window_min()
	sleep(50ms)
	user.window_highlight()
snap restore: user.window_restore()
focus <user.running_applications>:
	user.switcher_focus(running_applications)
	sleep(50ms)
	user.window_highlight()
#go screen <number>:
#	user.focus_screen(number)
screen one: user.focus_screen(1)
screen two: user.focus_screen(2)
screen three: user.focus_screen(3)
^screen debug: user.debug_screen()
snap screen <number>:
	user.move_window_to_screen(number)
	sleep(50ms)
	user.window_max()
snap next: key(super-shift-right)
snap last: key(super-shift-left)