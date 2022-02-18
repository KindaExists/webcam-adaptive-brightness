#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import tkinter as tk
import customtkinter as ctk
import toml

from user_interface.pages.home.home_ctk import HomeFrame
from user_interface.pages.settings.settings_ctk import SettingsFrame
from user_interface.constants import COLOR

class App(ctk.CTk):
    def __init__(self):
        super().__init__(
            bg=COLOR['dark_gray_2']
        )

        # Set window title
        self.title('Webcam Adaptive-Brightness')

        # Sizes and centers window
        self.window_size = [880, 495]
        positionRight = int(self.winfo_screenwidth() / 2 - self.window_size[0] / 2)
        positionDown = int(self.winfo_screenheight() / 2 - self.window_size[1] / 2)
        self.geometry(f'{self.window_size[0]}x{self.window_size[1]}+{positionRight}+{positionDown}')
        self.resizable(False, False)

        self.iconbitmap(os.path.dirname(os.path.abspath(__file__)) + '/assets/icon.ico')
        self.protocol('WM_DELETE_WINDOW', self.on_closing)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        self.home_frame = HomeFrame(self, self)
        self.home_frame.grid(column=0, row=0, sticky='nswe')
        self.settings_frame = SettingsFrame(self, self)
        self.settings_frame.grid(column=0, row=0, sticky='nswe')


        self.are_changes_saved = True
        with open(os.path.abspath(__file__+'/../../configs.toml'), 'r+') as fp:
            self.config = toml.load(fp)
        self.open_frame('home')
        self.load_saved_settings()


    def on_closing(self):
        self.destroy()

    def open_frame(self, frame_name):
        if frame_name == 'home':
            self.home_frame.tkraise()
        if frame_name == 'settings':
            self.settings_frame.tkraise()


    def set_ambient_display(self, new_value):
        ambient_value_frame = self.home_frame.body_frame.ambient_display_frame.ambient_value_frame
        ambient_value_frame.set_value(new_value)

    def set_screen_display(self, new_value):
        screen_value_frame = self.home_frame.body_frame.screen_display_frame.screen_value_frame
        screen_value_frame.set_value(new_value)

    def set_webcam_display(self, new_image):
        webcam_display_frame = self.home_frame.body_frame.webcam_display_frame
        webcam_display_frame.set_image(new_image)

    def enable_save(self):
        settings_apply = self.settings_frame.body_frame.left_body_frame.settings_apply
        settings_apply.apply_settings_button.enable_button()
        settings_apply.reset_settings_button.enable_button()
        self.are_changes_saved = False

    def disable_save(self):
        settings_apply = self.settings_frame.body_frame.left_body_frame.settings_apply
        settings_apply.apply_settings_button.disable_button()
        settings_apply.reset_settings_button.disable_button()
        self.are_changes_saved = True

    def save_settings(self):
        settings_main = self.settings_frame.body_frame.left_body_frame.settings_main
        settings_graph = self.settings_frame.body_frame.right_body_frame.graph_main_frame.graph_input_frame.graph_canvas

        new_config = {}
        new_config['settings'] = {}
        new_settings = new_config['settings']

        new_settings['update_interval'] = int(settings_main.interval_input_frame.get_value())
        new_settings['threshold'] = float(settings_main.threshold_input_frame.get_value())
        new_settings['samples_per_update'] = int(settings_main.samples_input_frame.get_value())

        (ambient_a, screen_a), (ambient_b, screen_b)= settings_graph.get_all_percentages()
        new_settings['ambient_percentages'] = [ambient_a, ambient_b]
        new_settings['screen_percentages'] = [screen_a, screen_b]

        new_settings['device_id'] = settings_main.device_input_frame.device_input.get_value()
        new_settings['on_startup_enabled'] = settings_main.start_up_checkbox_frame.get_value()
        new_settings['preview_enabled'] = settings_main.preview_checkbox_frame.get_value()

        self.config = new_config
        with open(os.path.dirname(os.path.abspath(__file__)) + '/configs.toml', 'r+') as fp:
            toml.dump(self.config, fp)

        self.disable_save()

    def load_saved_settings(self):
        settings_main = self.settings_frame.body_frame.left_body_frame.settings_main
        settings_graph = self.settings_frame.body_frame.right_body_frame.graph_main_frame.graph_input_frame.graph_canvas

        config = self.config
        settings = config['settings']

        settings_main.interval_input_frame.set_value(settings['update_interval'])
        settings_main.threshold_input_frame.set_value(settings['threshold'])
        settings_main.samples_input_frame.set_value(settings['samples_per_update'])

        ambient = settings['ambient_percentages']
        screen = settings['screen_percentages']
        settings_graph.set_all_percentages(ambient, screen)

        settings_main.device_input_frame.device_input.set_value(settings['device_id'])
        settings_main.start_up_checkbox_frame.set_value(settings['on_startup_enabled'])
        settings_main.preview_checkbox_frame.set_value(settings['preview_enabled'])

        self.disable_save()

    def update_values(self):
        pass
        # Insert updates here


