
# -*- coding: utf8 -*-
import sys
import tkinter as tk
import tkinter.messagebox as msgbox
import webbrowser
import const
import todos

vals  = [] # Object for verifying if box is checked
boxes = [] # Checkbox components
links = [] # Buttons of links

# ----- Functions -----
def check(event):
    sum = 0
    for i in range(const.SET_MAX):
        if vals[i].get(): sum += 1
    if sum < const.SET_MAX: msgbox.showerror(const.DLG_TITLE, const.DLG_MSG)
    else: return

def callback(i):
    webbrowser.open_new(links[i])

# ----- Setup -----
root = tk.Tk()                 # GUI Service
root.title(const.WINDOW_TITLE)   # Title
root.geometry(const.SCREEN_SIZE) # Window

# ----- Checkbox -----
# Create object
for i in range(const.SET_MAX):
    vals.append(tk.BooleanVar())
# Set initial state
for v in vals:
    v.set(False)
# Create components
for i in range(const.SET_MAX):
    boxes.append(tk.Checkbutton(text=todos.getTodos()[0],
            font=(const.FONT_STYLE, const.FONT_SIZE), variable=vals[i]).place(x = 10, y = i*30))

# ----- Button -----
# Link
links = todos.getLinks()
for i in range(const.SET_MAX):
    link = tk.Button(root, text=const.LINK, width=10, font=(const.FONT_STYLE, const.FONT_SIZE))
    # TODO Get url from external file
    link.bind('<Button-1>', callback(i))
    link.place(x = 300, y = i*30)
    # links.append(link)

# Confirm
confirm = tk.Button(root, text=const.CONFIRM, width=10, font=(const.FONT_STYLE, const.FONT_SIZE), command=root.destroy)
confirm.bind('<Button-1>', check)
confirm.place(x = 150, y = 160)

root.mainloop()