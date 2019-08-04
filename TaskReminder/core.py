# coding: utf-8
import sys
import tkinter as tk
import tkinter.messagebox as msgbox
import webbrowser
import const
import todos

vals  = []   # チェックボックスのON/OF
boxes = []   # チェックボックス
buttons = [] # リンクボタン

# 初期設定
root = tk.Tk()                   # tkinter
root.title(const.WINDOW_TITLE)   # タイトル
root.geometry(const.SCREEN_SIZE) # 画面

# すべてのタスクが完了しているか確認
def check(msg):
    def x():
        sum = 0
        for i in range(len(todos.getTodos())):
            if vals[i].get(): sum += 1
        if sum < len(todos.getTodos()):
            msgbox.showerror(const.DLG_TITLE, msg)
        else:
            root.destroy()
    return x

# クリックイベント
def clicked(url):
    def x():
       webbrowser.open_new(url)
    return x

# チェックボックス
for i in range(const.SET_MAX):
    vals.append(tk.BooleanVar())
    vals[i].set(False)

labels = todos.getTodos()
for i in range(len(labels)):
    b = tk.Checkbutton(
            text = labels[i],
            font = (const.FONT_STYLE, const.FONT_SIZE),
            variable = vals[i],
            height = 2
        )
    b.place(x = 10, y = i*30)
    boxes.append(b)

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
        buttons[i].place(x=300, y=i*30)
    else:
        buttons.append('Enpty')

# 確認ボタン
confirm = tk.Button(
    root,
    text = const.CONFIRM,
    width=10,
    font = (const.FONT_STYLE, const.FONT_SIZE),
    command = check(const.DLG_CONFIRM_MSG)
)
confirm.place(x = 150, y = 160)

root.protocol('WM_DELETE_WINDOW', check(const.DLG_CLOSING_MSG))

root.mainloop()