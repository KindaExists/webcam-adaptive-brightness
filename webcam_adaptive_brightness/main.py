#!/usr/bin/python
# -*- coding: utf-8 -*-
import ctypes
import logging
import sys
import os

from core import Core
from user_interface import app

if __name__ == '__main__':
    # Load time logger file
    if getattr(sys, 'frozen', False):
        logging.basicConfig(filename=os.path.abspath(os.path.dirname(sys.executable)+'/time_logger.log'),
                            filemode='a+', level=logging.INFO, format='%(asctime)s - %(message)s')
    else:
        logging.basicConfig(filename=os.path.abspath(os.path.dirname(__file__)+'/time_logger.log'),
                            filemode='a+', level=logging.INFO, format='%(asctime)s - %(message)s')
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

    core = Core()
    core.setup_external()
    core.setup_helpers()

    root = app.App(core)
    root.mainloop()