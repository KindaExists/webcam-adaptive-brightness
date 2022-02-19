#!/usr/bin/python
# -*- coding: utf-8 -*-
import ctypes

from core import Core
from user_interface import app

if __name__ == '__main__':
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

    core = Core()
    core.setup_external()
    core.setup_helpers()

    root = app.App(core)
    root.mainloop()