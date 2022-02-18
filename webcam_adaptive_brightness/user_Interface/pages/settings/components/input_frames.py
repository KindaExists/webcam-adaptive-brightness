#!/usr/bin/python
# -*- coding: utf-8 -*-
from email.mime import image
import os

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from user_interface.constants import COLOR

webcam_list = ['0', '1', '2']


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

        # Setup grid layout
        self.columnconfigure(0, weight=1, uniform='col')
        self.columnconfigure(1, weight=1, uniform='col')
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        vcmd = (self.register(self.__validate),
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
        interval_input = ctk.CTkEntry(
            self,
            text_font=('Bahnschrift Light', 10),
            justify='left',

            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            text_color=COLOR['white'],

            height=40,
            corner_radius=10,
        )
        interval_input.entry.configure(
            textvariable=self.interval_variable,
            validate='key',
            validatecommand=vcmd,
        )
        self.interval_variable.set(30)
        interval_input.grid(column=1, row=0, sticky='we')

        self.interval_variable.trace_add(
            'write', lambda name, index, mode, var=self.interval_variable: \
            self.__value_changed()
        )

    def __value_changed(self):
        self.controller.enable_save()

    def get_value(self):
        return self.interval_variable.get() or 1

    def set_value(self, new_value):
        self.interval_variable.set(new_value)

    def __validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed == '':
            return True
        try:
            if int(value_if_allowed) < 100000:
                return True
            else:
                return False
        except ValueError:
            return False




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

        # Setup grid layout
        self.columnconfigure(0, weight=1, uniform='col')
        self.columnconfigure(1, weight=1, uniform='col')
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        vcmd = (self.register(self.__validate),
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
        threshold_input = ctk.CTkEntry(
            self,
            text_font=('Bahnschrift Light', 10),
            justify='left',

            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            text_color=COLOR['white'],

            height=40,
            corner_radius=10,
        )
        threshold_input.entry.configure(
            textvariable=self.threshold_variable,
            validate='key',
            validatecommand=vcmd,
        )
        self.threshold_variable.set(0)
        threshold_input.grid(column=1, row=0, sticky='we')

        self.threshold_variable.trace_add(
            'write', lambda name, index, mode, var=self.threshold_variable: \
            self.__value_changed()
        )

    def __value_changed(self):
        self.controller.enable_save()

    def get_value(self):
        return self.threshold_variable.get() or 0

    def set_value(self, new_value):
        self.threshold_variable.set(new_value)

    def __validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed == '':
            return True
        try:
            if int(value_if_allowed) in range(0, 101):
                return True
            else:
                return False
        except ValueError:
            return False

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

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        vcmd = (self.register(self.__validate),
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
        samples_input = ctk.CTkEntry(
            self,
            text_font=('Bahnschrift Light', 10),
            justify='left',

            bg_color=COLOR['dark_gray_2'],
            fg_color=COLOR['dark_gray_3'],
            text_color=COLOR['white'],

            height=40,
            corner_radius=10,
        )
        samples_input.entry.configure(
            textvariable=self.samples_variable,
            validate='key',
            validatecommand=vcmd,
        )
        self.samples_variable.set(1)
        samples_input.grid(column=1, row=0, sticky='we')

        self.samples_variable.trace_add(
            'write', lambda name, index, mode, var=self.samples_variable: \
            self.__value_changed()
        )

    def __value_changed(self):
        self.controller.enable_save()

    def get_value(self):
        return self.samples_variable.get() or 1

    def set_value(self, new_value):
        self.samples_variable.set(new_value)

    def __validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed == '':
            return True
        try:
            if int(value_if_allowed) < 10:
                return True
            else:
                return False
        except ValueError:
            return False



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

        # Setup grid layout
        self.columnconfigure(0, weight=1, uniform='col')
        self.rowconfigure(0, weight=1, uniform='col')
        self.grid_propagate(False)

        self.__init_widgets()


    def __init_widgets(self):
        self.startup_variable = tk.BooleanVar()
        startup_checkbox = ctk.CTkCheckBox(
            self,
            variable=self.startup_variable,
            text_font=('Bahnschrift Light', 10),
            text='Open on Start',

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
        startup_checkbox.grid(column=0, row=0, sticky='we')

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

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()


    def __init_widgets(self):
        self.preview_variable = tk.BooleanVar()
        preview_checkbox = ctk.CTkCheckBox(
            self,
            variable=self.preview_variable,
            text_font=('Bahnschrift Light', 10),
            text='Enable Webcam Preview',

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
        self.preview_variable.set(False)
        preview_checkbox.grid(column=0, row=0, sticky='we')

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

    def get_value(self):
        return self.device_variable.get()

    def set_value(self, new_value):
        self.device_variable.set(new_value)




"""
class ThresholdInput(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=_GRAY,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__init_widgets()

    def __init_widgets(self):
        threshold_variable = tk.StringVar()
        # Event listner, fires on change of input value
        # threshold_variable.trace_add('write', lambda var, index, mode, threshold_variable=threshold_variable: \
        #                 self.enableSave(threshold_variable))
        #? TODO: Change to ttk for better styling
        threshold_value = tk.Entry(
            self,
            font=('Bahnschrift Light', 10),
            textvariable=threshold_variable,
            justify='center',

            bg=_GRAY,
            fg=_WHITE,
            insertbackground='white',

            width=12,
            bd=0,
            insertborderwidth=1,
        )

        # Inserts Default Value
        #? TODO: Fix defaults for all parts
        threshold_value.insert(0, '1')

        threshold_value.grid(column=0, row=0, sticky='nswe')
"""



"""
class IntervalInputFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=_DARK_GRAY,
            cursor='question_arrow',
            height=40,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        interval_label = tk.Label(
            self,
            font=('Bahnschrift Light', 10),
            text=f'Interval: ',

            bg=_DARK_GRAY,
            fg=_WHITE,
        )
        interval_label.grid(column=0, row=0)

        interval_input = ThresholdInput(self)
        interval_input.grid(column=1, row=0, sticky='ns')


class IntervalInput(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=_GRAY,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__init_widgets()

    def __init_widgets(self):
        interval_variable = tk.StringVar()
        # Event listner, fires on change of input value

        # interval_variable.trace_add('write', lambda var, index, mode, interval_variable=interval_variable: \
        #                 self.enableSave(interval_variable))

        #? TODO: Change to ttk for better styling
        interval_value = tk.Entry(
            self,
            font=('Bahnschrift Light', 10),
            textvariable=interval_variable,
            justify='center',

            bg=_GRAY,
            fg=_WHITE,
            insertbackground='white',

            width=12,
            bd=0,
            insertborderwidth=1,
        )

        # Inserts Default Value
        #? TODO: Fix defaults for all parts
        interval_value.insert(0, '1')

        interval_value.grid(column=0, row=0, sticky='nswe')






class ThresholdInputFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=_DARK_GRAY,
            cursor='question_arrow',
            height=40,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        threshold_label = tk.Label(
            self,
            font=('Bahnschrift Light', 10),
            text=f'Threshold %: ',

            bg=_DARK_GRAY,
            fg=_WHITE,
        )
        threshold_label.grid(column=0, row=0)

        threshold_input = ThresholdInput(self)
        threshold_input.grid(column=1, row=0, sticky='ns')


class ThresholdInput(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=_GRAY,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__init_widgets()

    def __init_widgets(self):
        threshold_variable = tk.StringVar()
        # Event listner, fires on change of input value
        # threshold_variable.trace_add('write', lambda var, index, mode, threshold_variable=threshold_variable: \
        #                 self.enableSave(threshold_variable))
        #? TODO: Change to ttk for better styling
        threshold_value = tk.Entry(
            self,
            font=('Bahnschrift Light', 10),
            textvariable=threshold_variable,
            justify='center',

            bg=_GRAY,
            fg=_WHITE,
            insertbackground='white',

            width=12,
            bd=0,
            insertborderwidth=1,
        )

        # Inserts Default Value
        #? TODO: Fix defaults for all parts
        threshold_value.insert(0, '1')

        threshold_value.grid(column=0, row=0, sticky='nswe')






class SamplesInputFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=_DARK_GRAY,
            cursor='question_arrow',
            height=40,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        sample_label = tk.Label(
            self,
            font=('Bahnschrift Light', 10),
            text=f'Samples: ',

            bg=_DARK_GRAY,
            fg=_WHITE,
        )
        sample_label.grid(column=0, row=0)

        sample_input = SampleInput(self)
        sample_input.grid(column=1, row=0, sticky='ns')


class SampleInput(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=_DARK_GRAY,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__init_widgets()

    def __init_widgets(self):
        sample_variable = tk.StringVar()
        # Event listner, fires on change of input value
        # sample_variable.trace_add('write', lambda var, index, mode, sample_variable=sample_variable: \
        #                 self.enableSave(sample_variable))

        #? TODO: Change to ttk for better styling
        sample_value = tk.Entry(
            self,
            font=('Bahnschrift Light', 10),
            textvariable=sample_variable,
            justify='center',

            bg=_GRAY,
            fg=_WHITE,
            insertbackground='white',

            width=12,
            bd=0,
            insertborderwidth=1,
        )

        # Inserts Default Value
        #? TODO: Fix defaults for all parts
        sample_value.insert(0, '1')

        sample_value.grid(column=0, row=0, sticky='nswe')






class DeviceInputFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=_DARK_GRAY,
            cursor='question_arrow',
            height=40,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        device_label = tk.Label(
            self,
            font=('Bahnschrift Light', 10),
            text=f'Webcam: ',

            bg=_DARK_GRAY,
            fg=_WHITE,
        )
        device_label.grid(column=0, row=0)

        device_input = DeviceInput(self)
        device_input.grid(column=1, row=0, sticky='ns')


class DeviceInput(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=_GRAY,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__init_widgets()

    def __init_widgets(self):
        selected_webcam = tk.StringVar()

        ttk.Style().configure('err.TMenubutton', background='#683333',
                              foreground='white', highlightthickness=0,
                              width=12)
        ttk.Style().configure('norm.TMenubutton', background=_GRAY,
                              foreground='white', highlightthickness=0,
                              width=12)

        webcam_value = ttk.OptionMenu(self,
                                     selected_webcam,
                                     webcam_list[0],
                                     style='norm.TMenubutton',
                                     *webcam_list)

        webcam_value.grid(column=0, row=0, sticky='nswe')





class StartUpCheckboxFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=_DARK_GRAY,
            cursor='question_arrow',
            height=40,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        startup_checkbox = PreviewCheckbox(self)
        startup_checkbox.grid(column=0, row=0)

        #? TODO: Fix this part later (Whitespace)
        startup_label = tk.Label(
            self,
            font=('Bahnschrift Light', 10),
            text=f'Enable on Start   ',

            bg=_DARK_GRAY,
            fg=_WHITE,
        )
        startup_label.grid(column=1, row=0)


class StartUpCheckbox(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=_GRAY,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__init_widgets()

    def __init_widgets(self):
        self.on_image = tk.PhotoImage(width=44, height=25)
        self.off_image = tk.PhotoImage(width=44, height=25)
        self.on_image.put(('white', ), to=(20, 0, 42, 23))
        self.off_image.put(('white', ), to=(1, 1, 23, 24))

        startup_variable = tk.BooleanVar()
        startup_variable.set(False)

        #? TODO: This thing
        # startup_variable.trace_add('write', lambda name, index, mode, \
        #             startup_variable=startup_variable: \
        #             self.enableSave(startup_variable))


        startup_checkbox = tk.Checkbutton(
            self,
            image=self.off_image,
            selectimage=self.on_image,
            indicatoron=False,
            onvalue=True,
            offvalue=False,
            variable=startup_variable,
            bd=0,
            selectcolor=fgColor,
            bg='#969696',
            activebackground='#7999B6',
        )

        startup_checkbox.grid(column=0, row=0, sticky='nswe')




class PreviewCheckboxFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=_DARK_GRAY,
            cursor='question_arrow',
            height=40,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        preview_checkbox = PreviewCheckbox(self)
        preview_checkbox.grid(column=0, row=0)

        preview_label = tk.Label(
            self,
            font=('Bahnschrift Light', 10),
            text=f'Webcam Preview',

            bg=_DARK_GRAY,
            fg=_WHITE,
        )
        preview_label.grid(column=1, row=0)


class PreviewCheckbox(tk.Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=_GRAY,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__init_widgets()

    def __init_widgets(self):
        self.on_image = tk.PhotoImage(width=44, height=25)
        self.off_image = tk.PhotoImage(width=44, height=25)
        self.on_image.put(('white', ), to=(20, 0, 42, 23))
        self.off_image.put(('white', ), to=(1, 1, 23, 24))

        preview_variable = tk.BooleanVar()
        preview_variable.set(False)

        #? TODO: This thing
        # preview_variable.trace_add('write', lambda name, index, mode, \
        #             preview_variable=preview_variable: \
        #             self.enableSave(preview_variable))

        preview_checkbox = tk.Checkbutton(
            self,
            image=self.off_image,
            selectimage=self.on_image,
            indicatoron=False,
            onvalue=True,
            offvalue=False,
            variable=preview_variable,
            bd=0,
            selectcolor=fgColor,
            bg='#969696',
            activebackground='#7999B6',
        )

        preview_checkbox.grid(column=0, row=0, sticky='nswe')
"""
