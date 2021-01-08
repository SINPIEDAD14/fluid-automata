import sys
import os
from cx_Freeze import*

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["pygame","math", "copy", "time", "os", "random"]}


setup(  name = "guifoo",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py")])