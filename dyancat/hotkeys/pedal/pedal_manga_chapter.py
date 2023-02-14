from talon import Context, actions, cron

ctx = Context()
ctx.matches = r"""
tag: browser
browser.url: /asurascans\.com(.*chapter.*)/
browser.url: /reaperscans\.com\/comics\/(.*chapters.*)/
"""

left_long_pressed = False

def on_left_long_pressed():
    global left_long_pressed
    actions.user.mouse_center_active_window()
    actions.user.scroll_on("UP")
    left_long_pressed = True

@ctx.action_class("user")
class Actions:
    def pedal_left():
        """Executes when pedal left is pressed"""
        global left_pressed_job
        left_pressed_job = cron.after("200ms", on_left_long_pressed)

    def pedal_left_up():
        """Executes when pedal left is released"""
        global left_pressed_job, left_long_pressed

        if left_pressed_job:
            cron.cancel(left_pressed_job)

        if not left_long_pressed:
            actions.user.rango_command_without_target("navigateToPreviousPage")

        left_long_pressed = False
        actions.user.scroll_off()

    def pedal_right():
        """Executes when pedal right is pressed"""
        actions.user.rango_command_without_target("navigateToNextPage")

    def pedal_right_up():
        """Executes when pedal right is released"""