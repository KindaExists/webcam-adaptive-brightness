#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk
import customtkinter as ctk

from user_interface.constants import COLOR


class FooterFrame(ctk.CTkFrame):
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

        self.__init_widgets()

    def __init_widgets(self):
        self.label_variable = tk.StringVar()
        self.label = tk.Label(
            self,
            textvariable=self.label_variable,
            font=('Bahnschrift Light', 10),

            bg=COLOR['dark_gray_3'],
            fg=COLOR['white'],
            justify='center',
        )
        self.set_webcam_name()
        self.label.place(x=10, rely=0.5, anchor='w')

    def set_webcam_name(self):
        if self.controller.core.webcam.active_cam_in_list():
            self.label_variable.set(f'Active Camera: {self.controller.core.webcam.active_cam_name}')
        else:
            self.label_variable.set(f'Active Camera: No Camera Found')