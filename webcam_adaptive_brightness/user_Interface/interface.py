#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import ctypes

import tkinter as tk
from tkinter import messagebox

from main import MainFrame
from settings import SettingsFrame

lightGrey = '#3A3A3A'
grey = '#262626'
black = 'black'
brightGrey = '#595959'
fgColor = '#5B9BD5'
errColor = '#FF5050'

window_width = 880
window_height = 495


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(
            bg=grey,
            highlightcolor=brightGrey,
            highlightthickness=1
        )

        self.title('WAABA')

        self.window_size = [880, 495]

        # Centers Window when it's opened
        positionRight = int(self.winfo_screenwidth() / 2 - self.window_size[0] / 2)
        positionDown = int(self.winfo_screenheight() / 2 - self.window_size[1] / 2)

        self.geometry(f'{self.window_size[0]}x{self.window_size[1]}+{positionRight}+{positionDown}')
        self.resizable(False, False)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        self.iconbitmap(os.path.dirname(os.path.abspath(__file__)) + '/assets/icon.ico')
        self.protocol('WM_DELETE_WINDOW', self.on_closing)

        self.main_frame = MainFrame(self)
        self.main_frame.grid(column=0, row=0, sticky='nswe')
        self.settings_frame = SettingsFrame(self)
        self.settings_frame.grid(column=0, row=0, sticky='nswe')

        self.open_frame('main')

    def on_closing(self):
        close = messagebox.askokcancel('Close Program',
                                    'Would you like to exit WAABP?\n\n' + \
                                    'Warning: Closing the program would\n' + \
                                    'stop all of its processes.')
        if close:
            self.destroy()

    def open_frame(self, frame_name):
        if frame_name == 'main':
            self.main_frame.tkraise()
        if frame_name == 'settings':
            self.settings_frame.tkraise()


if __name__ == '__main__':
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    app = App()
    app.mainloop()