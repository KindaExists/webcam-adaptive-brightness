#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk
import customtkinter as ctk

from user_interface.constants import COLOR


class FooterFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_3'],
            fg_color=COLOR['dark_gray_3'],
            height=60,
            corner_radius=0,
        )