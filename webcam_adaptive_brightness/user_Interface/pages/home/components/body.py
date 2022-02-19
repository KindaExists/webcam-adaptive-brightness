#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk
import customtkinter as ctk

from user_interface.constants import COLOR


class BodyFrame(ctk.CTkFrame):
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
        self.columnconfigure(0)
        self.columnconfigure(1)
        self.columnconfigure(2, weight=2)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        self.ambient_display_frame = AmbientDisplayFrame(self, self.controller)
        self.ambient_display_frame.grid(column=0, row=0, padx=(20, 0), pady=20, sticky='nswe')

        self.screen_display_frame = ScreenDisplayFrame(self, self.controller)
        self.screen_display_frame.grid(column=1, row=0, padx=(20, 20), pady=20, sticky='nswe')

        self.webcam_display_frame = WebcamDisplayFrame(self, self.controller)
        self.webcam_display_frame.grid(column=2, row=0, padx=(0, 20), pady=20, sticky='nswe')


class AmbientDisplayFrame(ctk.CTkFrame):
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
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=12)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        self.ambient_label_frame = AmbientLabelFrame(self, self.controller)
        self.ambient_label_frame.grid(column=0, row=0, pady=(0, 20), sticky='nswe')

        self.ambient_value_frame = AmbientValueFrame(self, self.controller)
        self.ambient_value_frame.grid(column=0, row=1, sticky='nswe')

class AmbientLabelFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            corner_radius=20,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__init_widgets()

    def __init_widgets(self):
        self.label = tk.Label(
            self,
            text='Ambient Brightness',
            font=('Bahnschrift Light', 11),

            bg=COLOR['dark_gray_3'],
            fg=COLOR['white'],
            justify='center',
        )

        self.label.grid(column=0, row=0)

class AmbientValueFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            corner_radius=20,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__init_widgets()

    def __init_widgets(self):
        self.value = tk.Label(
            self,
            text=f'100%',
            font=('Monospace', 36),

            bg=COLOR['dark_gray_3'],
            fg=COLOR['white'],
            justify='center',
        )
        self.set_value(100)
        self.value.grid(column=0, row=0)

    def set_value(self, ambient_value):
        self.value.configure(text=f'{ambient_value}%')


class ScreenDisplayFrame(ctk.CTkFrame):
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
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=12)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        self.screen_label_frame = ScreenLabelFrame(self, self.controller)
        self.screen_label_frame.grid(column=0, row=0, pady=(0, 20), sticky='nswe')

        self.screen_value_frame = ScreenValueFrame(self, self.controller)
        self.screen_value_frame.grid(column=0, row=1, sticky='nswe')

class ScreenLabelFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            corner_radius=20,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__init_widgets()

    def __init_widgets(self):
        self.label = tk.Label(
            self,
            text='Screen Brightness',
            font=('Bahnschrift Light', 11),

            bg=COLOR['dark_gray_3'],
            fg=COLOR['white'],
            justify='center',
        )

        self.label.grid(column=0, row=0)

class ScreenValueFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            corner_radius=20,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__init_widgets()

    def __init_widgets(self):
        self.value = tk.Label(
            self,
            text=f'100%',
            font=('Monospace', 36),

            bg=COLOR['dark_gray_3'],
            fg=COLOR['white'],
            justify='center',
        )
        self.set_value(100)
        self.value.grid(column=0, row=0)

    def set_value(self, screen_value):
        self.value.configure(text=f'{screen_value}%')


class WebcamDisplayFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            corner_radius=20,
        )

        self.__init_widgets()

    def __init_widgets(self):
        self.label = tk.Label(
            self,
            text='Webcam Preview',
            font=('Bahnschrift Light', 11),
            bg=COLOR['dark_gray_3'],
            fg=COLOR['white'],
            justify='center',
            bd=-2,
            highlightthickness = 0
        )
        self.label.pack(side=tk.TOP, pady=(18, 0))

        self.webcam_preview = tk.Label(
            self,
            bg=COLOR['black'],
            width=340,
            height=255,
        )
        self.webcam_preview.place(width=340, height=255, relx=0.5, rely=0.55, anchor='center')

        self.image = None

    def set_image(self, image_object):
        self.image = image_object
        self.webcam_preview.configure(
            image = self.image
        )