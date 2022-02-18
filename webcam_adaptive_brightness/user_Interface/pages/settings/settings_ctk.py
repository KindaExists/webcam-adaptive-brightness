#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk
import customtkinter as ctk

from user_interface.pages.settings.components.header import HeaderFrame
from user_interface.pages.settings.components.body import BodyFrame
from user_interface.constants import COLOR


class SettingsFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_2'],
            corner_radius=0,
        )

        # Setup grid layout
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0)
        self.rowconfigure(1, weight = 1)

        self.__init_widgets()

    def __init_widgets(self):
        self.header_frame = HeaderFrame(self, self.controller)
        self.header_frame.grid(column=0, row=0, sticky='nswe')

        self.body_frame = BodyFrame(self, self.controller)
        self.body_frame.grid(column=0, row=1, sticky='nswe')