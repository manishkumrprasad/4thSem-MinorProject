# All Required Imports And Libraries Required For The Project
import tkinter as tk
from tkinter import colorchooser
from tkinter import Button
from tkinter import messagebox

window = tk.Tk()
window.geometry("1100x500")
window.title("Painting Window Version 10")
# window.resizable(False , False)

# ------------------------------------------Parent-Frame-Section-Open----------------------------------------------------------+

# Parent Paint Toolbars / Which Will Contain All The Tools Frame Such As toolbar , color pallette , file management , help box etc
frameOne = tk.Frame(window , bg="#D6F5EF" , width=1280,height=170)
frameOne.grid(row=0 , column=0 , sticky=tk.NW)

# Parent Paint Frame Which Contain Only The Canvas Frame
frameTwo = tk.Frame(window , bg="yellow" , width=1280,height=800)
frameTwo.grid(row=1 , column=0)

# ------------------------------------------Parent-Frame-Section-Close----------------------------------------------------------+


# ------------------------------------------Icon-Section-Open----------------------------------------------------------+

#The Icon Section Contains All The Icon That Are Going To Be Used Throughout The Program  
iconOfPencil = tk.PhotoImage(file="Icons/Small_Pencil.png")
iconOfEraser = tk.PhotoImage(file="Icons/Small_Eraser.png")
iconOfFont = tk.PhotoImage(file="Icons/Small_Font.png")
iconOfGlass = tk.PhotoImage(file="Icons/Small_Glass.png")
iconOfFill = tk.PhotoImage(file="Icons/Small_Fill.png")
# iconOfSelectColor = tk.PhotoImage(file="Icons/Small_morecolors.png")
# iconOfSelectColor = tk.PhotoImage(file="Icons/Small_MoreColors2.png")
iconOfSelectColor = tk.PhotoImage(file="Icons/Small_MoreColorsWithPlus.png")

# ------------------------------------------Icon-Section-Close----------------------------------------------------------+

#-------------------------------------------Color-Box-Frame-Open--------------------------------------------------------------------+
# This Compartment Of The Code Handle The Position And Other Things Of The Color Selection Box
def selectcolor():
    selectedcolor = colorchooser.askcolor("red" , title="Select Color")
    stroke_color.set(selectedcolor[1])

colorBoxButton= Button(frameOne  , width=55, height=55, command=selectcolor , image= iconOfSelectColor , bg="#D6F5EF" , activebackground="#D6F5EF" , highlightthickness=0 , relief="flat",bd=0)
colorBoxButton.place(x=610, y=60)

#-------------------------------------------Color-Box-Frame-Close--------------------------------------------------------------------+


#-------------------------------------------Colors-Frame-Open--------------------------------------------------------------------+
# This Section Handle The Required Basic Colors Of Sets At The Upper Frame Of The Paint Window
colorFrame=tk.Frame(frameOne , height=120, width=230 , borderwidth=0 ,relief="sunken" ,bg="#D6F5EF")
colorFrame.place(x=415,y=55)

redButton=Button(colorFrame ,bg="Red",width=3 , height=1,activebackground="red", command=lambda:stroke_color.set("Red"), highlightthickness=0 , relief="flat" , bd=0)
redButton.grid(row=0,column=0 ,padx=5 , pady=5)

greenButton=Button(colorFrame ,bg="Green",width=3,height = 1,activebackground="green", command=lambda:stroke_color.set("Green"), highlightthickness=0 , relief="flat", bd=0)
greenButton.grid(row=0,column=1,padx=5 , pady=5)

blueButton=Button(colorFrame ,bg="Blue",width=3,height = 1,activebackground="blue", command=lambda:stroke_color.set("Blue"), highlightthickness=0 , relief="flat", bd=0)
blueButton.grid(row=0,column=2,padx=5 , pady=5)

yellowButton=Button(colorFrame ,bg="Yellow",width=3,height = 1,activebackground="yellow", command=lambda:stroke_color.set("Yellow"), highlightthickness=0 , relief="flat", bd=0)
yellowButton.grid(row=0,column=3,padx=5 , pady=5)

greyButton=Button(colorFrame ,bg="grey",width=3,height = 1,activebackground="grey", command=lambda:stroke_color.set("grey"), highlightthickness=0 , relief="flat", bd=0)
greyButton.grid(row=0,column=4,padx=5 , pady=5)

blackButton=Button(colorFrame ,bg="black",width=3,height = 1,activebackground="Black" ,command=lambda:stroke_color.set("Black") , fg="white", highlightthickness=0 , relief="flat", bd=0)
blackButton.grid(row=1,column=0,padx=5 , pady=5)

whiteButton=Button(colorFrame ,bg="White",width=3,height = 1,activebackground="white", command=lambda:stroke_color.set("White"), highlightthickness=0 , relief="flat", bd=0)
whiteButton.grid(row=1,column=1,padx=5 , pady=5)

orangeButton=Button(colorFrame ,bg="Orange",width=3,height = 1,activebackground="Orange", command=lambda:stroke_color.set("Orange"), highlightthickness=0 , relief="flat", bd=0)
orangeButton.grid(row=1,column=2,padx=5 , pady=5)

purpleButton=Button(colorFrame ,bg="Purple",width=3,height = 1, activebackground="Purple",command=lambda:stroke_color.set("Purple"), highlightthickness=0 , relief="flat", bd=0)
purpleButton.grid(row=1,column=3,padx=5 , pady=5)

pinkButton=Button(colorFrame ,bg="pink",width=3,height = 1, activebackground="pink",command=lambda:stroke_color.set("pink"), highlightthickness=0 , relief="flat", bd=0)
pinkButton.grid(row=1,column=4,padx=5 , pady=5)

MoreColors=Button
#-------------------------------------------Colors-Frame-Close--------------------------------------------------------------------+

# ------------------------------------------Tool-Functionality-Section-Open----------------------------------------------------------+
# This Part Of The Code Is Crucial As It Handles The Functionality Of The Buttons
stroke_color = tk.StringVar()
# stroke_color.set("blue")

def usePencil():
    stroke_color.set("black")
    # usePencil.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
    # pencilIcon["bordercolor"] = "blue"
    #canvas['cursor'] = tk.MOUSE

def useEraser():
    stroke_color.set("white")
    canvas['cursor'] = tk.DOTBOX

def addText():
    add_text_window()
    
# ------------------------------------------Tool-Functionality-Section-Close----------------------------------------------------------+


# ------------------------------------------Menu-Section-Open----------------------------------------------------------+
# The Menu Bar Will Contain Important Stuff Like File , Help , Edit , Undo , Redo , Setting Bar And Etc

menuFrame = tk.Frame(frameOne , height=30 , width=1280 , bg="#FF9578")
menuFrame.place(x=0,y=0)

# ------------------------------------------Menu-Section-Close----------------------------------------------------------+

#-------------------------------------------Save-Image-Frame-Open--------------------------------------------------------------------+
# Contains The Save Button Details
saveImageFrame=tk.Frame(frameOne , height=30, width=85 , borderwidth=0 ,relief="sunken",bg="#FF9578")
saveImageFrame.place(x=0,y=0)

saveImageFrame= Button(frameOne , text="Save" , width=10, highlightthickness=0 , relief="flat",bg="#FF9578" , activebackground="#FF9578")
saveImageFrame.place(x=2, y=2)

#-------------------------------------------Save-Image-Frame-Close--------------------------------------------------------------------+

#-------------------------------------------Clear-image-Frame-Open------------------------------------------------------------------------+
# The Clear All Button Details
def clear() :
    if messagebox.askokcancel("Warning!", "Do you want to clear everything?"):
        canvas.delete('all')

clearImageFrame=tk.Frame(frameOne , height=30, width=110 , borderwidth=0 ,relief="sunken",bg="#FF9578")
clearImageFrame.place(x=85,y=0)

clearImageFrame= Button(frameOne , text="Clear All" , width=14, command=clear, highlightthickness=0 , relief="flat" ,bg="#FF9578" , activebackground="#FF9578")
clearImageFrame.place(x=87, y=1)
#-------------------------------------------Clear-image-Frame-Close------------------------------------------------------------------------+

#-------------------------------------------New-Window-Open------------------------------------------------------------------------+
def help_window():
    new_window = tk.Toplevel(window)
    new_window.title("Help")
    new_window.geometry("400x600")
    label = tk.Label(new_window, text="This is a Help Window")
    label.pack(pady=20)

def aboutus_window():
    new_window = tk.Toplevel(window)
    new_window.title("About Us")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="This is a new window")
    label.pack(pady=20)

def setting_window():
    new_window = tk.Toplevel(window)
    new_window.title("Setting")
    new_window.geometry("700x400")
    label = tk.Label(new_window, text="This is a new window")
    label.pack(pady=20)

def add_text_window():
    new_window = tk.Toplevel(window)
    new_window.title("Add Text To Canvas")
    new_window.geometry("600x300")
    label = tk.Label(new_window, text="Enter The Text You Want To Display :")
    label.pack(pady=20)

    global entry
    entry = tk.Entry(new_window)
    entry.place(x = 130, y = 80)
    btn = tk.Button(new_window , text="Add" , command= printt  , width = 5, height = 1)
    btn.place(x = 170 , y = 120)

    # Sliders for X and Y position
    global x_slider , y_slider
    x_slider = tk.Scale(new_window, from_=0, to=1280, orient="horizontal", label="X Position")
    x_slider.set(200)  # default center
    x_slider.place(x = 350 , y = 50)

    y_slider = tk.Scale(new_window, from_=0, to=800, orient="vertical", label="Y Position")
    y_slider.set(125)
    y_slider.place(x = 350 , y = 150)
#-------------------------------------------New-Window-Close------------------------------------------------------------------------+

#--------------------------------------------Help-setting-Frame-Open------------------------------------------------------------------------------+
# The Help Button Details
HelpSettingFrame=tk.Frame(frameOne , height=30, width=240 , borderwidth=0 ,relief="sunken",bg="white")
HelpSettingFrame.place(x=850,y=0)

Help= Button(HelpSettingFrame , text="Help" , width=10, highlightthickness=0 , relief="flat",bg="#FF9578" , activebackground="#FF9578" , command=help_window)
Help.grid(row=0, column=0)

Setting= Button(HelpSettingFrame , text="Setting" , width=10, highlightthickness=0 , relief="flat",bg="#FF9578" , activebackground="#FF9578",command=setting_window)
Setting.grid(row=0, column=1)

About= Button(HelpSettingFrame , text="About us" , width=10, highlightthickness=0 , relief="flat",bg="#FF9578" , activebackground="#FF9578",command=aboutus_window)
About.grid(row=0, column=2)

#--------------------------------------------Help-Setting-Frame-Close-----------------------------------------------------------------------------+

# ----------------------------------------------------------------------------------------------------+
# Tool Frame Which Will Contain All The Required Tools etc - pencil , eraser , color
toolFrame = tk.Frame(frameOne , height=120 , width=120 , bg="#D6F5EF", highlightthickness=0 , relief="flat" )
toolFrame.place(x = 20  , y = 50 )

#Pencil Button/Icon -> Onclicking The Button The User Can Use The Pencil
pencilIcon = tk.Button(toolFrame ,  width=20 , height=20 , image= iconOfPencil , command=usePencil, highlightthickness=0 , relief="flat" )
pencilIcon.place(x = 5 , y = 5 )

# Rubber Button/Icon
eraserIcon = tk.Button(toolFrame , width=20, height=20 , image=iconOfEraser , command= useEraser, highlightthickness=0 , relief="flat")
eraserIcon.place(x = 5 , y = 40)

# Font Icon
fontIcon = tk.Button(toolFrame , width=20, height=20 , image=iconOfFont, highlightthickness=0,command= addText , relief="flat")
fontIcon.place(x = 40 , y = 5)

# Glass Icon
glassIcon = tk.Button(toolFrame , width=20, height=20 , image=iconOfGlass, highlightthickness=0 , relief="flat")
glassIcon.place(x = 40 , y = 40)

# Fill Icon
fillIcon = tk.Button(toolFrame , width=20, height=20 , image=iconOfFill, highlightthickness=0 , relief="flat")
fillIcon.place(x=80, y = 5)

# One More Icon keep x = 80 and y = 40

# ToolLabel
toolLabel = tk.Label(toolFrame , text="Tool Bar" , width=25 , bg="#D6F5EF")
toolLabel.place(x=-30 , y= 80)

# ----------------------------------------------------------------------------------------------------
# Addind Borders Along The Different Tools
border_frame_one = tk.Frame(frameOne , width=2 , height= 100 , bg="black")
border_frame_one.place(x = 160 , y = 50)

border_frame_two = tk.Frame(frameOne , width=2 , height= 100 , bg="black")
border_frame_two.place(x = 400 , y = 50)

border_frame_three = tk.Frame(frameOne , width=2 , height= 100 , bg="black")
border_frame_three.place(x = 690 , y = 50)
# ----------------------------------------------------------------------------------------------------
# Implementing Scale For Pencil Stroke Size So That The User Can Use The Scale To Increase The Size Of The Pencil And Eraser Stroke
stroke_size = tk.IntVar(value = 5)

scale = tk.Scale(frameOne , from_=1, to=20 , orient="horizontal" , length=200 , bg="#D6F5EF" , background="#D6F5EF" ,troughcolor="#706D68",variable=stroke_size , highlightthickness=0)
scale.place(x = 180 ,y = 50)

scale_label = tk.Label(frameOne , text="Pencil & Eraser Size", bg="#D6F5EF")
scale_label.place(x=220 , y=130)

# ----------------------------------------------------------------------------------------------------
# The Canvas Frame Where The User Can Draw Things
canvas = tk.Canvas(frameTwo , width=1280 , height=800 , bg="white")
canvas.grid(row=0,column=0)
# ----------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------
#Creating Pencil Functionality For The Paint Program
prevPoint = [0,0]
currentPoint = [0,0]

def paint(event):
    # print(event.type)
    global prevPoint
    global currentPoint
    x = event.x
    y = event.y
    currentPoint =[x,y]

    if prevPoint != [0,0]:
        canvas.create_line(prevPoint[0] , prevPoint[1] , currentPoint[0] , currentPoint[1] ,fill=stroke_color.get() , width=stroke_size.get())
            
    prevPoint = currentPoint 

    if event.type == "5":
        prevPoint = [0,0]   

canvas.bind("<B1-Motion>" , paint)
canvas.bind("<ButtonRelease-1>",paint)

def printt():
    entered_text = entry.get()
    x_pos_text = x_slider.get()
    y_pos_text = y_slider.get()

    canvas.create_text(x_pos_text, y_pos_text, text=entered_text, font=("Arial", 16), fill="black", tags="text")
# canvas.create_line(100,100,200,300)
# canvas.create_rectangle(220,200,400,300)

# ----------------------------------------------------------------------------------------------------

window.mainloop()
