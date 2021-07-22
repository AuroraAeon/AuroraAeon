# name:   P.U.B.智能计算系统
# author: Thomas·P
# date:   2020.12.3
# version:0.0.2

import math
import time
from tkinter import*


def start_label():
    global root
    start = Label(root, text="欢迎来到P.U.B.智能计算系统！")
    start.pack()


root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))
root.resizable(0, 0)
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
