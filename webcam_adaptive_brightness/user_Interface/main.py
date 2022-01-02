from tkinter import *
from tkinter import messagebox

def round_rectangle(canvas,x1, y1, x2, y2, radius=25, **kwargs):
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
def opensettings():
   messagebox.showinfo("Settings", "just imagine ur in d settings")
def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

webcamvalue=100 #webcam brightness value
screenvalue=100 #screen brightness value
lightGrey="#3A3A3A"
grey="#262626"
fgBlue="#5B9BD5"


root = Tk()
root.resizable(False,False)
root.title("WAABP")
positionRight = int(root.winfo_screenwidth()/2 - 880/2)
positionDown = int(root.winfo_screenheight()/2 - 495/2)
root.geometry("880x495+{}+{}".format(positionRight, positionDown))
root.configure(background='#262626',highlightcolor=fgBlue,highlightthickness=1)

#bgcolor=#262626 dark grey, #3A3A3A light grey



######## header ########
header= Frame(root, highlightbackground=fgBlue, bg='#262626', highlightcolor=fgBlue, highlightthickness=1, width=880, height=55, bd= 0)
header.pack_propagate(0)
header.pack()

title = Frame(header,width=80,height=30,bg=grey)
title.pack_propagate(0)
Label(title,bg=grey,fg="white",text="WAABP:",font=("Bahnschrift Bold",14)).pack()
title.pack(side=LEFT,padx=(15,0))

subtitle = Frame(header,width=340,height=20,bg=grey)
subtitle.pack_propagate(0)
Label(subtitle, text = "A Webcam-based Adjustable Adaptive Brightness Program", font=("Bahnschrift Light",10), bg=grey,fg='white').pack()
subtitle.pack(side=LEFT,padx=0,pady=(6,0))

settings = Frame(header,width=70,height=30,bg=grey,highlightbackground=fgBlue,highlightthickness=1)
settings.pack_propagate(0)
settingsButton=Button(settings, font=("Bahnschrift",10), bg='#262626',fg='#FFFFFF',text = "Settings", padx=5,pady=3, command = opensettings,activebackground=fgBlue,activeforeground="black",borderwidth = 0)
settingsButton.pack(fill=X)
settings.pack(side=RIGHT,padx=(0,15))
changeOnHover(settingsButton, "#364A5B", grey)

######## middle ########
middle= Canvas(root, highlightbackground=fgBlue, bg='#262626', highlightcolor=fgBlue, highlightthickness=1, width=880, height=385, bd= 0)
middle.pack(side=TOP)

webcamF1=Frame(middle,width=187,height=44,bg=lightGrey)
webcamF1.pack_propagate(0)
Label(webcamF1, text = "Current Webcam\nBrightness", font='{Bahnschrift Light} 12', bg=lightGrey,fg='#FFFFFF').pack()
webcamF1.place(x=40,y=49)
webcamB1=round_rectangle(middle,35,40,230,102,radius=20,fill=lightGrey,outline='#595959')

webcamF2 = Frame(middle,width=187,height=87,bg=lightGrey)
webcamF2.pack_propagate(0)
Label(webcamF2, text="{}%".format(webcamvalue), font='{Bahnschrift Light} 50', bg=lightGrey,fg='#FFFFFF',width=4,justify='center').pack()
webcamF2.place(x=40,y=185)
webcamB2=round_rectangle(middle,35,120,230,340,radius=20,fill=lightGrey,outline='#595959')

screenF1 = Frame(middle,width=188,height=44,bg=lightGrey)
screenF1.pack_propagate(0)
Label(screenF1, text = "Calculated Screen\nBrightness", font='{Bahnschrift Light} 12', bg=lightGrey,fg='#FFFFFF').pack()
screenF1.place(x=252,y=49)
screenB1=round_rectangle(middle,248,40,443,102,radius=20,fill=lightGrey,outline='#595959')

screenF2 = Frame(middle,width=187,height=87,bg=lightGrey)
screenF2.pack_propagate(0)
Label(screenF2, text = "{}%".format(screenvalue), font='{Bahnschrift Light} 50', bg=lightGrey,fg='#FFFFFF',width=4,justify='center').pack()
screenF2.place(x=252,y=185)
screenbox2=round_rectangle(middle,248,120,443,340,radius=20,fill=lightGrey,outline='#595959')

previewbox=round_rectangle(middle,461,40,845,340,radius=20,fill=lightGrey,outline='#595959')
preview = Frame(middle,width=376,height=25,bg=lightGrey)
preview.pack_propagate(0)
Label(preview, text = "Webcam Preview", font='{Bahnschrift Light} 12', bg=lightGrey,fg='#FFFFFF').pack(fill=BOTH)
preview.place(x=465,y=50)

webcamFrame = Frame(middle, width=300, height=225,bg='#000')
webcamFrame.place(x=505,y=85)

######## bottom ########
bottom= Frame(root, highlightbackground=fgBlue, bg='#262626', highlightcolor=fgBlue, highlightthickness=1, width=880, height=55, bd= 0)
bottom.pack(side=TOP)

root.mainloop()