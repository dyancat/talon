tag: browser
-
# Adds some key presses so chrome go back behaviour works
(jump|click) <user.rango_target>:
  user.rango_command_with_target("clickElement", rango_target)

# Open in a new tab
ground <user.rango_target>:
  user.rango_command_with_target("openInBackgroundTab", rango_target)

fly: user.rango_command_without_target("scrollUpPage")
#upper <number>: user.rango_command_without_target("scrollUpPage", number)
#upper all: user.rango_command_without_target("scrollUpPage", 9999)
#tiny up: user.rango_command_without_target("scrollUpPage", 0.2)

fall: user.rango_command_without_target("scrollDownPage")
#downer <number>: user.rango_command_without_target("scrollDownPage", number)
#downer all: user.rango_command_without_target("scrollDownPage", 9999)
#tiny down: user.rango_command_without_target("scrollDownPage", 0.2)

go home: user.rango_command_without_target("navigateToPageRoot")
#page next: user.rango_command_without_target("navigateToNextPage")
#page last: user.rango_command_without_target("navigateToPreviousPage")