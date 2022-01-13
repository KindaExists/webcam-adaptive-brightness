from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

def round_rectangle(canvas,x1, y1, len, wid, radius=25, **kwargs):
    x2=x1+len
    y2=y1+wid
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)
def openHome():
   messagebox.showinfo("home", "just imagine ur in d home")
def changeButtonOnHover(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))
def changeSettingDesc(frame, setting):
    descList=[
        "Webcam Device: (Insert Description Here)",
        "Sample Count: (Insert Description Here)",
        "Threshold: (Insert Description Here)",
        "Time Interval: (Insert Description Here)",
        "Enables the application the next time you start up the computer",
        "Disables webcam preview on the home page. May improve PC performace",
    ]
    frame.bind("<Enter>", func=lambda e: desc.config(text=descList[setting]))
    frame.bind("<Leave>", func=lambda e: desc.config(text="Setting Description: (appears on mouse hover)"))
def validateSettings():
    current={
        "MinB": float(get_Minimum_value()),
        "MaxB": float(get_Maximum_value()),
        "Webcam": selectedWebcam.get(),
        "Sample": sampleValue.get(),
        "Thresh": threshValue.get(),
        "TimeInt": intvValue.get(),
        "StartUp": enableStartupVar.get(),
        "DisWebcam": disablewcpvVar.get()
    }
    isValid={"MinB":False,"MaxB":False,"Webcam":False,"Sample":False,"Thresh":False,"TimeInt":False}
    invalidInputs=[]

    BrightnessError=""
    if (current["MinB"]<=current["MaxB"]):
        isValid["MinB"] = True
        isValid["MaxB"] = True
    else: BrightnessError="Error: Min. Brightness must be less than Max. Brightness"

    if current["Webcam"] != '-----------':
        isValid["Webcam"] = True
    else: invalidInputs.append("Webcam Device")

    try:
        current["Thresh"]=float(current["Thresh"])
        if 0 <= current["Thresh"] <= 100:
            isValid["Thresh"] = True
        else: invalidInputs.append("Threshold")
    except: invalidInputs.append("Threshold")

    try:
        current["TimeInt"]=float(current["TimeInt"])
        if 1 <= current["TimeInt"] <= 43200:
            isValid["TimeInt"] = True
        else: invalidInputs.append("Interval")
    except: invalidInputs.append("Interval")

    if current["Sample"].isnumeric():
        current["Sample"]=int(current["Sample"])
        try:
            int(current["TimeInt"])
            if 1 <= current["Sample"] <= int(current["TimeInt"]):
                isValid["Sample"] = True
            else: invalidInputs.append("Sample Count")
        except:
            invalidInputs.append("Sample Count")     
    else: invalidInputs.append("Sample Count")

    changeBoxColors(isValid)

    if all(isValid.values()):
        status.config(text="Changes saved successfully!", foreground=fgColor)
        printSettings()
        disableSave()
    else:
        line1=BrightnessError
        line2,s,err="","",""
        if len(invalidInputs)>0:
            if len(invalidInputs)>1: s='s'
            if line1!="": line1+='\n'
            if len(invalidInputs)>2: invalidInputs.insert(3,'\n')
            for i in invalidInputs:
                if i != '\n': err+=(i+', ')
                else: err+=(i+'            ')
            if err[-2:] ==', ': err=err[:-2]
            else:
                err=err[:-15]
                err+=(i+'           ')
            line2="Error: Invalid {} Input{}".format(err,s)
        status.config(text=line1+line2, foreground=errColor)
def changeBoxColors(isValid):
    if isValid["MinB"]:
        left.itemconfig(minbox,fill=lightGrey,outline=brightGrey)
        minValLabel.config(bg=lightGrey)
        minVal.config(bg=lightGrey)
    else:
        left.itemconfig(minbox,fill='#683333',outline=errColor)
        minValLabel.config(bg='#683333')
        minVal.config(bg='#683333')

    if isValid["MaxB"]:
        left.itemconfig(maxbox,fill=lightGrey,outline=brightGrey)
        maxValLabel.config(bg=lightGrey)
        maxVal.config(bg=lightGrey)
    else:
        left.itemconfig(maxbox,fill='#683333',outline=errColor)
        maxValLabel.config(bg='#683333')
        maxVal.config(bg='#683333')

    if isValid["Webcam"]:
        right.itemconfig(box1,fill=lightGrey,outline=brightGrey)
        wbdevInput.config(bg=lightGrey)
        wbdevValue.config(style="norm.TMenubutton")
    else:
        right.itemconfig(box1,fill='#683333',outline=errColor)
        wbdevInput.config(bg='#683333')
        wbdevValue.config(style="err.TMenubutton")
    
    if isValid["Sample"]:
        right.itemconfig(box2,fill=lightGrey,outline=brightGrey)
        sampleInput.config(bg=lightGrey)
        sampleValue.config(bg=lightGrey)
    else:
        right.itemconfig(box2,fill='#683333',outline=errColor)
        sampleInput.config(bg='#683333')
        sampleValue.config(bg='#683333')

    if isValid["Thresh"]:
        right.itemconfig(box3,fill=lightGrey,outline=brightGrey)
        threshInput.config(bg=lightGrey)
        threshValue.config(bg=lightGrey)
    else:
        right.itemconfig(box3,fill='#683333',outline=errColor)
        threshInput.config(bg='#683333')
        threshValue.config(bg='#683333')

    if isValid["TimeInt"]:
        right.itemconfig(box4,fill=lightGrey,outline=brightGrey)
        intvInput.config(bg=lightGrey)
        intvValue.config(bg=lightGrey)
    else:
        right.itemconfig(box4,fill='#683333',outline=errColor)
        intvInput.config(bg='#683333')
        intvValue.config(bg='#683333')
def printSettings():
    print("Minimum Brightness:", get_Minimum_value()+'%')
    print("Maximum Brightness:", get_Maximum_value()+'%')
    print("Webcam Device:", selectedWebcam.get())
    print("Sample Count:", sampleValue.get())
    print("Threshold:", threshValue.get())
    print("Time Interval:", intvValue.get())
    print("Enable on Start-Up?", enableStartupVar.get())
    print("Disable Webcam Preview?", disablewcpvVar.get())
def on_closing():
    exit = messagebox.askokcancel("Close Program", 
            "Would you like to exit WAABP?\n\nWarning: Closing the program would\nstop all of its processes.")
    if exit:
        root.destroy()
def minSliderChanged(event):
    minValLabel.configure(text=get_Minimum_value()+'%')
    createLineCurve(left,get_Minimum_value(),get_Maximum_value())
    enableSave('x')
def maxSliderChanged(event):
    maxValLabel.configure(text=get_Maximum_value()+'%')
    createLineCurve(left,get_Minimum_value(),get_Maximum_value())
    enableSave('x')
def get_Minimum_value():
    return '{:.0f}'.format(sliderMinVal.get())
def get_Maximum_value():
    return '{:.0f}'.format(sliderMaxVal.get())
def createLineCurve(canvas,minSlider,maxSlider):
    y0=100+(((100-int(minSlider))/100)*200)
    y1=100+(((100-int(maxSlider))/100)*200)
    if y0<y1: color=errColor 
    elif y0==y1: color="#FFC001"
    else: color=fgColor
    #FFC001

    canvas.delete('line')
    return canvas.create_line(80,y0,280,y1,fill=color,width=2,tags='line')
def enableSave(event):
    saveButton["state"] = NORMAL
def disableSave():
    saveButton["state"] = DISABLED

lightGrey="#3A3A3A"
grey="#262626"
black="black"
brightGrey='#595959'
fgColor="#5B9BD5"
errColor="#FF5050"

root = Tk()
root.resizable(False,False)
root.title("WAABA")
root.iconbitmap(os.path.dirname(os.path.abspath(__file__))+'/icon.ico')
positionRight = int(root.winfo_screenwidth()/2 - 880/2)
positionDown = int(root.winfo_screenheight()/2 - 495/2)
root.geometry("880x495+{}+{}".format(positionRight, positionDown))
root.configure(background=grey,highlightcolor=fgColor,highlightthickness=1)

########################
######## header ########
########################

header= Frame(root, highlightbackground=fgColor, bg=grey, highlightcolor=fgColor, highlightthickness=1, width=880, height=55, bd= 0)
header.pack_propagate(0)
header.pack()

title = Frame(header,width=80,height=30,bg=grey)
title.pack_propagate(0)
Label(title,bg=grey,fg="white",text="WAABA:",font=("Bahnschrift Bold",14)).pack()
title.pack(side=LEFT,padx=(15,0))

subtitle = Frame(header,width=600,height=20,bg=grey)
subtitle.pack_propagate(0)
Label(subtitle, text = "A Webcam-based Adjustable Adaptive Brightness Application", font=("Bahnschrift Light",10), bg=grey,fg='white',justify='left').pack(side="left")
subtitle.pack(side=LEFT,padx=0,pady=(6,0))

home = Frame(header,width=100,height=30,bg=black,highlightbackground=fgColor,highlightthickness=0,cursor='hand2')
home.pack_propagate(0)
homeButton=Button(home, font=("Bahnschrift SemiBold",10), bg=lightGrey,fg='white',text = "HOME", padx=35,pady=10, command = openHome,
                    activebackground=fgColor,activeforeground="black",borderwidth = 0)
homeButton.pack(fill=X, side=LEFT)
home.place(x=759,y=12)
changeButtonOnHover(homeButton, "#364A5B", lightGrey)

######################
######## left ########
######################

left= Canvas(root, highlightbackground=fgColor, bg=grey, highlightcolor=fgColor, highlightthickness=1, width=340, height=440, bd= 0)
left.pack(side=LEFT)

graphLabel = Frame(left,width=332,height=50,bg=grey)
graphLabel.pack_propagate(0)
Label(graphLabel, text = "Adjustable linear curve for\nScreen Brightness", font='{Bahnschrift SemiBold} 13', bg=grey,fg='#FFFFFF').pack(fill=BOTH)
graphLabel.place(x=5,y=25)

sliderMinVal = DoubleVar()
sliderMin = ttk.Scale(left,length=200,from_=100,to=0,orient='vertical', command=minSliderChanged, variable=sliderMinVal)
sliderMin.set(0.0)
ttk.Style().configure("Vertical.TScale", background=grey)
sliderMin.place(x=50,y=100)
minL1 = Frame(left,width=26,height=20,bg=grey)
minL1.pack_propagate(0)
Label(minL1, text = "100", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=TOP)
minL1.place(x=50,y=77)
maxL1 = Frame(left,width=26,height=20,bg=grey)
maxL1.pack_propagate(0)
Label(maxL1, text = "0", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=TOP)
maxL1.place(x=50,y=303)

sliderMaxVal = DoubleVar()
sliderMax = ttk.Scale(left,length=200,from_=100,to=0,orient='vertical', command=maxSliderChanged, variable=sliderMaxVal)
sliderMax.set(100.0)
sliderMax.place(x=285,y=100)
minL2 = Frame(left,width=26,height=20,bg=grey)
minL2.pack_propagate(0)
Label(minL2, text = "100", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=TOP)
minL2.place(x=285,y=77)
maxL2 = Frame(left,width=26,height=20,bg=grey)
maxL2.pack_propagate(0)
Label(maxL2, text = "0", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=TOP)
maxL2.place(x=285,y=303)

yLabel=PhotoImage(file=os.path.dirname(os.path.abspath(__file__))+'/LabelY.png')
left.create_image(40,200, image=yLabel)
xLabel=PhotoImage(file=os.path.dirname(os.path.abspath(__file__))+'/LabelX.png')
left.create_image(80,308, image=xLabel, anchor=NW)

minBoxLabel = Frame(left,width=80,height=38,bg=grey)
minBoxLabel.pack_propagate(0)
Label(minBoxLabel, text = "Minimum\nBrightness:", font='{Bahnschrift Light} 10',justify='left', bg=grey,fg='#FFFFFF').pack(side=TOP)
minBoxLabel.place(x=20,y=350)
minbox=round_rectangle(left,105,351,50,35,radius=15,fill=lightGrey,outline=brightGrey)
minVal = Frame(left,width=41,height=20,bg=lightGrey)
minVal.pack_propagate(0)
minValLabel=Label(minVal, text = '0%', font='{Bahnschrift Light} 10', bg=lightGrey,fg='#FFFFFF')
minValLabel.pack(side=TOP)
minVal.place(x=110,y=359)

maxBoxLabel = Frame(left,width=80,height=38,bg=grey)
maxBoxLabel.pack_propagate(0)
Label(maxBoxLabel, text = "Maximum\nBrightness:", font='{Bahnschrift Light} 10',justify='left', bg=grey,fg='#FFFFFF').pack(side=TOP)
maxBoxLabel.place(x=185,y=350)
maxbox=round_rectangle(left,270,351,50,35,radius=15,fill=lightGrey,outline=brightGrey)
maxVal = Frame(left,width=41,height=20,bg=lightGrey)
maxVal.pack_propagate(0)
maxValLabel=Label(maxVal, text = '100%', font='{Bahnschrift Light} 10', bg=lightGrey,fg='#FFFFFF')
maxValLabel.pack(side=TOP)
maxVal.place(x=275,y=359)

graphBox= left.create_rectangle(80, 100, 280, 300,fill=lightGrey,outline=lightGrey)
for x in range(100,280,20):
    left.create_line(x,100,x,300,fill=grey,width=2)
for y in range(120,300,20):
    left.create_line(80,y,280,y,fill=grey,width=2)
createLineCurve(left,get_Minimum_value(),get_Maximum_value())

#######################
######## right ########
#######################

right= Canvas(root, highlightbackground=fgColor, bg=grey, highlightcolor=fgColor, highlightthickness=1, width=540, height=440, bd= 0)
right.pack(side=LEFT)

settingsLabel = Frame(right,width=520,height=30,bg=grey)
settingsLabel.pack_propagate(0)
Label(settingsLabel, text = "Settings", font='{Bahnschrift SemiBold} 14', bg=grey,fg='#FFFFFF').pack(fill=BOTH)
settingsLabel.place(x=8,y=25)

box1=round_rectangle(right,142,80,115,35,radius=15,fill=lightGrey,outline=brightGrey)#webcam device
box2=round_rectangle(right,400,80,115,35,radius=15,fill=lightGrey,outline=brightGrey)#sample count
box3=round_rectangle(right,142,140,115,35,radius=15,fill=lightGrey,outline=brightGrey)#threshold
box4=round_rectangle(right,400,140,115,35,radius=15,fill=lightGrey,outline=brightGrey)#time interval
box5=round_rectangle(right,17,265,500,45,radius=17,fill=lightGrey)#settings description

wbdevLabel = Frame(right,width=125,height=30,bg=grey,cursor='question_arrow')
wbdevLabel.pack_propagate(0)
Label(wbdevLabel, text = "Webcam Device:", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=LEFT)
wbdevLabel.place(x=17,y=83)
changeSettingDesc(wbdevLabel, 0)

wbdevList=('-----------','Webcam 1','Webcam 2','Webcam 3')
selectedWebcam = StringVar()
wbdevInput = Frame(right,width=110,height=30,bg=lightGrey)
wbdevInput.pack_propagate(0)
ttk.Style().configure("err.TMenubutton", background='#683333',foreground='white',highlightthickness=0)
ttk.Style().configure("norm.TMenubutton", background=lightGrey,foreground='white',highlightthickness=0)
wbdevValue=ttk.OptionMenu(wbdevInput,selectedWebcam,wbdevList[0],*wbdevList,style="norm.TMenubutton")
wbdevValue.configure(width=110)
wbdevValue.pack(side=LEFT,fill=BOTH)
wbdevInput.place(x=145,y=83)
changeSettingDesc(wbdevInput, 0)

sampleLabel = Frame(right,width=125,height=30,bg=grey,cursor='question_arrow')
sampleLabel.pack_propagate(0)
Label(sampleLabel, text = "Sample Count:", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=LEFT)
sampleLabel.place(x=275,y=83)
changeSettingDesc(sampleLabel, 1)

sampleInput = Frame(right,width=110,height=30,bg=lightGrey)
sampleInput.pack_propagate(0)
sampleVar = StringVar()
sampleVar.trace("w", lambda name, index, mode, sampleVar=sampleVar: enableSave(sampleVar))
sampleValue=Entry(sampleInput, font='{Bahnschrift Light} 10', bg=lightGrey,fg='#FFFFFF',bd=0,insertbackground="white",insertborderwidth=1,textvariable=sampleVar)
sampleValue.insert(0,"1")
sampleValue.pack(side=LEFT,fill=BOTH,padx=(7,0))
sampleInput.place(x=403,y=83)
changeSettingDesc(sampleInput, 1)

threshLabel = Frame(right,width=125,height=30,bg=grey,cursor='question_arrow')
threshLabel.pack_propagate(0)
Label(threshLabel, text = "Threshold %:", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=LEFT)
threshLabel.place(x=17,y=143)
changeSettingDesc(threshLabel, 2)

threshInput = Frame(right,width=110,height=30,bg=lightGrey)
threshInput.pack_propagate(0)
threshVar = StringVar()
threshVar.trace("w", lambda name, index, mode, threshVar=threshVar: enableSave(threshVar))
threshValue=Entry(threshInput, font='{Bahnschrift Light} 10', bg=lightGrey,fg='#FFFFFF',bd=0,insertbackground="white",insertborderwidth=1, textvariable=threshVar)
threshValue.insert(0,"1")
threshValue.pack(side=LEFT,fill=BOTH,padx=(7,0))
threshInput.place(x=145,y=143)
changeSettingDesc(threshInput, 2)

intvLabel = Frame(right,width=125,height=30,bg=grey,cursor='question_arrow')
intvLabel.pack_propagate(0)
Label(intvLabel, text = "Interval (sec):", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=LEFT)
intvLabel.place(x=275,y=143)
changeSettingDesc(intvLabel, 3)

intvInput = Frame(right,width=110,height=30,bg=lightGrey)
intvInput.pack_propagate(0)
intVar = StringVar()
intVar.trace("w", lambda name, index, mode, intVar=intVar: enableSave(intVar))
intvValue=Entry(intvInput, font='{Bahnschrift Light} 10', bg=lightGrey,fg='#FFFFFF',bd=0,insertbackground="white",insertborderwidth=1,textvariable=intVar)
intvValue.insert(0,"1")
intvValue.pack(side=LEFT,fill=BOTH,padx=(7,0))
intvInput.place(x=403,y=143)
changeSettingDesc(intvInput, 3)

###checkboxes###
on_image = PhotoImage(width=44, height=25)
off_image = PhotoImage(width=44, height=25)
on_image.put(('white',), to=(20, 0, 42, 23))
off_image.put(('white',), to=(1, 1, 23,24))

enableStartupVar = BooleanVar()
disablewcpvVar = BooleanVar()

enableStartupVar.trace("w", lambda name, index, mode, enableStartupVar=enableStartupVar: enableSave(enableStartupVar))
enStartUpBox = Checkbutton(right, image=off_image, selectimage=on_image, indicatoron=False, onvalue=True, offvalue=False, 
                    variable=enableStartupVar, bd=0, selectcolor=fgColor, bg='#969696',activebackground='#7999B6')
enStartUpBox.place(x=17,y=204)
enableStartup = Frame(right,width=190,height=30,bg=grey,cursor='question_arrow')
enableStartup.pack_propagate(0)
Label(enableStartup, text = "Enable program on start-up", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=LEFT,padx=(3,0))
enableStartup.place(x=67,y=203)
changeSettingDesc(enStartUpBox, 4)
changeSettingDesc(enableStartup, 4)

disablewcpvVar.trace("w", lambda name, index, mode, disablewcpvVar=disablewcpvVar: enableSave(disablewcpvVar))
disablewcBox = Checkbutton(right, image=off_image, selectimage=on_image, indicatoron=False, onvalue=True, offvalue=False, 
                    variable=disablewcpvVar, bd=0, selectcolor=fgColor, bg='#969696',activebackground='#7999B6')
disablewcBox.place(x=275,y=204)
disablewcpv = Frame(right,width=190,height=30,bg=grey,cursor='question_arrow')
disablewcpv.pack_propagate(0)
Label(disablewcpv, text = "Disable webcam preview", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=LEFT,padx=(3,0))
disablewcpv.place(x=325,y=203)
changeSettingDesc(disablewcBox, 5)
changeSettingDesc(disablewcpv, 5)

settingDesc = Frame(right,width=493,height=24,bg=lightGrey)
settingDesc.pack_propagate(0)
desc=Label(settingDesc, text = "Setting Description: (appears on mouse hover)", 
                    font='{Bahnschrift Light} 10', bg=lightGrey,fg='#FFFFFF')
desc.pack(side=TOP,padx=(3,0),fill=BOTH)
settingDesc.place(x=20,y=276)

saveSettings = Frame(right,width=155,height=50,bg=black,highlightbackground=fgColor,highlightthickness=0,cursor='hand2')
saveSettings.pack_propagate(0)
saveButton=Button(saveSettings, font=("Bahnschrift SemiBold",11), bg=lightGrey,fg='white',text = "APPLY CHANGES", padx=15,pady=12, 
                    command = validateSettings,activebackground=fgColor,activeforeground="black",borderwidth = 0,state=DISABLED)
saveButton.pack(side=TOP,fill='x')
saveSettings.place(x=17,y=343)
changeButtonOnHover(saveButton, "#364A5B", lightGrey)

statusFrame = Frame(right,width=330,height=50,bg=grey)
statusFrame.pack_propagate(0)
status=Label(statusFrame, text = "", font='{Bahnschrift SemiBold} 9', bg=grey,fg='#FFFFFF',justify="left")
status.pack(side=LEFT,fill=BOTH)
statusFrame.place(x=185,y=343)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()