import tkinter as tk
from tkinter import colorchooser, messagebox

# ------------------------------------------- Setup ------------------------------------------- #
window = tk.Tk()
window.geometry("1100x500")
window.title("Painting Window Version 10")

stroke_color = tk.StringVar()
stroke_size = tk.IntVar(value=5)

# ------------------------------------------- Frames ------------------------------------------- #
frameOne = tk.Frame(window, bg="#D6F5EF", width=1280, height=170)
frameOne.grid(row=0, column=0, sticky="nw")

frameTwo = tk.Frame(window, bg="yellow", width=1280, height=800)
frameTwo.grid(row=1, column=0)

menuFrame = tk.Frame(frameOne, height=30, width=1280, bg="#FF9578")
menuFrame.place(x=0, y=0)

canvas = tk.Canvas(frameTwo, width=1280, height=800, bg="white")
canvas.grid(row=0, column=0)

# ------------------------------------------- Icons ------------------------------------------- #
iconOfPencil = tk.PhotoImage(file="Icons/Small_Pencil.png")
iconOfEraser = tk.PhotoImage(file="Icons/Small_Eraser.png")
iconOfFont = tk.PhotoImage(file="Icons/Small_Font.png")
iconOfGlass = tk.PhotoImage(file="Icons/Small_Glass.png")
iconOfFill = tk.PhotoImage(file="Icons/Small_Fill.png")
iconOfSelectColor = tk.PhotoImage(file="Icons/Small_MoreColorsWithPlus.png")

# ------------------------------------------- Color Picker ------------------------------------------- #
def select_color():
    color = colorchooser.askcolor(title="Select Color")
    if color[1]:
        stroke_color.set(color[1])

colorBoxButton = tk.Button(frameOne, image=iconOfSelectColor, command=select_color, bg="#D6F5EF",
                           activebackground="#D6F5EF", relief="flat", bd=0, highlightthickness=0)
colorBoxButton.place(x=610, y=60)

# ------------------------------------------- Color Buttons ------------------------------------------- #
def create_color_buttons(parent):
    colors = [
        ("Red", 0, 0), ("Green", 0, 1), ("Blue", 0, 2), ("Yellow", 0, 3), ("Grey", 0, 4),
        ("Black", 1, 0), ("White", 1, 1), ("Orange", 1, 2), ("Purple", 1, 3), ("Pink", 1, 4)
    ]
    for color, row, col in colors:
        btn = tk.Button(parent, bg=color, width=3, height=1, relief="flat", bd=0,
                        activebackground=color, highlightthickness=0,
                        fg="white" if color.lower() == "black" else "black",
                        command=lambda c=color: stroke_color.set(c))
        btn.grid(row=row, column=col, padx=5, pady=5)

colorFrame = tk.Frame(frameOne, width=230, height=120, bg="#D6F5EF")
colorFrame.place(x=415, y=55)
create_color_buttons(colorFrame)

# ------------------------------------------- Tool Functions ------------------------------------------- #
def use_pencil():
    stroke_color.set("black")

def use_eraser():
    stroke_color.set("white")
    canvas['cursor'] = tk.DOTBOX

def print_text():
    entered_text = entry.get()
    x, y = x_slider.get(), y_slider.get()
    textofentry.set("")
    canvas.create_text(x, y, text=entered_text, font=("Arial", 16), fill="black")

def clear_canvas():
    if messagebox.askokcancel("Warning!", "Do you want to clear everything?"):
        canvas.delete('all')

# ------------------------------------------- Tool Icons ------------------------------------------- #
def create_tool_icons():
    toolFrame = tk.Frame(frameOne, bg="#D6F5EF", width=120, height=120)
    toolFrame.place(x=20, y=50)

    tools = [
        (iconOfPencil, use_pencil, 5, 5),
        (iconOfEraser, use_eraser, 5, 40),
        (iconOfFont, add_text_window, 40, 5),
        (iconOfGlass, None, 40, 40),
        (iconOfFill, None, 80, 5)
    ]
    for icon, cmd, x, y in tools:
        tk.Button(toolFrame, image=icon, command=cmd, relief="flat", bd=0,
                  highlightthickness=0, width=20, height=20).place(x=x, y=y)

    tk.Label(toolFrame, text="Tool Bar", bg="#D6F5EF", width=25).place(x=-30, y=80)

create_tool_icons()

# ------------------------------------------- Save & Clear Buttons ------------------------------------------- #
tk.Button(frameOne, text="Save", width=10, bg="#FF9578", activebackground="#FF9578",
          relief="flat", highlightthickness=0).place(x=2, y=2)

tk.Button(frameOne, text="Clear All", width=14, command=clear_canvas,
          bg="#FF9578", activebackground="#FF9578", relief="flat", highlightthickness=0).place(x=87, y=1)

# ------------------------------------------- Stroke Size Scale ------------------------------------------- #
tk.Scale(frameOne, from_=1, to=20, orient="horizontal", variable=stroke_size, length=200,
         bg="#D6F5EF", troughcolor="#706D68", highlightthickness=0).place(x=180, y=50)
tk.Label(frameOne, text="Pencil & Eraser Size", bg="#D6F5EF").place(x=220, y=130)

# ------------------------------------------- Help, Setting, About ------------------------------------------- #
def show_popup(title, msg="This is a new window", size="300x200"):
    new_win = tk.Toplevel(window)
    new_win.title(title)
    new_win.geometry(size)
    tk.Label(new_win, text=msg).pack(pady=20)

help_frame = tk.Frame(frameOne, width=240, height=30, bg="white")
help_frame.place(x=850, y=0)

tk.Button(help_frame, text="Help", width=10, bg="#FF9578", command=lambda: show_popup("Help", "This is a Help Window"),
          relief="flat", highlightthickness=0).grid(row=0, column=0)
tk.Button(help_frame, text="Setting", width=10, bg="#FF9578", command=lambda: show_popup("Setting", size="700x400"),
          relief="flat", highlightthickness=0).grid(row=0, column=1)
tk.Button(help_frame, text="About Us", width=10, bg="#FF9578", command=lambda: show_popup("About Us"),
          relief="flat", highlightthickness=0).grid(row=0, column=2)

# ------------------------------------------- Add Text Window ------------------------------------------- #
def add_text_window():
    global textofentry, entry, x_slider, y_slider
    new_window = tk.Toplevel(window)
    new_window.title("Add Text To Canvas")
    new_window.geometry("600x300")

    tk.Label(new_window, text="Enter The Text You Want To Display :").pack(pady=20)

    textofentry = tk.StringVar(value="Enter Here")
    entry = tk.Entry(new_window, textvariable=textofentry, font=("Arial", 10), width=50, justify="center")
    entry.place(x=100, y=80)

    tk.Button(new_window, text="Add", command=print_text, width=10, height=2).place(x=250, y=120)

    x_slider = tk.Scale(new_window, from_=0, to=1280, orient="horizontal", label="X Position", length=200)
    x_slider.set(200)
    x_slider.place(x=50, y=200)

    y_slider = tk.Scale(new_window, from_=0, to=800, orient="horizontal", label="Y Position", length=200)
    y_slider.set(125)
    y_slider.place(x=350, y=200)

# ------------------------------------------- Drawing Logic ------------------------------------------- #
prev_point = [0, 0]

def paint(event):
    global prev_point
    if prev_point != [0, 0]:
        canvas.create_line(prev_point[0], prev_point[1], event.x, event.y,
                           fill=stroke_color.get(), width=stroke_size.get())
    prev_point = [event.x, event.y]
    if event.type == "5":
        prev_point = [0, 0]

canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)

# ------------------------------------------- Main Loop ------------------------------------------- #
window.mainloop()
