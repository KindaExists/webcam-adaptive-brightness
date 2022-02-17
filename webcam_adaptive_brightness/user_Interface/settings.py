#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def round_rectangle(
    canvas,
    x1,
    y1,
    len,
    wid,
    radius=25,
    **kwargs
    ):
    x2 = x1 + len
    y2 = y1 + wid
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

def changeButtonOnHover(button, colorOnHover, colorOnLeave):
    button.bind('<Enter>', func=lambda e: \
                button.config(background=colorOnHover))
    button.bind('<Leave>', func=lambda e: \
                button.config(background=colorOnLeave))


lightGrey = '#3A3A3A'
grey = '#262626'
black = 'black'
brightGrey = '#595959'
fgColor = '#5B9BD5'
errColor = '#FF5050'

window_width = 880
window_height = 495



########################
######## header ########
########################

class SettingsFrame(Frame):
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

        title = Frame(header, width=80, height=30, bg=grey)
        title.pack_propagate(0)
        Label(
            title,
            bg=grey,
            fg='white',
            text='WAABA:',
            font=('Bahnschrift Bold', 14)
            ).pack()
        title.pack(side=LEFT, padx=(15, 0))

        subtitle = Frame(header, width=600, height=20, bg=grey)
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

        home = Frame(
            header,
            width=100,
            height=30,
            bg=black,
            highlightbackground=fgColor,
            highlightthickness=0,
            cursor='hand2',
            )
        home.pack_propagate(0)
        homeButton = Button(
            home,
            font=('Bahnschrift SemiBold', 10),
            bg=lightGrey,
            fg='white',
            text='HOME',
            padx=35,
            pady=10,
            command=self.open_main,
            activebackground=fgColor,
            activeforeground='black',
            borderwidth=0,
            )
        homeButton.pack(fill=X, side=LEFT)
        home.place(x=759, y=12)
        changeButtonOnHover(homeButton, '#364A5B', lightGrey)

        ######################
        ######## left ########
        ######################

        self.left = Canvas(
            self,
            highlightbackground=fgColor,
            bg=grey,
            highlightcolor=fgColor,
            highlightthickness=1,
            width=340,
            height=440,
            bd=0,
            )
        self.left.pack(side=LEFT)

        graphLabel = Frame(self.left, width=332, height=50, bg=grey)
        graphLabel.pack_propagate(0)
        Label(
            graphLabel,
            text='Adjustable linear curve for\nScreen Brightness',
            font='{Bahnschrift SemiBold} 13',
            bg=grey,
            fg='#FFFFFF'
            ).pack(fill=BOTH)
        graphLabel.place(x=5, y=25)

        self.sliderMinVal = DoubleVar()
        sliderMin = ttk.Scale(
            self.left,
            length=200,
            from_=100,
            to=0,
            orient='vertical',
            command=self.minSliderChanged,
            variable=self.sliderMinVal,
            )
        sliderMin.set(0.0)
        ttk.Style().configure('Vertical.TScale', background=grey)
        sliderMin.place(x=50, y=100)
        minL1 = Frame(self.left, width=26, height=20, bg=grey)
        minL1.pack_propagate(0)
        Label(
            minL1,
            text='100',
            font='{Bahnschrift Light} 10',
            bg=grey,
            fg='#FFFFFF'
            ).pack(side=TOP)
        minL1.place(x=50, y=77)
        maxL1 = Frame(self.left, width=26, height=20, bg=grey)
        maxL1.pack_propagate(0)
        Label(
            maxL1,
            text='0',
            font='{Bahnschrift Light} 10',
            bg=grey,
            fg='#FFFFFF'
            ).pack(side=TOP)
        maxL1.place(x=50, y=303)

        self.sliderMaxVal = DoubleVar()
        sliderMax = ttk.Scale(
            self.left,
            length=200,
            from_=100,
            to=0,
            orient='vertical',
            command=self.maxSliderChanged,
            variable=self.sliderMaxVal,
            )
        sliderMax.set(100.0)
        sliderMax.place(x=285, y=100)
        minL2 = Frame(self.left, width=26, height=20, bg=grey)
        minL2.pack_propagate(0)
        Label(
            minL2,
            text='100',
            font='{Bahnschrift Light} 10',
            bg=grey,
            fg='#FFFFFF'
            ).pack(side=TOP)
        minL2.place(x=285, y=77)
        maxL2 = Frame(self.left, width=26, height=20, bg=grey)
        maxL2.pack_propagate(0)
        Label(
            maxL2,
            text='0',
            font='{Bahnschrift Light} 10',
            bg=grey,
            fg='#FFFFFF'
            ).pack(side=TOP)
        maxL2.place(x=285, y=303)

        yLabel = PhotoImage(file=os.path.dirname(os.path.abspath(__file__))
                            + '/LabelY.png')
        self.left.create_image(40, 200, image=yLabel)
        xLabel = PhotoImage(file=os.path.dirname(os.path.abspath(__file__))
                            + '/LabelX.png')
        self.left.create_image(80, 308, image=xLabel, anchor=NW)

        minBoxLabel = Frame(self.left, width=80, height=38, bg=grey)
        minBoxLabel.pack_propagate(0)
        Label(
            minBoxLabel,
            text='Minimum\nBrightness:',
            font='{Bahnschrift Light} 10',
            justify='left',
            bg=grey,
            fg='#FFFFFF',
            ).pack(side=TOP)
        minBoxLabel.place(x=20, y=350)
        self.minbox = round_rectangle(
            self.left,
            105,
            351,
            50,
            35,
            radius=15,
            fill=lightGrey,
            outline=brightGrey,
            )
        self.minVal = Frame(self.left, width=41, height=20, bg=lightGrey)
        self.minVal.pack_propagate(0)
        self.minValLabel = Label(self.minVal,
                            text='0%',
                            font='{Bahnschrift Light} 10',
                            bg=lightGrey,
                            fg='#FFFFFF')
        self.minValLabel.pack(side=TOP)
        self.minVal.place(x=110, y=359)

        maxBoxLabel = Frame(self.left, width=80, height=38, bg=grey)
        maxBoxLabel.pack_propagate(0)
        Label(
            maxBoxLabel,
            text='Maximum\nBrightness:',
            font='{Bahnschrift Light} 10',
            justify='left',
            bg=grey,
            fg='#FFFFFF',
            ).pack(side=TOP)
        maxBoxLabel.place(x=185, y=350)
        self.maxbox = round_rectangle(
            self.left,
            270,
            351,
            50,
            35,
            radius=15,
            fill=lightGrey,
            outline=brightGrey,
            )
        self.maxVal = Frame(self.left, width=41, height=20, bg=lightGrey)
        self.maxVal.pack_propagate(0)
        self.maxValLabel = Label(self.maxVal,
                            text='100%',
                            font='{Bahnschrift Light} 10',
                            bg=lightGrey,
                            fg='#FFFFFF')
        self.maxValLabel.pack(side=TOP)
        self.maxVal.place(x=275, y=359)

        graphBox = self.left.create_rectangle(
            80, 100, 280, 300,
            fill=lightGrey,
            outline=lightGrey,
            )
        for x in range(100, 280, 20):
            self.left.create_line(
                x, 100,
                x, 300,
                fill=grey,
                width=2,
                )
        for y in range(120, 300, 20):
            self.left.create_line(
                80, y,
                280, y,
                fill=grey,
                width=2,
                )
        self.createLineCurve(self.left, self.get_Minimum_value(), self.get_Maximum_value())

        #######################
        ######## right ########
        #######################

        self.right = Canvas(
            self,
            highlightbackground=fgColor,
            bg=grey,
            highlightcolor=fgColor,
            highlightthickness=1,
            width=540,
            height=440,
            bd=0,
            )
        self.right.pack(side=LEFT)

        settingsLabel = Frame(self.right, width=520, height=30, bg=grey)
        settingsLabel.pack_propagate(0)
        Label(
            settingsLabel,
            text='Settings',
            font='{Bahnschrift SemiBold} 14',
            bg=grey,
            fg='#FFFFFF'
            ).pack(fill=BOTH)
        settingsLabel.place(x=8, y=25)

        self.box1 = round_rectangle(  # webcam device
            self.right,
            142, 80,
            115, 35,
            radius=15,
            fill=lightGrey,
            outline=brightGrey,
            )
        self.box2 = round_rectangle(  # sample count
            self.right,
            400, 80,
            115, 35,
            radius=15,
            fill=lightGrey,
            outline=brightGrey,
            )
        self.box3 = round_rectangle(  # threshold
            self.right,
            142, 140,
            115, 35,
            radius=15,
            fill=lightGrey,
            outline=brightGrey,
            )
        self.box4 = round_rectangle(  # time interval
            self.right,
            400, 140,
            115, 35,
            radius=15,
            fill=lightGrey,
            outline=brightGrey,
            )
        box5 = round_rectangle(  # settings description
            self.right,
            17, 265,
            500, 45,
            radius=17,
            fill=lightGrey,
            )

        wbdevLabel = Frame(self.right, width=125, height=30, bg=grey,
                        cursor='question_arrow')
        wbdevLabel.pack_propagate(0)
        Label(
            wbdevLabel,
            text='Webcam Device:',
            font='{Bahnschrift Light} 10',
            bg=grey,
            fg='#FFFFFF'
            ).pack(side=LEFT)
        wbdevLabel.place(x=17, y=83)
        self.changeSettingDesc(wbdevLabel, 0)

        #! Webcam List Here, CHANGE LATER
        wbdevList = ('-----------', 'Webcam 1', 'Webcam 2', 'Webcam 3')

        self.selectedWebcam = StringVar()
        self.wbdevInput = Frame(self.right, width=110, height=30, bg=lightGrey)
        self.wbdevInput.pack_propagate(0)
        ttk.Style().configure('err.TMenubutton', background='#683333',
                            foreground='white', highlightthickness=0)
        ttk.Style().configure('norm.TMenubutton', background=lightGrey,
                            foreground='white', highlightthickness=0)
        self.wbdevValue = ttk.OptionMenu(self.wbdevInput,
                                    self.selectedWebcam,
                                    wbdevList[0],
                                    style='norm.TMenubutton',
                                    *wbdevList)
        self.wbdevValue.configure(width=110)
        self.wbdevValue.pack(side=LEFT, fill=BOTH)
        self.wbdevInput.place(x=145, y=83)
        self.changeSettingDesc(self.wbdevInput, 0)

        sampleLabel = Frame(self.right, width=125, height=30, bg=grey,
                            cursor='question_arrow')
        sampleLabel.pack_propagate(0)
        Label(sampleLabel, text='Sample Count:', font='{Bahnschrift Light} 10',
            bg=grey, fg='#FFFFFF').pack(side=LEFT)
        sampleLabel.place(x=275, y=83)
        self.changeSettingDesc(sampleLabel, 1)

        self.sampleInput = Frame(self.right, width=110, height=30, bg=lightGrey)
        self.sampleInput.pack_propagate(0)
        sampleVar = StringVar()
        sampleVar.trace('w', lambda name, index, mode, sampleVar=sampleVar: \
                        self.enableSave(sampleVar))
        self.sampleValue = Entry(
            self.sampleInput,
            font='{Bahnschrift Light} 10',
            bg=lightGrey,
            fg='#FFFFFF',
            bd=0,
            insertbackground='white',
            insertborderwidth=1,
            textvariable=sampleVar,
            )
        self.sampleValue.insert(0, '1')
        self.sampleValue.pack(side=LEFT, fill=BOTH, padx=(7, 0))
        self.sampleInput.place(x=403, y=83)
        self.changeSettingDesc(self.sampleInput, 1)

        threshLabel = Frame(self.right, width=125, height=30, bg=grey,
                            cursor='question_arrow')
        threshLabel.pack_propagate(0)
        Label(threshLabel, text='Threshold %:', font='{Bahnschrift Light} 10',
            bg=grey, fg='#FFFFFF').pack(side=LEFT)
        threshLabel.place(x=17, y=143)
        self.changeSettingDesc(threshLabel, 2)

        self.threshInput = Frame(self.right, width=110, height=30, bg=lightGrey)
        self.threshInput.pack_propagate(0)
        threshVar = StringVar()
        threshVar.trace('w', lambda name, index, mode, threshVar=threshVar: \
                        self.enableSave(threshVar))
        self.threshValue = Entry(
            self.threshInput,
            font='{Bahnschrift Light} 10',
            bg=lightGrey,
            fg='#FFFFFF',
            bd=0,
            insertbackground='white',
            insertborderwidth=1,
            textvariable=threshVar,
            )
        self.threshValue.insert(0, '1')
        self.threshValue.pack(side=LEFT, fill=BOTH, padx=(7, 0))
        self.threshInput.place(x=145, y=143)
        self.changeSettingDesc(self.threshInput, 2)

        intvLabel = Frame(self.right, width=125, height=30, bg=grey,
                        cursor='question_arrow')
        intvLabel.pack_propagate(0)
        Label(
            intvLabel,
            text='Interval (sec):',
            font='{Bahnschrift Light} 10',
            bg=grey,
            fg='#FFFFFF'
            ).pack(side=LEFT)
        intvLabel.place(x=275, y=143)
        self.changeSettingDesc(intvLabel, 3)

        self.intvInput = Frame(self.right, width=110, height=30, bg=lightGrey)
        self.intvInput.pack_propagate(0)
        intVar = StringVar()
        intVar.trace('w', lambda name, index, mode, intVar=intVar: \
                    self.enableSave(intVar))
        self.intvValue = Entry(
            self.intvInput,
            font='{Bahnschrift Light} 10',
            bg=lightGrey,
            fg='#FFFFFF',
            bd=0,
            insertbackground='white',
            insertborderwidth=1,
            textvariable=intVar,
            )
        self.intvValue.insert(0, '1')
        self.intvValue.pack(side=LEFT, fill=BOTH, padx=(7, 0))
        self.intvInput.place(x=403, y=143)
        self.changeSettingDesc(self.intvInput, 3)

        ###checkboxes###

        on_image = PhotoImage(width=44, height=25)
        off_image = PhotoImage(width=44, height=25)
        on_image.put(('white', ), to=(20, 0, 42, 23))
        off_image.put(('white', ), to=(1, 1, 23, 24))

        self.enableStartupVar = BooleanVar()
        self.disablewcpvVar = BooleanVar()

        self.enableStartupVar.trace('w', lambda name, index, mode, \
                            enableStartupVar=self.enableStartupVar: \
                            self.enableSave(self.enableStartupVar))
        enStartUpBox = Checkbutton(
            self.right,
            image=off_image,
            selectimage=on_image,
            indicatoron=False,
            onvalue=True,
            offvalue=False,
            variable=self.enableStartupVar,
            bd=0,
            selectcolor=fgColor,
            bg='#969696',
            activebackground='#7999B6',
            )
        enStartUpBox.place(x=17, y=204)
        enableStartup = Frame(self.right, width=190, height=30, bg=grey,
                            cursor='question_arrow')
        enableStartup.pack_propagate(0)
        Label(
            enableStartup,
            text='Enable program on start-up',
            font='{Bahnschrift Light} 10',
            bg=grey,
            fg='#FFFFFF'
            ).pack(side=LEFT, padx=(3, 0))
        enableStartup.place(x=67, y=203)
        self.changeSettingDesc(enStartUpBox, 4)
        self.changeSettingDesc(enableStartup, 4)

        self.disablewcpvVar.trace('w', lambda name, index, mode, \
                            disablewcpvVar=self.disablewcpvVar: \
                            self.enableSave(self.disablewcpvVar))
        disablewcBox = Checkbutton(
            self.right,
            image=off_image,
            selectimage=on_image,
            indicatoron=False,
            onvalue=True,
            offvalue=False,
            variable=self.disablewcpvVar,
            bd=0,
            selectcolor=fgColor,
            bg='#969696',
            activebackground='#7999B6',
            )
        disablewcBox.place(x=275, y=204)
        disablewcpv = Frame(self.right, width=190, height=30, bg=grey,
                            cursor='question_arrow')
        disablewcpv.pack_propagate(0)
        Label(
            disablewcpv,
            text='Disable webcam preview',
            font='{Bahnschrift Light} 10',
            bg=grey,
            fg='#FFFFFF'
            ).pack(side=LEFT, padx=(3, 0))
        disablewcpv.place(x=325, y=203)
        self.changeSettingDesc(disablewcBox, 5)
        self.changeSettingDesc(disablewcpv, 5)

        settingDesc = Frame(self.right, width=493, height=24, bg=lightGrey)
        settingDesc.pack_propagate(0)
        self.desc = Label(settingDesc,
                    text='Setting Description: (appears on mouse hover)',
                    font='{Bahnschrift Light} 10',
                    bg=lightGrey,
                    fg='#FFFFFF')
        self.desc.pack(side=TOP, padx=(3, 0), fill=BOTH)
        settingDesc.place(x=20, y=276)

        saveSettings = Frame(
            self.right,
            width=155,
            height=50,
            bg=black,
            highlightbackground=fgColor,
            highlightthickness=0,
            cursor='hand2',
            )
        saveSettings.pack_propagate(0)
        self.saveButton = Button(
            saveSettings,
            font=('Bahnschrift SemiBold', 11),
            bg=lightGrey,
            fg='white',
            text='APPLY CHANGES',
            padx=15,
            pady=12,
            command=self.validateSettings,
            activebackground=fgColor,
            activeforeground='black',
            borderwidth=0,
            state=DISABLED,
            )
        self.saveButton.pack(side=TOP, fill='x')
        saveSettings.place(x=17, y=343)
        changeButtonOnHover(self.saveButton, '#364A5B', lightGrey)

        statusFrame = Frame(self.right, width=330, height=50, bg=grey)
        statusFrame.pack_propagate(0)
        self.status = Label(
            statusFrame,
            text='',
            font='{Bahnschrift SemiBold} 9',
            bg=grey,
            fg='#FFFFFF',
            justify='left',
            )
        self.status.pack(side=LEFT, fill=BOTH)
        statusFrame.place(x=185, y=343)



    def changeSettingDesc(self, frame, setting):
        descList = [
            'Webcam Device: (Insert Description Here)',
            'Sample Count: (Insert Description Here)',
            'Threshold: (Insert Description Here)',
            'Time Interval: (Insert Description Here)',
            'Enables the application the next time you start up the computer',
            'Disables webcam preview on the home page. May improve PC performace'
            ]
        frame.bind('<Enter>', func=lambda e: \
                self.desc.config(text=descList[setting]
                ))
        frame.bind('<Leave>', func=lambda e: \
                self.desc.config(text='Setting Description: (appears on mouse hover)'
                ))


    def validateSettings(self):
        current = {
            'MinB': float(self.get_Minimum_value()),
            'MaxB': float(self.get_Maximum_value()),
            'Webcam': self.selectedWebcam.get(),
            'Sample': self.sampleValue.get(),
            'Thresh': self.threshValue.get(),
            'TimeInt': self.intvValue.get(),
            'StartUp': self.enableStartupVar.get(),
            'DisWebcam': self.disablewcpvVar.get(),
            }
        isValid = {
            'MinB': False,
            'MaxB': False,
            'Webcam': False,
            'Sample': False,
            'Thresh': False,
            'TimeInt': False,
            }
        invalidInputs = []

        BrightnessError = ''
        if current['MinB'] <= current['MaxB']:
            isValid['MinB'] = True
            isValid['MaxB'] = True
        else:
            BrightnessError = \
                'Error: Min. Brightness must be less than Max. Brightness'

        if current['Webcam'] != '-----------':
            isValid['Webcam'] = True
        else:
            invalidInputs.append('Webcam Device')

        try:
            current['Thresh'] = float(current['Thresh'])
            if 0 <= current['Thresh'] <= 100:
                isValid['Thresh'] = True
            else:
                invalidInputs.append('Threshold')
        except:
            invalidInputs.append('Threshold')

        try:
            current['TimeInt'] = float(current['TimeInt'])
            if 1 <= current['TimeInt'] <= 43200:
                isValid['TimeInt'] = True
            else:
                invalidInputs.append('Interval')
        except:
            invalidInputs.append('Interval')

        if current['Sample'].isnumeric():
            current['Sample'] = int(current['Sample'])
            try:
                int(current['TimeInt'])
                if 1 <= current['Sample'] <= int(current['TimeInt']):
                    isValid['Sample'] = True
                else:
                    invalidInputs.append('Sample Count')
            except:
                invalidInputs.append('Sample Count')
        else:
            invalidInputs.append('Sample Count')

        self.changeBoxColors(isValid)

        if all(isValid.values()):
            self.status.config(text='Changes saved successfully!',
                        foreground=fgColor)
            self.printSettings()
            self.disableSave()
        else:
            line1 = BrightnessError
            (line2, s, err) = ('', '', '')
            if len(invalidInputs) > 0:
                if len(invalidInputs) > 1:
                    s = 's'
                if line1 != '':
                    line1 += '\n'
                if len(invalidInputs) > 2:
                    invalidInputs.insert(3, '\n')
                for i in invalidInputs:
                    if i != '\n':
                        err += i + ', '
                    else:
                        err += i + '            '
                if err[-2:] == ', ':
                    err = err[:-2]
                else:
                    err = err[:-15]
                    err += i + '           '
                line2 = 'Error: Invalid {} Input{}'.format(err, s)
            self.status.config(text=line1 + line2, foreground=errColor)


    def changeBoxColors(self, isValid):
        if isValid['MinB']:
            self.left.itemconfig(self.minbox, fill=lightGrey, outline=brightGrey)
            self.minValLabel.config(bg=lightGrey)
            self.minVal.config(bg=lightGrey)
        else:
            self.left.itemconfig(self.minbox, fill='#683333', outline=errColor)
            self.minValLabel.config(bg='#683333')
            self.minVal.config(bg='#683333')

        if isValid['MaxB']:
            self.left.itemconfig(self.maxbox, fill=lightGrey, outline=brightGrey)
            self.maxValLabel.config(bg=lightGrey)
            self.maxVal.config(bg=lightGrey)
        else:
            self.left.itemconfig(self.maxbox, fill='#683333', outline=errColor)
            self.maxValLabel.config(bg='#683333')
            self.maxVal.config(bg='#683333')

        if isValid['Webcam']:
            self.right.itemconfig(self.box1, fill=lightGrey, outline=brightGrey)
            self.wbdevInput.config(bg=lightGrey)
            self.wbdevValue.config(style='norm.TMenubutton')
        else:
            self.right.itemconfig(self.box1, fill='#683333', outline=errColor)
            self.wbdevInput.config(bg='#683333')
            self.wbdevValue.config(style='err.TMenubutton')

        if isValid['Sample']:
            self.right.itemconfig(self.box2, fill=lightGrey, outline=brightGrey)
            self.sampleInput.config(bg=lightGrey)
            self.sampleValue.config(bg=lightGrey)
        else:
            self.right.itemconfig(self.box2, fill='#683333', outline=errColor)
            self.sampleInput.config(bg='#683333')
            self.sampleValue.config(bg='#683333')

        if isValid['Thresh']:
            self.right.itemconfig(self.box3, fill=lightGrey, outline=brightGrey)
            self.threshInput.config(bg=lightGrey)
            self.threshValue.config(bg=lightGrey)
        else:
            self.right.itemconfig(self.box3, fill='#683333', outline=errColor)
            self.threshInput.config(bg='#683333')
            self.threshValue.config(bg='#683333')

        if isValid['TimeInt']:
            self.right.itemconfig(self.box4, fill=lightGrey, outline=brightGrey)
            self.intvInput.config(bg=lightGrey)
            self.intvValue.config(bg=lightGrey)
        else:
            self.right.itemconfig(self.box4, fill='#683333', outline=errColor)
            self.intvInput.config(bg='#683333')
            self.intvValue.config(bg='#683333')


    def printSettings(self):
        print ('Minimum Brightness:', self.get_Minimum_value() + '%')
        print ('Maximum Brightness:', self.get_Maximum_value() + '%')
        print ('Webcam Device:', self.selectedWebcam.get())
        print ('Sample Count:', self.sampleValue.get())
        print ('Threshold:', self.threshValue.get())
        print ('Time Interval:', self.intvValue.get())
        print ('Enable on Start-Up?', self.enableStartupVar.get())
        print ('Disable Webcam Preview?', self.disablewcpvVar.get())

    def minSliderChanged(self, event):
        self.minValLabel.configure(text=self.get_Minimum_value() + '%')
        self.createLineCurve(self.left, self.get_Minimum_value(), self.get_Maximum_value())
        self.enableSave('x')

    def maxSliderChanged(self, event):
        self.maxValLabel.configure(text=self.get_Maximum_value() + '%')
        self.createLineCurve(self.left, self.get_Minimum_value(), self.get_Maximum_value())
        self.enableSave('x')

    def get_Minimum_value(self):
        return '{:.0f}'.format(self.sliderMinVal.get())

    def get_Maximum_value(self):
        return '{:.0f}'.format(self.sliderMaxVal.get())


    def createLineCurve(self, canvas, minSlider, maxSlider):
        y0 = 100 + (100 - int(minSlider)) / 100 * 200
        y1 = 100 + (100 - int(maxSlider)) / 100 * 200
        if y0 < y1:
            color = errColor
        elif y0 == y1:
            color = '#FFC001'
        else:
            color = fgColor

        # FFC001

        canvas.delete('line')
        return canvas.create_line(
            80,
            y0,
            280,
            y1,
            fill=color,
            width=2,
            tags='line',
            )


    def enableSave(self, event):
        self.saveButton['state'] = NORMAL

    def disableSave(self):
        self.saveButton['state'] = DISABLED

    def open_main(self):
        self.master.open_frame('main')

