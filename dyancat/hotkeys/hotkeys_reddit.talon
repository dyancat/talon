tag: browser
browser.host: /reddit\.com/
-

next: "j"
last: "k"
open: "e"
^blank$:
	"E"
	sleep(180ms)
	app.tab_next()

gallery next: "}"
gallery last: "{"