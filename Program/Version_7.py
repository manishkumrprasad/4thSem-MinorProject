import tkinter as tk

window = tk.Tk()
window.geometry("1100x500")
window.title("Painting Window Version 7")

# ------------------------------------------Parent-Frame-Section-Open----------------------------------------------------------+

# Parent Paint Toolbars / Which Will Contain All The Tools Frame Such As toolbar , color pallette , file management , help box etc
frameOne = tk.Frame(window , bg="#D6F5EF" , width=1280,height=170)
frameOne.grid(row=0 , column=0 , sticky=tk.NW)

# Parent Paint Frame Which Contain Only The Canvas Frame
frameTwo = tk.Frame(window , bg="yellow" , width=1280,height=800)
frameTwo.grid(row=1 , column=0)

# ------------------------------------------Parent-Frame-Section-Close----------------------------------------------------------+


# ------------------------------------------Icon-Section-Open----------------------------------------------------------+

#The Ico Section Contains All The Icon That Are Going To Be Used Throughout The Program  
iconOfPencil = tk.PhotoImage(file="Icons/Small_Pencil.png")
iconOfEraser = tk.PhotoImage(file="Icons/Small_Eraser.png")
iconOfFont = tk.PhotoImage(file="Icons/Small_Font.png")
iconOfGlass = tk.PhotoImage(file="Icons/Small_Glass.png")
iconOfFill = tk.PhotoImage(file="Icons/Small_Fill.png")

# ------------------------------------------Icon-Section-Close----------------------------------------------------------+


# ------------------------------------------Menu-Section-Open----------------------------------------------------------+
# The Menu Bar Will Contain Important Stuff Like File , Help , Edit , Undo , Redo , Setting Bar And Etc

menuFrame = tk.Frame(frameOne , height=30 , width=1280 , bg="#FF9578")
menuFrame.place(x=0,y=0)

# ------------------------------------------Menu-Section-Close----------------------------------------------------------+

# ------------------------------------------Tool-Functionality-Section-Open----------------------------------------------------------+
stroke_color = tk.StringVar()
# stroke_color.set("blue")

def usePencil():
    stroke_color.set("black")
    # canvas['cursor'] = tk.ROUND

def useEraser():
    stroke_color.set("white")
    canvas['cursor'] = tk.DOTBOX
# ------------------------------------------Tool-Functionality-Section-Close----------------------------------------------------------+

# ----------------------------------------------------------------------------------------------------+

# Tool Frame Which Will Contain All The Required Tools etc - pencil , eraser , color
toolFrame = tk.Frame(frameOne , height=120 , width=120 , bg="#D6F5EF" )
toolFrame.place(x = 20  , y = 50 )

#Pencil Button/Icon -> Onclicking The Button The User Can Use The Pencil
pencilIcon = tk.Button(toolFrame ,  width=20 , height=20 , image= iconOfPencil , command=usePencil )
pencilIcon.place(x = 5 , y = 5 )

# Rubber Button/Icon
eraserIcon = tk.Button(toolFrame , width=20, height=20 , image=iconOfEraser , command= useEraser)
eraserIcon.place(x = 5 , y = 40)

# Font Icon
fontIcon = tk.Button(toolFrame , width=20, height=20 , image=iconOfFont)
fontIcon.place(x = 40 , y = 5)

# Glass Icon
glassIcon = tk.Button(toolFrame , width=20, height=20 , image=iconOfGlass)
glassIcon.place(x = 40 , y = 40)

# Fill Icon
fillIcon = tk.Button(toolFrame , width=20, height=20 , image=iconOfFill)
fillIcon.place(x=80, y = 5)

# One More Icon keep x = 80 and y = 40

# ToolLabel
toolLabel = tk.Label(toolFrame , text="Tool Bar" , width=25 , bg="#D6F5EF")
toolLabel.place(x=-30 , y= 80)

# ----------------------------------------------------------------------------------------------------

border_frame = tk.Frame(frameOne , width=2 , height= 100 , bg="black")
border_frame.place(x = 160 , y = 50)

# ----------------------------------------------------------------------------------------------------
# Implementing Scale For Pencil Stroke Size So That The User Can Use The Scale To Increase The Size Of The Pencil And Eraser Stroke

stroke_size = tk.IntVar(value = 5)

scale = tk.Scale(frameOne , from_=1, to=70 , orient="horizontal" , length=200 , bg="#D6F5EF" , background="#D6F5EF" ,variable=stroke_size)
scale.place(x = 180 ,y = 50)

scale_label = tk.Label(frameOne , text="Pencil & Eraser Size", bg="#D6F5EF")
scale_label.place(x=220 , y=130)

# ----------------------------------------------------------------------------------------------------

# The Canvas Frame Where The User Can Draw Things
canvas = tk.Canvas(frameTwo , width=1280 , height=800 , bg="white")
canvas.grid(row=0,column=0)

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
    # canvas.create_oval(x,y,x+5,y+5, fill="black")

    if prevPoint != [0,0]:
        canvas.create_line(prevPoint[0] , prevPoint[1] , currentPoint[0] , currentPoint[1] ,fill=stroke_color.get() , width=stroke_size.get())

    prevPoint = currentPoint 

    if event.type == "5":
        prevPoint = [0,0]   

canvas.bind("<B1-Motion>" , paint)
canvas.bind("<ButtonRelease-1>",paint)

# canvas.create_line(100,100,200,300)
# canvas.create_rectangle(220,200,400,300)

# ----------------------------------------------------------------------------------------------------

window.mainloop()