#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

from user_interface.constants import COLOR, TEXT_FACTOR


class HeaderFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_3'],
            fg_color=COLOR['dark_gray_3'],
            height=60,
            corner_radius=0,
        )
        self.pack_propagate(False)
        self.__init_widgets()

    def __init_widgets(self):
        title_frame = TitleFrame(self)
        title_frame.pack(side=tk.LEFT)

        home_button = HomeButton(self, self.controller)
        home_button.pack(side=tk.RIGHT, padx=10)


class TitleFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_3'],
            fg_color=COLOR['dark_gray_3'],
            corner_radius=0,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.__init_widgets()

    def __init_widgets(self):
        title = tk.Label(
            self,
            text='WAABA 0.1.0',
            font=('Bahnschrift Bold', round(14 * TEXT_FACTOR)),
            justify='left',
            bg=COLOR['dark_gray_3'],
            fg=COLOR['white'],
        )
        title.grid(column=0, row=0, padx=(10, 0))

        subtitle = tk.Label(
            self,
            text='| Settings',
            font=('Bahnschrift Light', round(14 * TEXT_FACTOR)),
            justify='left',
            bg=COLOR['dark_gray_3'],
            fg=COLOR['white'],
        )
        subtitle.grid(column=1, row=0)

class HomeButton(ctk.CTkButton):
    def __init__(self, master, controller):
        self.controller = controller
        self.back_icon = tk.PhotoImage(file=os.path.abspath(__file__+'/../../../../assets/arrow_back_white.png'))

        super().__init__(
            master,
            text='Back to Home',
            text_font=('Bahnschrift SemiBold', round(10 * TEXT_FACTOR)),
            image=self.back_icon,

            bg_color=COLOR['dark_gray_3'],
            fg_color=COLOR['dark_gray_4'],
            hover_color=COLOR['hover'],
            text_color=COLOR['white'],

            compound='left',
            height=48,
            corner_radius=5,

            command=self.__open_home,
        )

    def __open_home(self):
        if not self.controller.are_changes_saved:
            response = messagebox.askyesnocancel('Save Settings?',
                'Would you like to save all your changes to the settings?')

            if response is None:
                return
            elif response:
                self.controller.save_settings()
                self.controller.open_frame('home')
            else:
                self.controller.load_saved_settings()
                self.controller.open_frame('home')
        else:
            self.controller.open_frame('home')
