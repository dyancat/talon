os: windows
-
alter tablet:
	key(alt-tab)
	sleep(50ms)
	user.window_highlight()
(snap | nap) full: user.window_max()
(snap | nap) min:
	user.window_min()
	sleep(50ms)
	user.window_highlight()
(snap | nap) restore: user.window_restore()
focus <user.running_applications>:
	user.switcher_focus(running_applications)
	sleep(50ms)
	user.window_highlight()
#go screen <number>:
#	user.focus_screen(number)
(screen | play | display) one: user.focus_screen(1)
(screen | play | display) two: user.focus_screen(2)
(screen | play | display) three: user.focus_screen(3)
^screen debug: user.debug_screen()
(snap | nap) screen <number>:
	user.move_window_to_screen(number)
	sleep(50ms)
	user.window_max()
(snap | nap) next: key(super-shift-right)
(snap | nap) last: key(super-shift-left)