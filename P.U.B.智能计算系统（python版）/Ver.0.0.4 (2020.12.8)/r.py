# name:   P.U.B.智能计算系统
# author: Thomas·P
# date:   2020.12.8
# version:0.0.4

import math
import time
from tkinter import *
from tkinter.ttk import *


def start_label():
    global root
    start = Label(root, text="欢迎来到P.U.B.智能计算系统！")
    start.pack()


root = Tk()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = 990
wh = 540
x = (sw-ww) / 2
y = (sh-wh) / 2
root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
root.resizable(0, 0)
canvas = Canvas(root, width=ww, height=wh, scrollregion=(0, 0, 520, 520)) #创建canvas
canvas.place(x = 0, y = 0) #放置canvas的位置
frame=Frame(canvas) #把frame放在canvas里
frame.place(width = ww, height = wh) #frame的长宽，和canvas差不多的
vbar=Scrollbar(canvas,orient=VERTICAL) #竖直滚动条
vbar.place(x = ww-20, width = 20, height = wh)
vbar.configure(command=canvas.yview)
hbar=Scrollbar(canvas,orient=HORIZONTAL)#水平滚动条
hbar.place(x =0,y=wh-20,width=ww,height=20)
hbar.configure(command = canvas.xview)
canvas.config(xscrollcommand=hbar.set,yscrollcommand=vbar.set) #设置
canvas.create_window((ww, wh), window = frame)  #create_window
scrollbar = Scrollbar(root)
button_1 = Button(root, text="点击按钮启动计算系统", command=start_label)
button_1.pack()
root.wm_title("P.U.B.智能计算系统")
root.mainloop()
start_input = "请选择您需要的计算类型（按1或2并按下回车(ENTER)）："
time.sleep(2)
print("以下是本系统支持的数学计算领域：\n1.代数\n2.几何")
time.sleep(2)
while True:
    choose = input(start_input)
    start_input = "请选择您需要的计算类型（按1或2并按下回车(ENTER)）："
    if choose == '1' or choose == '2':
        input_content = "请输入圆的半径："
        while True:
            a = input(input_content)
            input_content = "请输入圆的半径："
            try:
                r = float(a)
                s = math.pi * r ** 2
                print("圆的面积是：", s)
                break
            except ValueError:
                print("您输入的格式有误，请重新输入：", end='')
                input_content = ''
                continue
    else:
        print("您输入的格式有误，请重新输入：", end='')
        start_input = ''
        continue
