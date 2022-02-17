#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from tkinter import *
from tkinter import messagebox

webcamvalue = 100  # webcam brightness value
screenvalue = 100  # screen brightness value
scaling_value = 1.25


def round_rectangle(
    canvas,
    x1,
    y1,
    x2,
    y2,
    radius=25,
    **kwargs
    ):
    points = [
        x1 + radius, y1,
        x1 + radius, y1,
        x2 - radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1 + radius,
        x1, y1
        ]

    return canvas.create_polygon(points, smooth=True, **kwargs)


def changeOnHover(button, colorOnHover, colorOnLeave):
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind('<Enter>', func=lambda e: \
                button.config(background=colorOnHover))

    # background color on leving widget
    button.bind('<Leave>', func=lambda e: \
                button.config(background=colorOnLeave))

########################
######## setup #########
########################


lightGrey = '#3A3A3A'
grey = '#262626'
black = '#000000'
brightGrey = '#595959'
fgColor = '#5B9BD5'
errColor = '#FF5050'


########################
######## header ########
########################

class MainFrame(Frame):
    def __init__(self, master):
        super().__init__(
            master,
            bg=grey,
        )
        self.master = master

        header = Frame(
            self,
            highlightbackground=fgColor,
            bg=grey,
            highlightcolor=fgColor,
            highlightthickness=1,
            width=880,
            height=55,
            bd=0,
            )
        header.pack_propagate(0)
        header.pack()

        title = Frame(
            header,
            width=80,
            height=30,
            bg=grey
            )
        title.pack_propagate(0)
        Label(
            title,
            bg=grey,
            fg='white',
            text='WAABA:',
            font=('Bahnschrift Bold', 14)
            ).pack()
        title.pack(side=LEFT, padx=(15, 0))

        subtitle = Frame(
            header,
            width=600,
            height=20,
            bg=grey
            )
        subtitle.pack_propagate(0)
        Label(
            subtitle,
            text='A Webcam-based Adjustable Adaptive Brightness Application',
            font=('Bahnschrift Light', 10),
            bg=grey,
            fg='white',
            justify='left',
            ).pack(side='left')
        subtitle.pack(side=LEFT, padx=0, pady=(6, 0))

        settings = Frame(
            header,
            width=100,
            height=30,
            bg=black,
            highlightbackground=fgColor,
            highlightthickness=0,
            cursor='hand2',
            )
        settings.pack_propagate(0)
        settingsButton = Button(
            settings,
            font=('Bahnschrift SemiBold', 10),
            bg=lightGrey,
            fg='#FFFFFF',
            text='SETTINGS',
            padx=20,
            pady=10,
            command=self.open_settings,
            activebackground=fgColor,
            activeforeground='black',
            borderwidth=0,
            )
        settingsButton.pack(fill=X, side=LEFT)
        settings.place(x=759, y=12)
        changeOnHover(settingsButton, '#364A5B', lightGrey)

        ########################
        ######## middle ########
        ########################

        middle = Canvas(
            self,
            highlightbackground=fgColor,
            bg=grey,
            highlightcolor=fgColor,
            highlightthickness=1,
            width=880,
            height=385,
            bd=0,
            )
        middle.pack(side=TOP)

        webcamF1 = Frame(middle, width=187, height=44, bg=lightGrey)
        webcamF1.pack_propagate(0)
        Label(
            webcamF1,
            text='Current Webcam\nBrightness',
            font='{Bahnschrift Light} 12',
            bg=lightGrey,
            fg='#FFFFFF'
            ).pack()
        webcamF1.place(x=40, y=49)
        webcamB1 = round_rectangle(
            middle,
            35,
            40,
            230,
            102,
            radius=20,
            fill=lightGrey,
            outline='#595959',
            )

        webcamF2 = Frame(middle, width=187, height=87, bg=lightGrey)
        webcamF2.pack_propagate(0)
        Label(
            webcamF2,
            text='{}%'.format(webcamvalue),
            font='{Bahnschrift Light} 50',
            bg=lightGrey,
            fg='#FFFFFF',
            width=4,
            justify='center',
            ).pack()
        webcamF2.place(x=40, y=185)
        webcamB2 = round_rectangle(
            middle,
            35,
            120,
            230,
            340,
            radius=20,
            fill=lightGrey,
            outline='#595959',
            )

        screenF1 = Frame(middle, width=188, height=44, bg=lightGrey)
        screenF1.pack_propagate(0)
        Label(
            screenF1,
            text='Calculated Screen\nBrightness',
            font='{Bahnschrift Light} 12',
            bg=lightGrey,
            fg='#FFFFFF'
            ).pack()
        screenF1.place(x=252, y=49)
        screenB1 = round_rectangle(
            middle,
            248,
            40,
            443,
            102,
            radius=20,
            fill=lightGrey,
            outline='#595959',
            )

        screenF2 = Frame(middle, width=187, height=87, bg=lightGrey)
        screenF2.pack_propagate(0)
        Label(
            screenF2,
            text='{}%'.format(screenvalue),
            font='{Bahnschrift Light} 50',
            bg=lightGrey,
            fg='#FFFFFF',
            width=4,
            justify='center',
            ).pack()
        screenF2.place(x=252, y=185)
        screenbox2 = round_rectangle(
            middle,
            248,
            120,
            443,
            340,
            radius=20,
            fill=lightGrey,
            outline='#595959',
            )

        previewbox = round_rectangle(
            middle,
            461,
            40,
            845,
            340,
            radius=20,
            fill=lightGrey,
            outline='#595959',
            )
        preview = Frame(middle, width=376, height=25, bg=lightGrey)
        preview.pack_propagate(0)
        Label(
            preview,
            text='Webcam Preview',
            font='{Bahnschrift Light} 12',
            bg=lightGrey,
            fg='#FFFFFF'
            ).pack(fill=BOTH)
        preview.place(x=465, y=50)

        webcamFrame = Frame(middle, width=300, height=225, bg=black)
        webcamFrame.place(x=505, y=85)

        ########################
        ######## bottom ########
        ########################

        bottom = Frame(
            self,
            highlightbackground=fgColor,
            bg=grey,
            highlightcolor=fgColor,
            highlightthickness=1,
            width=880,
            height=55,
            bd=0,
            )
        bottom.pack(side=TOP)

    def open_settings(self):
        self.master.open_frame('settings')
