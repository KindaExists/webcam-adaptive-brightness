#!/usr/bin/python
# -*- coding: utf-8 -*-
import ctypes

from user_interface import app

if __name__ == '__main__':
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    root = app.App()
    root.mainloop()