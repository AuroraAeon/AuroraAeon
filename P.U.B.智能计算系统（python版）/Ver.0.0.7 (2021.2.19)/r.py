# name:   P.U.B.智能计算系统
# author: Thomas·P
# date:   2021.2.19
# version:0.0.7
from tkinter import *
from tkinter.ttk import *
from tkinter import Label
from time import sleep

root = Tk()
root.wm_title("P.U.B.智能计算系统")
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = 990
wh = 540
x = (sw - ww) / 2
y = (sh - wh) / 2
root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
root.resizable(0, 0)
menubar = Menu(root)
for item in ["语言", "关于", "反馈"]:
    menubar.add_command(label=item)
root["menu"] = menubar
scrollbar = Scrollbar(root, orient="vertical")
scrollbar.pack(side='right', fill='y')
scrollbar2 = Scrollbar(root, orient="horizontal")
scrollbar2.pack(side='bottom', fill='x')

def subwindow():
    new=Toplevel(root)
def start_label():
    start = Label(root, text="欢迎来到P.U.B.智能计算系统！", font=("宋体", "20"))
    start.pack(side="top", anchor="center")
    button_1.pack_forget()
    root.update()
    sleep(1)
    start.config(text="功能目录", font=("仿宋", "15"))
    contents = Treeview(root)
    contents.pack(expand='yes', fill="both")
    treeA = contents.insert("", 0, "A", text="代数计算", values=("A"))
    treeB = contents.insert("", 1, "B", text="几何计算", values=("B"))
    treeA_1 = contents.insert(treeA, 0, "A_1", text="高级计算器", values=("A_1"))
    treeA_1.bind("<Button-1>",subwindow)
    treeA_2 = contents.insert(treeA, 0, "A_2", text="方程计算器", values=("A_2"))
    treeB_1 = contents.insert(treeB, 1, "B_1", text="平面计算", values=("B_1"))
    treeB_2 = contents.insert(treeB, 1, "B_2", text="立体计算", values=("B_2"))

style = Style(root)
style.configure('1.TButton', font=('仿宋', '20'), )
button_1 = Button(root, text="\0\0\0\0点击按钮\n启动计算系统\0", style='1.TButton', command=start_label)
button_1.pack(expand='yes')

root.mainloop()
