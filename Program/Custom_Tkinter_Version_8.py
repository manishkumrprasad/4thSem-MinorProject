import customtkinter as ctk
from tkinter import colorchooser, PhotoImage, messagebox

ctk.set_appearance_mode("light")  # or "dark"
ctk.set_default_color_theme("blue")

# Window
window = ctk.CTk()
window.geometry("1100x500")
window.title("Painting Window Version 8")
# window.resizable(False, False)

# Global color and stroke
stroke_color = ctk.StringVar(value="black")
stroke_size = ctk.IntVar(value=5)

# --------------------------------- Frames ---------------------------------
frameOne = ctk.CTkFrame(window, fg_color="#D6F5EF", width=1280, height=170, corner_radius=0)
frameOne.grid(row=0, column=0, sticky="nw")

frameTwo = ctk.CTkFrame(window, fg_color="yellow", width=1280, height=800, corner_radius=0)
frameTwo.grid(row=1, column=0)

# --------------------------------- Icons ---------------------------------
iconOfPencil = PhotoImage(file="Icons/Small_Pencil.png")
iconOfEraser = PhotoImage(file="Icons/Small_Eraser.png")
iconOfFont = PhotoImage(file="Icons/Small_Font.png")
iconOfGlass = PhotoImage(file="Icons/Small_Glass.png")
iconOfFill = PhotoImage(file="Icons/Small_Fill.png")
iconOfSelectColor = PhotoImage(file="Icons/Small_morecolors.png")

# --------------------------------- Color Picker ---------------------------------
def selectcolor():
    selected = colorchooser.askcolor(title="Select Color")[1]
    if selected:
        stroke_color.set(selected)

colorBoxButton = ctk.CTkButton(frameOne, width=40, height=40, image=iconOfSelectColor, text="", command=selectcolor, fg_color="#D6F5EF", hover=False)
colorBoxButton.place(x=420, y=70)

# --------------------------------- Color Buttons ---------------------------------
colorFrame = ctk.CTkFrame(frameOne, fg_color="#D6F5EF", width=230, height=120, corner_radius=0)
colorFrame.place(x=490, y=55)

def create_color_btn(color, row, col):
    return ctk.CTkButton(colorFrame, width=20, height=20, text="", fg_color=color, command=lambda: stroke_color.set(color)).grid(row=row, column=col, padx=5, pady=5)

colors = [["Red", "Green", "Blue", "Yellow"], ["Black", "White", "Orange", "Purple"]]
for r, row in enumerate(colors):
    for c, color in enumerate(row):
        create_color_btn(color, r, c)

# --------------------------------- Menu Buttons ---------------------------------
def clear():
    if messagebox.askokcancel("Warning!", "Do you want to clear everything?"):
        canvas.delete("all")

ctk.CTkButton(frameOne, text="Save", width=70).place(x=2, y=2)
ctk.CTkButton(frameOne, text="Clear All", width=100, command=clear).place(x=87, y=1)

help_frame = ctk.CTkFrame(frameOne, fg_color="#FF9578", width=300, height=30, corner_radius=0)
help_frame.place(x=850, y=0)

ctk.CTkButton(help_frame, text="Help", width=80).grid(row=0, column=0)
ctk.CTkButton(help_frame, text="Setting", width=80).grid(row=0, column=1)
ctk.CTkButton(help_frame, text="About Us", width=80).grid(row=0, column=2)

# --------------------------------- Tool Icons ---------------------------------
def usePencil():
    stroke_color.set("black")

def useEraser():
    stroke_color.set("white")
    canvas.configure(cursor="dotbox")

toolFrame = ctk.CTkFrame(frameOne, fg_color="#D6F5EF", width=120, height=120, corner_radius=0)
toolFrame.place(x=20, y=50)

ctk.CTkButton(toolFrame, image=iconOfPencil, text="", width=20, height=20, command=usePencil).place(x=5, y=5)
ctk.CTkButton(toolFrame, image=iconOfEraser, text="", width=20, height=20, command=useEraser).place(x=5, y=40)
ctk.CTkButton(toolFrame, image=iconOfFont, text="", width=20, height=20).place(x=40, y=5)
ctk.CTkButton(toolFrame, image=iconOfGlass, text="", width=20, height=20).place(x=40, y=40)
ctk.CTkButton(toolFrame, image=iconOfFill, text="", width=20, height=20).place(x=80, y=5)

ctk.CTkLabel(toolFrame, text="Tool Bar", width=100, text_color="black").place(x=0, y=80)

# --------------------------------- Scale ---------------------------------
scale = ctk.CTkSlider(frameOne, from_=1, to=20, variable=stroke_size, width=200)
scale.place(x=180, y=50)

ctk.CTkLabel(frameOne, text="Pencil & Eraser Size", text_color="black").place(x=220, y=130)

# --------------------------------- Canvas ---------------------------------
canvas = ctk.CTkCanvas(frameTwo, width=1280, height=800, bg="white", highlightthickness=0)
canvas.grid(row=0, column=0)

# Drawing Logic
prevPoint = [0, 0]

def paint(event):
    global prevPoint
    x, y = event.x, event.y
    if prevPoint != [0, 0]:
        canvas.create_line(prevPoint[0], prevPoint[1], x, y, fill=stroke_color.get(), width=stroke_size.get())
    prevPoint = [x, y]
    if event.type == tk.EventType.ButtonRelease:
        prevPoint = [0, 0]

canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)

# --------------------------------- Run ---------------------------------
window.mainloop()
