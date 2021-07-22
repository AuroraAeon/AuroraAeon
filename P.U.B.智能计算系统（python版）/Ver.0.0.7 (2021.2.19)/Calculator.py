# name:   P.U.B.智能计算系统
# author: Thomas·P , 李俊熠
# date:   2021.2.20
# version:0.0.8
from tkinter import Label, Button, Tk, Toplevel, Menu
from tkinter.ttk import Treeview
from time import sleep

root = Tk()
root.title("P.U.B.智能计算系统")
root.geometry("990x540+415+270")
root.resizable(False, False)


def messagebox_quit():
    quit_assure = Toplevel()
    quit_assure.geometry("200x100+890+490")
    quit_assure.resizable(False, False)
    quit_assure.overrideredirect(True)
    assure = Label(quit_assure, text="你确定要退出吗？")
    assure.pack(side="top", anchor="n")
    quit_assure.wm_attributes('-topmost', True)
    yes = Button(quit_assure, text="确定", command=root.quit)
    yes.place(x=25,y=50)
    nope = Button(quit_assure, text="取消", command=quit)
    nope.place(x=150,y=50)

def sub():
    new = Toplevel(root)


def click():
    def select(event):
        item=contents.selection()[0]
        if item==T_A_1:
            sub()
        
    start=Label(root, text="欢迎来到P.U.B.智能计算系统！", font=("宋体", "20"))
    start.pack(side="top")
    button.destroy()
    root.update()
    sleep(1)

    start.config(text="功能目录", font=("仿宋", "15"))
    contents=Treeview(root, selectmode="browse", show="tree")
    contents.pack(fill="both")
    T_A = contents.insert("", 0, text="代数计算")
    T_A_1 = contents.insert(T_A, 0, text="高级计算器")
    contents.insert(T_A, 1, text="方程计算器")
    T_B = contents.insert("", 1, text="几何计算")
    contents.insert(T_B, 0, text="平面计算")
    contents.insert(T_B, 1, text="立体计算")
    contents.bind("<Double-Button-1>", select)


button = Button(root, text="点击按钮启动智能计算系统", font=('仿宋', '20'), command=click, relief="groove")
button.pack(expand=True)
menu = Menu(root)
for item in ("语言", "关于", "反馈"):
    menu.add_command(label=item)
menu.add_command(label="退出", command=messagebox_quit)
root.config(menu=menu)

root.mainloop()
