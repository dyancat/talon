import subprocess
from talon import Module, app, actions, cron

mod = Module()

reset_mic_job = None

def reset_mic():
    try:
        subprocess.run(r'D:\Dropbox\Backup\Autohotkey\SoundVolumeView.exe /SetVolume "Microphone" 99')
        subprocess.run(r'D:\Dropbox\Backup\Autohotkey\SoundVolumeView.exe /SetVolume "Microphone" 100')
    except:
        print("Failed to reset mic, skipping")


def on_ready():
    global reset_mic_job
    reset_mic()
    cron.cancel(reset_mic_job)
    reset_mic_job = cron.interval("10m", reset_mic)
    actions.speech.disable()


app.register("ready", on_ready)

@mod.action_class
class Actions:
    def reset_mic():
        """Resets the mic"""
        reset_mic()