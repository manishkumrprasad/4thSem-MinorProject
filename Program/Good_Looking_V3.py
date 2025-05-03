import tkinter as tk

window = tk.Tk()
window.geometry("1100x500")
window.title("Painting Window Version 3")
window.resizable(False,False)

# ----------------------------------------------------------------------------------------------------

# Parent Paint Toolbars / Which Will Contain All The Tools Frame Such As toolbar , color pallette , file management , help box etc
frameOne = tk.Frame(window , bg="#D6F5EF" , width=1100,height=120)
frameOne.grid(row=0 , column=0 , sticky=tk.NW)

# Parent Paint Frame Which Contain Only The Canvas Frame
frameTwo = tk.Frame(window , bg="yellow" , width=1100,height=380)
frameTwo.grid(row=1 , column=0)

# ----------------------------------------------------------------------------------------------------+

# ------------------------------------------Icon-Section-Open----------------------------------------------------------+

#The Ico Section Contains All The Icon That Are Going To Be Used Throughout The Program  
iconOfPencil = tk.PhotoImage(file="Icons/Small_Pencil.png")
iconOfEraser = tk.PhotoImage(file="Icons/Small_Eraser.png")
iconOfFont = tk.PhotoImage(file="Icons/Small_Font.png")
iconOfGlass = tk.PhotoImage(file="Icons/Small_Glass.png")
iconOfFill = tk.PhotoImage(file="Icons/Small_Fill.png")

# ------------------------------------------Icon-Section-Close----------------------------------------------------------+


# ----------------------------------------------------------------------------------------------------+

# Tool Frame Which Will Contain All The Required Tools etc - pencil , eraser , color
toolFrame = tk.Frame(frameOne , height=100 , width=120 , bg="#DBDBDB")
toolFrame.place(x = 20  , y = 10 )

#Pencil Button/Icon -> Onclicking The Button The User Can Use The Pencil
pencilIcon = tk.Button(toolFrame ,  width=20 , height=20 , image= iconOfPencil )
pencilIcon.place(x = 5 , y = 5 )

# Rubber Button/Icon
eraserIcon = tk.Button(toolFrame , width=20, height=20 , image=iconOfEraser)
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
toolLabel = tk.Label(toolFrame , text="Tools" , width=25 )
toolLabel.place(x=-30 , y= 80)


# ----------------------------------------------------------------------------------------------------

# The Canvas Frame Where The User Can Draw Things
canvas = tk.Canvas(frameTwo , height=380 , width=1100 , bg="white")
canvas.grid(row=0,column=0)

# ----------------------------------------------------------------------------------------------------
# ------------------------------------------Eraser-Section-Open----------------------------------------------------------+

stroke_color = tk.StringVar()
stroke_color.set("blue")

# ------------------------------------------Eraser-Section-Close----------------------------------------------------------+

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
        canvas.create_line(prevPoint[0] , prevPoint[1] , currentPoint[0] , currentPoint[1] , fill=stroke_color.get())
        #The Fill field can be used to change the color of the line
    prevPoint = currentPoint 

    if event.type == "5":
        prevPoint = [0,0]   

canvas.bind("<B1-Motion>" , paint)
canvas.bind("<ButtonRelease-1>",paint)

# canvas.create_line(100,100,200,300)
# canvas.create_rectangle(220,200,400,300)

# ----------------------------------------------------------------------------------------------------

window.mainloop()