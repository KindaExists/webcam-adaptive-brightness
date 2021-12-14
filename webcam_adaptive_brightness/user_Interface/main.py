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


webcamvalue=100 #webcam brightness value
screenvalue=100 #screen brightness value

root = Tk()
root.resizable(False,False)
root.title("WAABP")
positionRight = int(root.winfo_screenwidth()/2 - 880/2)
positionDown = int(root.winfo_screenheight()/2 - 495/2)
root.geometry("880x495+{}+{}".format(positionRight, positionDown))
root.configure(background='#262626',highlightcolor='#5B9BD5',highlightthickness=1)

header= Frame(root, highlightbackground='#5B9BD5', bg='#262626', highlightcolor='#5B9BD5', highlightthickness=1, width=880, height=55, bd= 0)
header.pack()

title = Label(header, text = "WAABP:", font='Bahnschrift 14 bold', bg='#262626',fg='#FFFFFF').place(x = 20, y = 11)
subtitle = Label(header, text = "A Webcam-based Adjustable Adaptive Brightness Program", font='Bahnschrift 10', bg='#262626',fg='#FFFFFF').place(x = 95, y = 17)  
settings = Button(header, font='Bahnschrift 10', bg='#262626',fg='#FFFFFF',text = "Settings", padx=5,pady=3, command = opensettings).place(x=790,y=11)

middle= Canvas(root, highlightbackground='#5B9BD5', bg='#262626', highlightcolor='#5B9BD5', highlightthickness=1, width=880, height=385, bd= 0)
middle.pack(side=TOP)

webcambox1=round_rectangle(middle,35,40,230,102,radius=20,fill='#3A3A3A',outline='#595959')
webcamlabel = Label(middle, text = "Current Webcam\n Brightness", font='{Bahnschrift Light} 12', bg='#3A3A3A',fg='#FFFFFF').place(x = 70, y = 47)
webcambox2=round_rectangle(middle,35,120,230,340,radius=20,fill='#3A3A3A',outline='#595959')
webcamvaluelabel = Label(middle, text = "{}%".format(webcamvalue), font='{Bahnschrift Light} 50', bg='#3A3A3A',fg='#FFFFFF',width=4,justify='center').place(x = 57, y = 180)

screenbox1=round_rectangle(middle,248,40,443,102,radius=20,fill='#3A3A3A',outline='#595959')
screenlabel = Label(middle, text = "Calculated Screen\n Brightness", font='{Bahnschrift Light} 12', bg='#3A3A3A',fg='#FFFFFF').place(x = 275, y = 47)
screenbox2=round_rectangle(middle,248,120,443,340,radius=20,fill='#3A3A3A',outline='#595959')
screenvaluelabel = Label(middle, text = "{}%".format(screenvalue), font='{Bahnschrift Light} 50', bg='#3A3A3A',fg='#FFFFFF',width=4,justify='center').place(x = 269, y = 180)

previewbox=round_rectangle(middle,461,40,845,340,radius=20,fill='#3A3A3A',outline='#595959')
previewlabel = Label(middle, text = "Webcam Preview", font='{Bahnschrift Light} 12', bg='#3A3A3A',fg='#FFFFFF').place(x = 590, y = 50)
webcamFrame = Frame(middle, width=300, height=225,bg='#000').place(x=505,y=85)

bottom= Frame(root, highlightbackground='#5B9BD5', bg='#262626', highlightcolor='#5B9BD5', highlightthickness=1, width=880, height=55, bd= 0)
bottom.pack(side=TOP)

root.mainloop()