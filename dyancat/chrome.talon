app: chrome
-
tab move:
	key(esc ctrl-l)
	sleep(50ms)
	key(f6 menu)
	sleep(50ms)
	key(m right)
tab menu:
	key(esc ctrl-l)
	sleep(50ms)
	key(f6 menu)

go page: key(ctrl-f6)
go bookmarks:
	key(esc ctrl-l)
	sleep(50ms)
	key(f6:2)
go home:
	key(esc)
	key(ctrl-f6)
	'gU'
go input: 'gi'
go frame: 'gF'
open {user.website}: browser.go(website)

page left: 'zH'
page right: 'zL'

[go] link next: ']]'
[go] link last: '[['