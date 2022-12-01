from talon import actions, noise, Module, imgui, cron

mod = Module()

scroll_amount = 50
is_scrolling = False

def scroll_continuous_helper():
    global scroll_amount
    actions.mouse_scroll(by_lines=False, y=int(scroll_amount))

def toggle_scroll():
    global is_scrolling
    if is_scrolling:
        stop_scroll()
    else:
        start_scroll()

def start_scroll():
    global scroll_job, is_scrolling
    scroll_job = cron.interval("20ms", scroll_continuous_helper)
    is_scrolling = True

def stop_scroll():
    global scroll_amount, scroll_job, is_scrolling
    if scroll_job:
        cron.cancel(scroll_job)

    scroll_job = None
    is_scrolling = False

def on_hiss(active):
    if active:
        toggle_scroll()

@imgui.open(x=700, y=0)
def gui_scroll(gui: imgui.GUI):
    gui.text("Scroll hiss on")
    gui.line()
    if gui.button("Scroll hiss off"):
        actions.user.scroll_hiss_off()

@mod.action_class
class Actions:
    def scroll_hiss_on():
        """Enables hiss scroll mode"""
        noise.register("hiss", on_hiss)
        gui_scroll.show()

    def scroll_hiss_off():
        """Disables hiss scroll mode"""
        noise.unregister("hiss", on_hiss)
        stop_scroll()
        gui_scroll.hide()

    def scroll_on():
        """Enables scroll mode"""
        start_scroll()

    def scroll_off():
        """Disables scroll mode"""
        stop_scroll()