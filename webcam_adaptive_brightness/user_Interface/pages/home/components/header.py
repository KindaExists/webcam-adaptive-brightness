#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import tkinter as tk
import customtkinter as ctk

from user_interface.constants import COLOR, TEXT_FACTOR
from user_interface import images

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

        settings_button = SettingsButton(self, self.controller)
        settings_button.pack(side=tk.RIGHT, padx=10)


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
            text='| Home',
            font=('Bahnschrift Light', round(14 * TEXT_FACTOR)),
            justify='left',
            bg=COLOR['dark_gray_3'],
            fg=COLOR['white'],
        )
        subtitle.grid(column=1, row=0)

class SettingsButton(ctk.CTkButton):
    def __init__(self, master, controller):
        self.controller = controller
        self.settings_icon = tk.PhotoImage(data=images.baseline_settings_white)

        super().__init__(
            master,
            text='Settings',
            text_font=('Bahnschrift SemiBold', round(10 * TEXT_FACTOR)),
            image=self.settings_icon,

            bg_color=COLOR['dark_gray_3'],
            fg_color=COLOR['dark_gray_4'],
            hover_color=COLOR['hover'],
            text_color=COLOR['white'],

            compound='left',
            height=48,
            corner_radius=5,

            command=self.__open_settings,
        )

    def __open_settings(self):
        self.controller.open_frame('settings')