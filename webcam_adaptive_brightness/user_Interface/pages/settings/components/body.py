#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import tkinter as tk
import customtkinter as ctk
import numpy as np

from user_interface.pages.settings.components.input_frames import *
from user_interface.pages.settings.components.graph_frames import *
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
        self.columnconfigure(0, weight=7)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        self.left_body_frame = LeftBodyFrame(self, self.controller)
        self.left_body_frame.grid(column=0, row=0, padx=20, pady=20, sticky='nswe')

        self.right_body_frame = RightBodyFrame(self, self.controller)
        self.right_body_frame.grid(column=1, row=0, padx=(0, 20), pady=20, sticky='nswe')


class LeftBodyFrame(ctk.CTkFrame):
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
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1)
        self.rowconfigure(2)

        self.__init_widgets()

    def __init_widgets(self):
        self.settings_main = SettingsMainFrame(self, self.controller)
        self.settings_main.grid(column=0, row=0, sticky='nswe')

        self.settings_description = SettingsDescriptionFrame(self, self.controller)
        self.settings_description.grid(column=0, row=1, pady=20, sticky='nswe')

        self.settings_apply = ApplySettingsFrame(self, self.controller)
        self.settings_apply.grid(column=0, row=2, sticky='nswe')


class SettingsMainFrame(ctk.CTkFrame):
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
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        self.device_input_frame = DeviceInputFrame(self, self.controller)
        self.device_input_frame.grid(column=0, row=0, padx=(0, 10), sticky='nswe')

        self.interval_input_frame = IntervalInputFrame(self, self.controller)
        self.interval_input_frame.grid(column=1, row=0, padx=(10, 0), sticky='nswe')

        self.threshold_input_frame = ThresholdInputFrame(self, self.controller)
        self.threshold_input_frame.grid(column=0, row=1, padx=(0, 10), sticky='nswe')

        self.samples_input_frame = SamplesInputFrame(self, self.controller)
        self.samples_input_frame.grid(column= 1, row=1, padx=(10, 0), sticky='nswe')

        self.preview_checkbox_frame = PreviewCheckboxFrame(self, self.controller)
        self.preview_checkbox_frame.grid(column=0, row=2, padx=(0, 10), sticky='nswe')

        self.start_up_checkbox_frame = StartUpCheckboxFrame(self, self.controller)
        self.start_up_checkbox_frame.grid(column=1, row=2, padx=(10, 0), sticky='nswe')


class SettingsDescriptionFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            height=100,
            corner_radius=10,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        description_label = tk.Label(
            self,
            text='(Hover on settings to get description)',
            font=('Bahnschrift Light', 10),
            justify='center',

            bg=COLOR['dark_gray_3'],
            fg=COLOR['white'],
        )
        description_label.grid(column=0, row=0)


class ApplySettingsFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_2'],
            height=60,
            corner_radius=0,
        )

        self.pack_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        self.apply_settings_button = ApplySettingsButton(self, self.controller)
        self.apply_settings_button.pack(side=tk.LEFT, fill=tk.Y)

        self.reset_settings_button = ResetSettingsButton(self, self.controller)
        self.reset_settings_button.pack(side=tk.LEFT, fill=tk.Y, padx=10)


class ApplySettingsButton(ctk.CTkButton):
    def __init__(self, master, controller):
        self.controller = controller
        self.save_icon = tk.PhotoImage(file=os.path.abspath(__file__+'/../../../../assets/baseline_save_white.png'))

        super().__init__(
            master,
            text='Apply Settings',
            text_font=('Bahnschrift SemiBold', 10),
            image=self.save_icon,

            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_4'],
            hover_color=COLOR['hover'],
            text_color=COLOR['white'],

            compound='left',
            corner_radius=20,
        )
        self.disable_button()

        self.bind_tree(self, '<Button-1>', self.__button_clicked)
        self.bind_tree(self, '<ButtonRelease-1>', self.__button_released)

    def __button_clicked(self, event):
        if self.state == tk.NORMAL:
            self.configure(
                fg_color=COLOR['fg'],
            )
            self.controller.save_settings()

    def __button_released(self, event):
        if self.state == tk.NORMAL:
            self.configure(
                fg_color=COLOR['dark_gray_3'],
            )

    def enable_button(self):
        self.configure(
            state=tk.NORMAL,
            fg_color=COLOR['dark_gray_4'],
            text_color=COLOR['white'],
        )

    def disable_button(self):
        self.configure(
            state=tk.DISABLED,
            fg_color=COLOR['dark_gray_3'],
            text_color=COLOR['dark_gray_5'],
        )

    def bind_tree(self, master_widger, event, master_callback):
        # Binds an event to a widget and all its descendants
        master_widger.bind(event, master_callback)

        for child in master_widger.children.values():
            self.bind_tree(child, event, master_callback)


class ResetSettingsButton(ctk.CTkButton):
    def __init__(self, master, controller):
        self.controller = controller

        super().__init__(
            master,
            text='Reset Changes',
            text_font=('Bahnschrift SemiBold', 10),

            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_4'],
            hover_color=COLOR['hover'],
            text_color=COLOR['white'],

            corner_radius=20,
        )
        self.disable_button()

        self.bind_tree(self, '<Button-1>', self.__button_clicked)
        self.bind_tree(self, '<ButtonRelease-1>', self.__button_released)

    def __button_clicked(self, event):
        if self.state == tk.NORMAL:
            self.configure(
                fg_color=COLOR['fg'],
            )
            self.controller.load_saved_settings()

    def __button_released(self, event):
        if self.state == tk.NORMAL:
            self.configure(
                fg_color=COLOR['dark_gray_3'],
            )

    def enable_button(self):
        self.configure(
            state=tk.NORMAL,
            fg_color=COLOR['dark_gray_4'],
            text_color=COLOR['white'],
        )

    def disable_button(self):
        self.configure(
            state=tk.DISABLED,
            fg_color=COLOR['dark_gray_3'],
            text_color=COLOR['dark_gray_5'],
        )

    def bind_tree(self, master_widger, event, master_callback):
        # Binds an event to a widget and all its descendants
        master_widger.bind(event, master_callback)

        for child in master_widger.children.values():
            self.bind_tree(child, event, master_callback)


class RightBodyFrame(ctk.CTkFrame):
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
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        self.graph_main_frame = GraphMainFrame(self, self.controller)
        self.graph_main_frame.grid(column=0, row=0)

        self.ambient_value_variable = tk.StringVar()
        self.screen_value_variable = tk.StringVar()
        self.last_selected_point = None
        vcmd = (self.register(self.__validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.canvas_ref = self.graph_main_frame.graph_input_frame.graph_canvas


        point_values_frame = ctk.CTkFrame(
            self,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_2'],
            corner_radius=0,
        )
        point_values_frame.columnconfigure(0, weight=1)
        point_values_frame.columnconfigure(1, weight=1)
        point_values_frame.rowconfigure(0, weight=1)
        point_values_frame.rowconfigure(1)

        self.ambient_value_label = tk.Label(
            point_values_frame,
            text='Ambient %',
            font=('Bahnschrift Light', 10),
            justify='center',
            bg=COLOR['dark_gray_2'],
            fg=COLOR['white'],
        )
        self.ambient_value_label.grid(column=0, row=0)

        self.screen_value_label = tk.Label(
            point_values_frame,
            text='Screen %',
            font=('Bahnschrift Light', 10),
            justify='center',
            bg=COLOR['dark_gray_2'],
            fg=COLOR['white'],
        )
        self.screen_value_label.grid(column=1, row=0)


        self.ambient_value_entry = ctk.CTkEntry(
            point_values_frame,
            text_font=('Bahnschrift Light', 10),
            justify='center',

            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            text_color=COLOR['white'],

            height=40,
            corner_radius=10,
        )
        self.ambient_value_entry.entry.configure(
            textvariable=self.ambient_value_variable,
            disabledbackground=COLOR['dark_gray_3'],
            state=tk.DISABLED,
            validate='key',
            validatecommand=vcmd,
        )

        self.ambient_value_variable.trace_add(
            'write', lambda name, index, mode, var=self.ambient_value_variable: \
            self.update_graph()
        )
        self.ambient_value_entry.grid(column=0, row=1)


        self.screen_value_entry = ctk.CTkEntry(
            point_values_frame,
            text_font=('Bahnschrift Light', 10),
            justify='center',

            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            text_color=COLOR['white'],

            height=40,
            corner_radius=10,
        )
        self.screen_value_entry.entry.configure(
            textvariable=self.screen_value_variable,
            disabledbackground=COLOR['dark_gray_3'],
            state=tk.DISABLED,
            validate='key',
            validatecommand=vcmd,
        )
        self.screen_value_variable.trace_add(
            'write', lambda name, index, mode: \
            self.update_graph()
        )
        self.screen_value_entry.grid(column=1, row=1)

        self.ambient_value_variable.set(0)
        self.screen_value_variable.set(0)

        point_values_frame.grid(column=0, row=1, padx=10, pady=(0, 20), sticky='nswe')

    def select_point(self, point_id):
        if self.last_selected_point is None:
            self.ambient_value_entry.entry.configure(
                state=tk.NORMAL,
            )
            self.screen_value_entry.entry.configure(
                state=tk.NORMAL,
            )
        self.last_selected_point = point_id
        self.update_entries()

    def __validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed == '':
            return True
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False

    def update_entries(self):
        if self.last_selected_point is not None:
            x, y = self.canvas_ref.get_point_percentages(self.last_selected_point)
            self.ambient_value_variable.set(x)
            self.screen_value_variable.set(y)

    def update_graph(self):
        if self.last_selected_point is not None:
            ambient = self.ambient_value_variable.get() or 0
            screen = self.screen_value_variable.get() or 0
            x = np.clip(float(ambient), 0.0, 100.0) * 2
            y = (100 - np.clip(float(screen), 0.0, 100.0)) * 2
            self.canvas_ref.set_point_position(self.last_selected_point, x, y)