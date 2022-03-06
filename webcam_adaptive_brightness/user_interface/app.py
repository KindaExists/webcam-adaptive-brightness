#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import base64
import threading
import time
import io

import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import pystray
from pystray import MenuItem as item

from user_interface import images
from user_interface.pages.home.home_ctk import HomeFrame
from user_interface.pages.settings.settings_ctk import SettingsFrame
from user_interface.constants import COLOR

class App(ctk.CTk):
    def __init__(self, core):
        self.core = core
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

        icon_data = base64.b64decode(images.icon)
        temp_file = 'icon.ico'
        with open(temp_file, 'wb') as icon_file:
            icon_file.write(icon_data)
        self.iconbitmap(temp_file)
        os.remove(temp_file)

        self.protocol('WM_DELETE_WINDOW', self.close_application)

        self.maximized = True

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        self.home_frame = HomeFrame(self, self)
        self.home_frame.grid(column=0, row=0, sticky='nswe')
        self.settings_frame = SettingsFrame(self, self)
        self.settings_frame.grid(column=0, row=0, sticky='nswe')

        self.home_frame.bind('<Map>', lambda _: self.show_application())
        self.home_frame.bind('<Unmap>', lambda _: self.hide_application())

        self.io_directory = self.generate_io_directory()

        self.are_changes_saved = True
        self.open_frame('home')
        self.__update_webcam_display()
        self.load_saved_settings()
        self.update_values()

    def close_application(self):
        try:
            self.icon.stop()
        except AttributeError as e:
            # Explicit pass, as this does just means we don't
            # have to close the icon
            pass
        self.core.release_external()
        self.destroy()

    def show_application(self):
        if self.core.configs.get_setting('minimize_to_tray'):
            if not self.maximized:
                self.icon.stop()
                self.deiconify()

                if self.widthdraw_thread:
                    self.maximized = True
                    self.widthdraw_thread.join()
                    self.widthdraw_thread = None

    def hide_application(self):
        if self.core.configs.get_setting('minimize_to_tray'):
            if self.maximized:
                self.maximized = False

                self.withdraw()

                self.widthdraw_thread = threading.Thread(target=self.__update_withdrawn)
                self.widthdraw_thread.start()

                self.image = Image.open(io.BytesIO(base64.b64decode(images.icon)))
                self.menu = (item('Quit', self.close_application), item('Show', self.show_application, default=True))
                self.icon = pystray.Icon('WAB', self.image, 'Webcam Adaptive-Brightness', self.menu)
                self.icon.run()

    def open_frame(self, frame_name):
        if frame_name == 'home':
            self.home_frame.tkraise()
        if frame_name == 'settings':
            self.io_directory['device_in'].update_device_list()
            is_device_input_valid = self.io_directory['device_in'].parent.get_save_validity()
            self.io_directory['device_in'].parent.set_invalid_color(is_device_input_valid)

            self.settings_frame.tkraise()



    def generate_io_directory(self):
        return {
            'ambient_out': self.home_frame.body_frame.ambient_display_frame.ambient_value_frame,
            'screen_out': self.home_frame.body_frame.screen_display_frame.screen_value_frame,
            'webcam_out': self.home_frame.body_frame.webcam_display_frame,
            'active_out': self.home_frame.footer_frame,
            'description_out': self.settings_frame.body_frame.left_body_frame.settings_description.description_text,
            'apply_btn': self.settings_frame.body_frame.left_body_frame.settings_apply,
            'device_in': self.settings_frame.body_frame.left_body_frame.settings_main.device_input_frame.device_input,
            'interval_in': self.settings_frame.body_frame.left_body_frame.settings_main.interval_input_frame,
            'threshold_in': self.settings_frame.body_frame.left_body_frame.settings_main.threshold_input_frame,
            'samples_in': self.settings_frame.body_frame.left_body_frame.settings_main.samples_input_frame,
            'preview_in': self.settings_frame.body_frame.left_body_frame.settings_main.preview_checkbox_frame,
            'tray_in': self.settings_frame.body_frame.left_body_frame.settings_main.tray_checkbox_frame,
            'graph_in': self.settings_frame.body_frame.right_body_frame.graph_main_frame.graph_input_frame.graph_canvas
        }

    def set_ambient_display(self, new_value):
        ambient_value_frame = self.io_directory['ambient_out']
        ambient_value_frame.set_value(new_value)

    def set_screen_display(self, new_value):
        screen_value_frame = self.io_directory['screen_out']
        screen_value_frame.set_value(new_value)

    def set_webcam_display(self, new_image):
        webcam_display_frame = self.io_directory['webcam_out']
        webcam_display_frame.set_image(new_image)

    def enable_save(self):
        settings_apply = self.io_directory['apply_btn']
        settings_apply.apply_settings_button.enable_button()
        settings_apply.reset_settings_button.enable_button()
        self.are_changes_saved = False

    def disable_save(self):
        settings_apply = self.io_directory['apply_btn']
        settings_apply.apply_settings_button.disable_button()
        settings_apply.reset_settings_button.disable_button()
        self.are_changes_saved = True

    def save_settings(self):
        if self.validate_setting_inputs():
            new_config = {}
            new_config['settings'] = {}
            new_settings = new_config['settings']

            new_settings['update_interval'] = self.io_directory['interval_in'].get_value()
            new_settings['threshold'] = self.io_directory['threshold_in'].get_value()
            new_settings['samples_per_update'] = self.io_directory['samples_in'].get_value()

            (ambient_a, screen_a), (ambient_b, screen_b) = self.io_directory['graph_in'].get_all_percentages()
            new_settings['ambient_percentages'] = [ambient_a, ambient_b]
            new_settings['screen_percentages'] = [screen_a, screen_b]

            new_settings['device_name'] = self.io_directory['device_in'].get_value()
            new_settings['preview_enabled'] = self.io_directory['preview_in'].get_value()
            new_settings['minimize_to_tray'] = self.io_directory['tray_in'].get_value()

            self.core.configs.save_configs(new_config)
            self.disable_save()

            webcam_changed = self.core.update_webcam_device()
            if webcam_changed:
                self.__update_webcam_display()
            self.core.update_helpers()


    def load_saved_settings(self):
        settings = self.core.configs.get_settings()

        self.io_directory['interval_in'].set_value(settings['update_interval'])
        self.io_directory['threshold_in'].set_value(settings['threshold'])
        self.io_directory['samples_in'].set_value(settings['samples_per_update'])

        ambient = settings['ambient_percentages']
        screen = settings['screen_percentages']
        self.io_directory['graph_in'].set_all_percentages(ambient, screen)

        self.io_directory['device_in'].set_value(settings['device_name'])
        self.io_directory['preview_in'].set_value(settings['preview_enabled'])
        self.io_directory['tray_in'].set_value(settings['minimize_to_tray'])

        self.disable_save()
        self.validate_setting_inputs()

    def update_values(self):
        had_update = self.core.update()
        if had_update:
            if self.core.webcam.active_cam_in_list():
                self.set_ambient_display(self.core.get_last_ambient_brightness())
                self.set_screen_display(self.core.get_last_screen_brightness())
            else:
                self.set_ambient_display('---')
                self.set_screen_display('---')
            self.io_directory['active_out'].set_webcam_name()
            self.__update_webcam_display()
        if had_update is None:
            self.io_directory['active_out'].set_webcam_name()
            self.set_ambient_display('---')
            self.set_screen_display('---')
            self.set_webcam_display(False)
        self.after(100, self.update_values)

    def __update_webcam_display(self):
        if self.core.configs.get_setting('preview_enabled') and self.core.webcam.active_cam_in_list():
            cap = self.core.get_converted_capture()
            if not cap is None:
                img = Image.fromarray(cap)
                imgtk = ImageTk.PhotoImage(img)
                self.set_webcam_display(imgtk)
            return

        self.set_webcam_display(False)

    def __update_withdrawn(self):
        # Run algorithm while tkinter window is withdrawn
        while not self.maximized:
            self.core.update()
            time.sleep(0.1)

    def refresh_devices(self):
        is_device_input_valid = self.io_directory['device_in'].parent.get_save_validity()
        self.io_directory['device_in'].parent.set_invalid_color(is_device_input_valid)

        self.core.refresh_devices()
        self.io_directory['device_in'].update_device_list()

    def validate_setting_inputs(self):
        is_device_input_valid = self.io_directory['device_in'].parent.get_save_validity()
        self.io_directory['device_in'].parent.set_invalid_color(is_device_input_valid)

        is_interval_input_valid = self.io_directory['interval_in'].get_save_validity()
        self.io_directory['interval_in'].set_invalid_color(is_interval_input_valid)

        is_threshold_input_valid = self.io_directory['threshold_in'].get_save_validity()
        self.io_directory['threshold_in'].set_invalid_color(is_threshold_input_valid)

        is_samples_input_valid = self.io_directory['samples_in'].get_save_validity()
        self.io_directory['samples_in'].set_invalid_color(is_samples_input_valid)

        return all([is_interval_input_valid, is_threshold_input_valid, is_samples_input_valid])

    def set_setting_description(self, is_valid, description_text, error_text):
        if is_valid:
            self.io_directory['description_out'].set_description_text(description_text, '')
        else:
            self.io_directory['description_out'].set_description_text(description_text, error_text)

    def remove_setting_description(self):
        self.io_directory['description_out'].set_default_text()

