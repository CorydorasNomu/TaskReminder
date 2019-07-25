
# -*- coding: utf8 -*-
import sys
import tkinter as tk
import tkinter.messagebox as msgbox
import webbrowser
import config as cfg

vals  = [] # Object for verifying if box is checked
boxes = [] # Checkbox components
links = [] # Buttons of links

# ----- Functions -----
def check(event):
    sum = 0
    for i in range(cfg.SET_MAX):
        if vals[i].get(): sum += 1
    if sum < cfg.SET_MAX: msgbox.showerror(cfg.DLG_TITLE, cfg.DLG_MSG)
    else: return

# TODO Insert url from external file
def callback(url):
    print(url)
    webbrowser.open_new(r'https://www.google.co.jp')

# ----- Setup -----
root = tk.Tk()                 # GUI Service
root.title(cfg.WINDOW_TITLE)   # Title
root.geometry(cfg.SCREEN_SIZE) # Window

# ----- Checkbox -----
# Create object
for i in range(cfg.SET_MAX):
    vals.append(tk.BooleanVar())
# Set initial state
for v in vals:
    v.set(False)
# Create components
for i in range(cfg.SET_MAX):
    boxes.append(tk.Checkbutton(text=u'Import from external file',
            font=(cfg.FONT_STYLE, cfg.FONT_SIZE), variable=vals[i]).place(x = 10, y = i*30))

# ----- Button -----
# Link
for i in range(cfg.SET_MAX):
    link = tk.Button(root, text=cfg.LINK, width=10, font=(cfg.FONT_STYLE, cfg.FONT_SIZE))
    # TODO Get url from external file
    link.bind('<Button-1>', callback('url'))
    link.place(x = 300, y = i*30)
    links.append(link)

# Confirm
confirm = tk.Button(root, text=cfg.CONFIRM, width=10, font=(cfg.FONT_STYLE, cfg.FONT_SIZE), command=root.destroy)
confirm.bind('<Button-1>', check)
confirm.place(x = 150, y = 160)

root.mainloop()