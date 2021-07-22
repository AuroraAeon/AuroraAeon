# name:   P.U.B.智能计算系统
# author: Thomas·P
# date:   2020.12.13
# version:0.0.6
from tkinter import *
from tkinter.ttk import *
root = Tk()
root.wm_title("P.U.B.智能计算系统")
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = 990
wh = 540
x = (sw-ww) / 2
y = (sh-wh) / 2
root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
root.resizable(0, 0)
scrollbar = Scrollbar(root, orient="vertical")
scrollbar.pack(side='right', fill='y')
scrollbar2 = Scrollbar(root, orient="horizontal")
scrollbar2.pack(side='bottom', fill='x')


def start_label():
    start = Label(root, text="欢迎来到P.U.B.智能计算系统！")
    start.pack()
    button_1.pack_forget()


style = Style(root)
style.configure('1.TButton', font=('仿宋', '20'),)
button_1 = Button(root, text="\0\0\0\0点击按钮\n启动计算系统\0", style='1.TButton', command=start_label)
button_1.pack(expand='yes')

root.mainloop()
