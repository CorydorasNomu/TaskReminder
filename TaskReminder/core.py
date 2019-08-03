# coding: utf-8
import sys
import tkinter as tk
import tkinter.messagebox as msgbox
import webbrowser
import const
import todos

vals  = [] # Object for verifying if box is checked
boxes = [] # Checkbox components
buttons = []

# すべてのTODO項目が完了しているかを確認
def check(event):
    sum = 0
    for i in range(len(todos.getTodos())):
        if vals[i].get(): sum += 1
    if sum < len(todos.getTodos()): msgbox.showerror(const.DLG_TITLE, const.DLG_MSG)
    else: return

# クリックイベント
def clicked(url):
    def x():
       webbrowser.open_new(url)
    return x

# 初期設定
root = tk.Tk()                   # tkinter
root.title(const.WINDOW_TITLE)   # タイトル
root.geometry(const.SCREEN_SIZE) # 画面

# チェックボックス
for i in range(const.SET_MAX):
    vals.append(tk.BooleanVar())
    vals[i].set(False)

labels = todos.getTodos()
for i in range(len(labels)):
    print(labels[i])
    boxes.append(tk.Checkbutton(
            text = labels[i],
            font = (const.FONT_STYLE, const.FONT_SIZE),
            variable = vals[i],
            height = 2
        ).place(x = 10, y = i*30))

# リンクボタン
links = todos.getLinks()
for i in range(len(links)):
    if ':' in links[i]:
        link = tk.Button(
                root,
                text = const.LINK,
                width = 10,
                font = (const.FONT_STYLE, const.FONT_SIZE),
                command = clicked(links[i])
            )
        buttons.append(link)
        buttons[i].pack()
        buttons[i].place(x=300, y=i*30)
    else:
        buttons.append('Enpty')

# 確認ボタン
confirm = tk.Button(
    root,
    text = const.CONFIRM,
    width=10,
    font = (const.FONT_STYLE, const.FONT_SIZE),
    command=root.destroy
)
confirm.bind('<Button-1>', check)
confirm.place(x = 150, y = 160)

root.mainloop()