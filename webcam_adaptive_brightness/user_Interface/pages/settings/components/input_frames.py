#!/usr/bin/python
# -*- coding: utf-8 -*-
from email.mime import image
import os

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from user_interface.constants import COLOR


# ===================================================
# Webcam Device Input Frame
# ===================================================

webcam_list = ['0', '1', '2']

class DeviceInputFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_2'],
            corner_radius=0,
        )

        self.is_valid = True
        self.description = '\n\nChange the webcam device being used by the Application.'
        self.error_text = '\nWebcam ID not found. Please choose a different ID.'

        self.bind('<Enter>', self.set_description)
        self.bind('<Leave>', self.remove_description)

        # Setup grid layout
        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        device_label = tk.Label(
            self,
            font=('Bahnschrift Light', 10),
            text='Device: ',
            justify='left',

            bg=COLOR['dark_gray_2'],
            fg=COLOR['white'],
        )
        device_label.grid(column=0, row=0, sticky='w')

        self.device_input = DeviceInput(self, self.controller)
        self.device_input.grid(column=1, row=0, sticky='we')

    def set_description(self, event):
        self.controller.set_setting_description(self.is_valid, self.description, self.error_text)

    def remove_description(self, event):
        self.controller.remove_setting_description()


class DeviceInput(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            height=40,
            corner_radius=10,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        self.expand_icon = tk.PhotoImage(file=os.path.abspath(__file__+'/../../../../assets/outline_expand_white.png'))
        self.device_variable = tk.StringVar()

        self.device_menu = tk.OptionMenu(
            self,
            self.device_variable,
            *webcam_list,
        )
        self.device_variable.set(webcam_list[0])

        self.device_menu.configure(
            width=16,
            font=('Bahnschrift Light', 10),
            anchor=tk.W,
            background=COLOR['dark_gray_3'],
            foreground=COLOR['white'],

            bd=0,
            border=0,
            borderwidth=0,
            highlightthickness=0,
            relief=tk.FLAT,

            highlightbackground=COLOR['dark_gray_3'],
            highlightcolor=COLOR['dark_gray_3'],
            activebackground=COLOR['dark_gray_3'],
            activeforeground=COLOR['white'],

            image=None,
            bitmap=None,
            indicatoron=False,
            cursor='hand2',
        )
        self.device_menu.grid(column=0, row=0, sticky='ns')
        expand_button = tk.Label(
            self,
            background=COLOR['dark_gray_3'],
            image=self.expand_icon,
            height=40,
        )
        expand_button.place(relx=0.87, rely=0.5, anchor='center')

        self.device_variable.trace_add(
            'write', lambda name, index, mode, var=self.device_variable: \
            self.__value_changed()
        )

    def __value_changed(self):
        self.controller.enable_save()

    def get_value(self):
        return int(self.device_variable.get())

    def set_value(self, new_value):
        self.device_variable.set(new_value)


# ===================================================
# Update Interval Input
#
# Input type: float
# Measurement: seconds(s)
# Bounds: [1.0, 43200.0]
# ===================================================

class IntervalInputFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_2'],
            corner_radius=0,
        )

        self.is_valid = True
        self.description = '\nChange the interval of time (in seconds) it takes for the screen brightness to update. ' + \
            'Accepted values range from 1 second to 43,200 seconds.'
        self.error_text = 'Time interval should only be from 1 to 43,200 seconds.'

        self.bind('<Enter>', self.set_description)
        self.bind('<Leave>', self.remove_description)

        # Setup grid layout
        self.columnconfigure(0, weight=1, uniform='col')
        self.columnconfigure(1, weight=1, uniform='col')
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        vcmd = (self.register(self.__type_validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        interval_label = tk.Label(
            self,
            font=('Bahnschrift Light', 10),
            text='Interval: ',
            justify='left',

            bg=COLOR['dark_gray_2'],
            fg=COLOR['white'],
        )
        interval_label.grid(column=0, row=0, sticky='w')

        self.interval_variable = tk.StringVar()
        self.interval_input = ctk.CTkEntry(
            self,
            text_font=('Bahnschrift Light', 10),
            justify='left',

            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            text_color=COLOR['white'],

            height=40,
            corner_radius=10,
        )
        self.interval_input.entry.configure(
            textvariable=self.interval_variable,
            validate='key',
            validatecommand=vcmd,
        )
        self.interval_variable.set(30)
        self.interval_input.grid(column=1, row=0, sticky='we')

        self.interval_variable.trace_add(
            'write', lambda name, index, mode, var=self.interval_variable: \
            self.__value_changed()
        )

    def __value_changed(self):
        self.controller.enable_save()

    def get_value(self):
        return int(self.interval_variable.get() or 1)

    def set_value(self, new_value):
        self.interval_variable.set(new_value)

    def __type_validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed == '':
            return True
        try:
            if float(value_if_allowed) >= 0:
                return True
            else:
                return False
        except ValueError:
            return False


    def get_save_validity(self):
        if 1 <= self.get_value() <= 43200:
            self.is_valid = True
            return True
        else:
            self.is_valid = False
            return False

    def set_invalid_color(self, is_valid):
        if is_valid:
            self.interval_input.configure(
                fg_color=COLOR['dark_gray_3']
            )
        else:
            self.interval_input.configure(
                fg_color=COLOR['error']
            )

    def set_description(self, event):
        self.controller.set_setting_description(self.is_valid, self.description, self.error_text)

    def remove_description(self, event):
        self.controller.remove_setting_description()



# ===================================================
# Percent Threshold Input
#
# Input type: float
# Measurement: percent
# Bounds: [0.0, 100.0]
# ===================================================

class ThresholdInputFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_2'],
            corner_radius=0,
        )

        self.is_valid = True
        self.description = '\nChange the threshold amount (in percent) needed for the screen to change its brightness. ' + \
            'Accepted values range from 0% to 100%.'
        self.error_text = 'Threshold cannot be above 100%.'

        self.bind('<Enter>', self.set_description)
        self.bind('<Leave>', self.remove_description)

        # Setup grid layout
        self.columnconfigure(0, weight=1, uniform='col')
        self.columnconfigure(1, weight=1, uniform='col')
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        vcmd = (self.register(self.__type_validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        threshold_label = tk.Label(
            self,
            font=('Bahnschrift Light', 10),
            text='Threshold %: ',
            justify='left',

            bg=COLOR['dark_gray_2'],
            fg=COLOR['white'],
        )
        threshold_label.grid(column=0, row=0, sticky='w')

        self.threshold_variable = tk.StringVar()
        self.threshold_input = ctk.CTkEntry(
            self,
            text_font=('Bahnschrift Light', 10),
            justify='left',

            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            text_color=COLOR['white'],

            height=40,
            corner_radius=10,
        )
        self.threshold_input.entry.configure(
            textvariable=self.threshold_variable,
            validate='key',
            validatecommand=vcmd,
        )
        self.threshold_variable.set(0)
        self.threshold_input.grid(column=1, row=0, sticky='we')

        self.threshold_variable.trace_add(
            'write', lambda name, index, mode, var=self.threshold_variable: \
            self.__value_changed()
        )

    def __value_changed(self):
        self.controller.enable_save()

    def get_value(self):
        return float(self.threshold_variable.get() or 0)

    def set_value(self, new_value):
        self.threshold_variable.set(new_value)

    def __type_validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed == '':
            return True
        try:
            if float(value_if_allowed) >= 0:
                return True
            else:
                return False
        except ValueError:
            return False


    def get_save_validity(self):
        if 0 <= self.get_value() <= 100:
            self.is_valid = True
            return True
        else:
            self.is_valid = False
            return False

    def set_invalid_color(self, is_valid):
        if is_valid:
            self.threshold_input.configure(
                fg_color=COLOR['dark_gray_3']
            )
        else:
            self.threshold_input.configure(
                fg_color=COLOR['error']
            )

    def set_description(self, event):
        self.controller.set_setting_description(self.is_valid, self.description, self.error_text)

    def remove_description(self, event):
        self.controller.remove_setting_description()


# ===================================================
# Sampling rate (Number of samples per brightness update) Input
#
# Input type: int
# Measurement: counting number
# Bounds: [1, 10]
# ===================================================

class SamplesInputFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_2'],
            corner_radius=0,
        )

        self.is_valid = True
        self.description = '\nChange the number of webcam samples used when updating the screen brightness. ' + \
            'Accepted values range from 1 to 10. Lower values will provide better performance.'
        self.error_text = 'Sampling rate should only be from 1 to 10.'

        self.bind('<Enter>', self.set_description)
        self.bind('<Leave>', self.remove_description)

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        vcmd = (self.register(self.__type_validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        samples_label = tk.Label(
            self,
            font=('Bahnschrift Light', 10),
            text='Sample Rate:',
            justify='left',

            bg=COLOR['dark_gray_2'],
            fg=COLOR['white'],
        )
        samples_label.grid(column=0, row=0, sticky='w')

        self.samples_variable = tk.StringVar()
        self.samples_input = ctk.CTkEntry(
            self,
            text_font=('Bahnschrift Light', 10),
            justify='left',

            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            text_color=COLOR['white'],

            height=40,
            corner_radius=10,
        )
        self.samples_input.entry.configure(
            textvariable=self.samples_variable,
            validate='key',
            validatecommand=vcmd,
        )
        self.samples_variable.set(1)
        self.samples_input.grid(column=1, row=0, sticky='we')

        self.samples_variable.trace_add(
            'write', lambda name, index, mode, var=self.samples_variable: \
            self.__value_changed()
        )

    def __value_changed(self):
        self.controller.enable_save()

    def get_value(self):
        return int(self.samples_variable.get() or 1)

    def set_value(self, new_value):
        self.samples_variable.set(new_value)

    def __type_validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed == '':
            return True
        try:
            if int(value_if_allowed) >= 0:
                return True
            else:
                return False
        except ValueError:
            return False


    def get_save_validity(self):
        if 0 <= self.get_value() <= 10:
            self.is_valid = True
            return True
        else:
            self.is_valid = False
            return False

    def set_invalid_color(self, is_valid):
        if is_valid:
            self.samples_input.configure(
                fg_color=COLOR['dark_gray_3']
            )
        else:
            self.samples_input.configure(
                fg_color=COLOR['error']
            )

    def set_description(self, event):
        self.controller.set_setting_description(self.is_valid, self.description, self.error_text)

    def remove_description(self, event):
        self.controller.remove_setting_description()


class PreviewCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_2'],
            corner_radius=0,
        )

        self.description = '\nEnables the webcam preview on the home screen.\n' + \
            'The preview will display the webcam image used for calculating brightness.'
        self.warning = 'Warning: This is very resource-heavy.'

        self.bind('<Enter>', self.set_description)
        self.bind('<Leave>', self.remove_description)

        # Setup grid layout
        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()


    def __init_widgets(self):
        self.preview_variable = tk.BooleanVar()
        preview_checkbox = ctk.CTkCheckBox(
            self,
            variable=self.preview_variable,
            text_font=('Bahnschrift Light', 10),
            text='',

            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['light_gray_1'],
            hover_color=COLOR['hover'],
            text_color=COLOR['white'],
            border_color=COLOR['dark_gray_5'],

            border_width=3,
            onvalue=True,

            offvalue=False,
            corner_radius=7
        )
        self.preview_variable.set(False)
        preview_checkbox.grid(column=0, row=0, padx=(0, 0))

        preview_label = tk.Label(
            self,
            font=('Bahnschrift Light', 10),
            text='Enable Preview',
            justify='left',
            anchor='w',

            bg=COLOR['dark_gray_2'],
            fg=COLOR['white'],
        )
        preview_label.grid(column=1, row=0, sticky='we')

        self.preview_variable.trace_add(
            'write', lambda name, index, mode, var=self.preview_variable: \
            self.__value_changed()
        )

    def __value_changed(self):
        self.controller.enable_save()

    def get_value(self):
        return self.preview_variable.get()

    def set_value(self, new_value):
        self.preview_variable.set(new_value)

    def set_description(self, event):
        self.controller.set_setting_description(False, self.description, self.warning)

    def remove_description(self, event):
        self.controller.remove_setting_description()


class StartUpCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_2'],
            corner_radius=0,
        )

        self.description = '\nEnabling this will automatically\n open this application on start-up.'
        self.warning = '\nWarning: This does not work yet.'

        self.bind('<Enter>', self.set_description)
        self.bind('<Leave>', self.remove_description)

        # Setup grid layout
        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()


    def __init_widgets(self):
        self.startup_variable = tk.BooleanVar()
        startup_checkbox = ctk.CTkCheckBox(
            self,
            variable=self.startup_variable,
            text_font=('Bahnschrift Light', 10),
            text='',

            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['light_gray_1'],
            hover_color=COLOR['hover'],
            text_color=COLOR['white'],
            border_color=COLOR['dark_gray_5'],

            border_width=3,
            onvalue=True,

            offvalue=False,
            corner_radius=7,
        )
        self.startup_variable.set(False)
        startup_checkbox.grid(column=0, row=0, padx=(0, 0))

        startup_label = tk.Label(
            self,
            font=('Bahnschrift Light', 10),
            text='Open on Start',
            justify='left',
            anchor='w',

            bg=COLOR['dark_gray_2'],
            fg=COLOR['white'],
        )
        startup_label.grid(column=1, row=0, sticky='we')

        self.startup_variable.trace_add(
            'write', lambda name, index, mode, var=self.startup_variable: \
            self.__value_changed()
        )

    def __value_changed(self):
        self.controller.enable_save()

    def get_value(self):
        return self.startup_variable.get()

    def set_value(self, new_value):
        self.startup_variable.set(new_value)

    def set_description(self, event):
        self.controller.set_setting_description(False, self.description, self.warning)

    def remove_description(self, event):
        self.controller.remove_setting_description()