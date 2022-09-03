import os, subprocess
from talon import Module

mod = Module()

@mod.action_class
class Actions:
    def talon_pull():
        """Updates the talon user git repo"""
        cwd = os.path.dirname(os.path.realpath(__file__))
        os.chdir(cwd)
        subprocess.run(["git", "pull"], shell=True)

    def talon_code():
        """Opens VSCode for the talon user repo"""
        cwd = os.path.dirname(os.path.realpath(__file__))
        os.chdir(cwd)
        git_root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], shell=True, text=True)
        subprocess.run(["code", git_root], shell=True)