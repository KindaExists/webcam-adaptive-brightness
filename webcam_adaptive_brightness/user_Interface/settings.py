from tkinter import *
from tkinter import messagebox
from tkinter import ttk

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
def printSettings():
    print("Webcam Device:", selectedWebcam.get())
    print("Sample Count:", sampleValue.get())
    print("Threshold:", threshValue.get())
    print("Time Interval:", intvValue.get())
    print("Enable on Start-Up?", enableStartupVal.get())
    print("Disable Webcam Preview?", disablewcpvVal.get())

webcamvalue=100 #webcam brightness value
screenvalue=100 #screen brightness value
lightGrey="#3A3A3A"
grey="#262626"
black="black"
fgColor="#5B9BD5"


root = Tk()
root.resizable(False,False)
root.title("WAABP")
positionRight = int(root.winfo_screenwidth()/2 - 880/2)
positionDown = int(root.winfo_screenheight()/2 - 495/2)
root.geometry("880x495+{}+{}".format(positionRight, positionDown))
root.configure(background=grey,highlightcolor=fgColor,highlightthickness=1)

######## header ########
header= Frame(root, highlightbackground=fgColor, bg=grey, highlightcolor=fgColor, highlightthickness=1, width=880, height=55, bd= 0)
header.pack_propagate(0)
header.pack()

title = Frame(header,width=80,height=30,bg=grey)
title.pack_propagate(0)
Label(title,bg=grey,fg="white",text="WAABP:",font=("Bahnschrift Bold",14)).pack()
title.pack(side=LEFT,padx=(15,0))

subtitle = Frame(header,width=600,height=20,bg=grey)
subtitle.pack_propagate(0)
Label(subtitle, text = "A Webcam-based Adjustable Adaptive Brightness Program", font=("Bahnschrift Light",10), bg=grey,fg='white',justify='left').pack(side="left")
subtitle.pack(side=LEFT,padx=0,pady=(6,0))

home = Frame(header,width=70,height=30,bg=grey,highlightbackground=fgColor,highlightthickness=1,cursor='hand2')
home.pack_propagate(0)
homeButton=Button(home, font=("Bahnschrift",10), bg=grey,fg='white',text = "Home", padx=5,pady=3, command = openHome,
                    activebackground=fgColor,activeforeground="black",borderwidth = 0)
homeButton.pack(fill=X)
home.pack(side=RIGHT,padx=(0,15))
changeButtonOnHover(homeButton, "#364A5B", grey)

######## left ########
left= Canvas(root, highlightbackground=fgColor, bg=grey, highlightcolor=fgColor, highlightthickness=1, width=340, height=440, bd= 0)
left.pack(side=LEFT)

######## right ########
right= Canvas(root, highlightbackground=fgColor, bg=grey, highlightcolor=fgColor, highlightthickness=1, width=540, height=440, bd= 0)
right.pack(side=LEFT)

settingsLabel = Frame(right,width=520,height=30,bg=grey)
settingsLabel.pack_propagate(0)
Label(settingsLabel, text = "Settings", font='{Bahnschrift SemiBold} 14', bg=grey,fg='#FFFFFF').pack(fill=BOTH)
settingsLabel.place(x=8,y=25)

box1=round_rectangle(right,142,80,115,35,radius=15,fill=lightGrey,outline='#595959')#webcam device
box2=round_rectangle(right,400,80,115,35,radius=15,fill=lightGrey,outline='#595959')#sample count
box3=round_rectangle(right,142,140,115,35,radius=15,fill=lightGrey,outline='#595959')#threshold
box4=round_rectangle(right,400,140,115,35,radius=15,fill=lightGrey,outline='#595959')#time interval
box5=round_rectangle(right,17,265,500,45,radius=17,fill=lightGrey)#settings description

wbdevLabel = Frame(right,width=125,height=30,bg=grey,cursor='question_arrow')
wbdevLabel.pack_propagate(0)
Label(wbdevLabel, text = "Webcam Device:", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=LEFT)
wbdevLabel.place(x=17,y=83)
changeSettingDesc(wbdevLabel, 0)

wbdevList=('Webcam 1','Webcam 2','Webcam 3')
selectedWebcam = StringVar()
wbdevInput = Frame(right,width=110,height=30,bg=lightGrey)
wbdevInput.pack_propagate(0)
wbdevValue=ttk.OptionMenu(wbdevInput,selectedWebcam,wbdevList[0],*wbdevList)
wbdevValue.configure(width=110)
ttk.Style().configure("TMenubutton", background=lightGrey,foreground='white',highlightthickness=0)
wbdevValue.pack(side=LEFT,fill=BOTH)
wbdevInput.place(x=145,y=83)

sampleLabel = Frame(right,width=125,height=30,bg=grey,cursor='question_arrow')
sampleLabel.pack_propagate(0)
Label(sampleLabel, text = "Sample Count:", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=LEFT)
sampleLabel.place(x=275,y=83)
changeSettingDesc(sampleLabel, 1)

sampleInput = Frame(right,width=110,height=30,bg=lightGrey)
sampleInput.pack_propagate(0)
sampleValue=Entry(sampleInput, font='{Bahnschrift Light} 10', bg=lightGrey,fg='#FFFFFF',bd=0,insertbackground="white",insertborderwidth=1)
sampleValue.insert(0,"0")
sampleValue.pack(side=LEFT,fill=BOTH,padx=(7,0))
sampleInput.place(x=403,y=83)

threshLabel = Frame(right,width=125,height=30,bg=grey,cursor='question_arrow')
threshLabel.pack_propagate(0)
Label(threshLabel, text = "Threshold:", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=LEFT)
threshLabel.place(x=17,y=143)
changeSettingDesc(threshLabel, 2)

threshInput = Frame(right,width=110,height=30,bg=lightGrey)
threshInput.pack_propagate(0)
threshValue=Entry(threshInput, font='{Bahnschrift Light} 10', bg=lightGrey,fg='#FFFFFF',bd=0,insertbackground="white",insertborderwidth=1)
threshValue.insert(0,"1")
threshValue.pack(side=LEFT,fill=BOTH,padx=(7,0))
threshInput.place(x=145,y=143)

intvLabel = Frame(right,width=125,height=30,bg=grey,cursor='question_arrow')
intvLabel.pack_propagate(0)
Label(intvLabel, text = "Interval (sec):", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=LEFT)
intvLabel.place(x=275,y=143)
changeSettingDesc(intvLabel, 3)

intvInput = Frame(right,width=110,height=30,bg=lightGrey)
intvInput.pack_propagate(0)
intvValue=Entry(intvInput, font='{Bahnschrift Light} 10', bg=lightGrey,fg='#FFFFFF',bd=0,insertbackground="white",insertborderwidth=1)
intvValue.insert(0,"1")
intvValue.pack(side=LEFT,fill=BOTH,padx=(7,0))
intvInput.place(x=403,y=143)

###checkboxes###
on_image = PhotoImage(width=44, height=25)
off_image = PhotoImage(width=44, height=25)
on_image.put(('white',), to=(20, 0, 42, 23))
off_image.put(('white',), to=(1, 1, 23,24))

enableStartupVal = BooleanVar()
disablewcpvVal = BooleanVar()

enStartUpBox = Checkbutton(right, image=off_image, selectimage=on_image, indicatoron=False, onvalue=True, offvalue=False, 
                    variable=enableStartupVal, bd=0, selectcolor=fgColor, bg='#969696',activebackground='#7999B6')
enStartUpBox.place(x=17,y=204)
enableStartup = Frame(right,width=190,height=30,bg=grey,cursor='question_arrow')
enableStartup.pack_propagate(0)
Label(enableStartup, text = "Enable program on start-up", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=LEFT,padx=(3,0))
enableStartup.place(x=67,y=203)
changeSettingDesc(enableStartup, 4)

disablewcBox = Checkbutton(right, image=off_image, selectimage=on_image, indicatoron=False, onvalue=True, offvalue=False, 
                    variable=disablewcpvVal, bd=0, selectcolor=fgColor, bg='#969696',activebackground='#7999B6')
disablewcBox.place(x=275,y=204)
disablewcpv = Frame(right,width=190,height=30,bg=grey,cursor='question_arrow')
disablewcpv.pack_propagate(0)
Label(disablewcpv, text = "Disable webcam preview", font='{Bahnschrift Light} 10', bg=grey,fg='#FFFFFF').pack(side=LEFT,padx=(3,0))
disablewcpv.place(x=325,y=203)
changeSettingDesc(disablewcpv, 5)

settingDesc = Frame(right,width=493,height=24,bg=lightGrey)
settingDesc.pack_propagate(0)
desc=Label(settingDesc, text = "Setting Description: (appears on mouse hover)", 
                    font='{Bahnschrift Light} 10', bg=lightGrey,fg='#FFFFFF')
desc.pack(side=TOP,padx=(3,0),fill=BOTH)
settingDesc.place(x=20,y=276)

saveSettings = Frame(right,width=150,height=39,bg=grey,highlightbackground=fgColor,highlightthickness=1,cursor='hand2')
saveSettings.pack_propagate(0)
saveButton=Button(saveSettings, font=("Bahnschrift Light",11), bg=grey,fg='white',text = "Apply Changes", padx=5,pady=6, 
                    command = printSettings,activebackground=fgColor,activeforeground="black",borderwidth = 0)
saveButton.pack(fill=BOTH)
saveSettings.place(x=17,y=335)
changeButtonOnHover(saveButton, "#364A5B", grey)

root.mainloop()