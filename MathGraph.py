from tkinter import *
import tkinter as tk
from math import sqrt,exp,tan,sin,cos,log,atan
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import matplotlib.pyplot as plt


window = Tk()

window.geometry("730x670+250+20")
window.resizable(0,0)
window.title("Math Graph Generator")
color_back='white'
font_color='black'
bar_task_color='black'
title_task_color='red'
window.configure(background=color_back)


def Plot_initial():
    fun = [1]
    timp = [1]
    fig = Figure(figsize=(7.2, 6.1))
    a = fig.add_subplot(111)
    a.plot(timp, fun, color='blue')
    a.minorticks_on()
    a.grid(b=True, which='minor', color='#666666', linestyle='-', alpha=0.3)
    a.grid(b=True, which='major', color='#666666', linestyle='-')
    a.set_ylim(bottom=None, top=None, emit=True, auto=True, ymin=None, ymax=None)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=7)
    canvas.draw()

Plot_initial()

def Makeploat():

    math_function = entry_function.get()

    if "e" in math_function:
        math_function = math_function.replace('e^', 'exp')
    elif "^" in math_function:
        math_function = math_function.replace('^', '**')
    if "ln" in math_function:
        math_function = math_function.replace('ln', 'log')
    if "rad" in math_function:
        math_function = math_function.replace('rad', 'sqrt')

    math_function2 = entry_function2.get()

    if "e" in math_function2:
        math_function2 = math_function2.replace('e^', 'exp')
    elif "^" in math_function2:
        math_function2 = math_function2.replace('^', '**')
    if "ln" in math_function2:
        math_function2 = math_function2.replace('ln', 'log')
    if "rad" in math_function2:
        math_function2 = math_function2.replace('rad', 'sqrt')

    fig = Figure(figsize=(7.2, 6.1))
    a = fig.add_subplot(111)

    if  math_function != (''):
        start_time = int(entry_start.get())
        stop_time = int(entry_stop.get())
        f = list()
        domen = list()
        bold_x = list()
        interval = np.linspace(start_time, stop_time, 1000)
        for x in interval:
            try:
                y = eval(math_function)
                f.append(y)
                domen.append(x)
            except:
                continue


        #a.plot(domen, bold_x, color='black', label='First function')
        #a.plot(bold_x, domen, color='black', label='First function')
        a.plot(domen, f, color='blue',label='First function')
        a.legend()


    a.minorticks_on()
    a.grid(b=True, which='minor', color='#666666', linestyle='-', alpha=0.1)
    a.grid(b=True, which='major', color='#666666', linestyle='-')
    a.set_ylim(bottom=None, top=None, emit=True, auto=True, ymin=None, ymax=None)
    a.margins(0,0)
    a.autoscale()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=7)
    canvas.draw()



    if math_function2 != (''):
        start_time2 = int(entry_start2.get())
        stop_time2 = int(entry_stop2.get())
        interval2 = np.linspace(start_time2, stop_time2, 1000)
        f2 = list()
        domen2 = list()
        for x in interval2:
            try:
                y2 = eval(math_function2)
                f2.append(y2)
                domen2.append(x)
            except:
                continue
        a.plot(domen2, f2, color='red', label='Second function')
        a.legend()


def Clear_all():
    entry_function.delete(0, 'end')
    entry_function2.delete(0, 'end')
    entry_stop.delete(0, 'end')
    entry_stop2.delete(0, 'end')
    entry_start.delete(0, 'end')
    entry_start2.delete(0,'end')


tk.Label(window, text="Function 1:", font="arial 12 bold",width=10,bg=color_back,fg=font_color).grid(row=1)
tk.Label(window, text="Start from:",font="arial 12 bold",width=10,bg=color_back,fg=font_color).grid(row=1,column=2)
tk.Label(window, text="to stop at:", font="arial 12 bold",width=10,bg=color_back,fg=font_color).grid(row=1,column=4)

tk.Label(window, text="Function 2:", font="arial 12 bold",width=10,bg=color_back,fg=font_color).grid(row=2)
tk.Label(window, text="Start from:",font="arial 12 bold",width=10,bg=color_back,fg=font_color).grid(row=2,column=2)
tk.Label(window, text="to stop at:", font="arial 12 bold",width=10,bg=color_back,fg=font_color).grid(row=2,column=4)

entry_function = tk.Entry(window,font="arial 12 bold",width=12,bg=color_back,fg=font_color)
entry_start = tk.Entry(window,font="arial 12 bold",width=10,bg=color_back,fg=font_color)
entry_stop = tk.Entry(window,font="arial 12 bold",width=10,bg=color_back,fg=font_color)

entry_function2 = tk.Entry(window,font="arial 12 bold",width=12,bg=color_back,fg=font_color)
entry_start2 = tk.Entry(window,font="arial 12 bold",width=10,bg=color_back,fg=font_color)
entry_stop2 = tk.Entry(window,font="arial 12 bold",width=10,bg=color_back,fg=font_color)

entry_function.grid(row=1, column=1)
entry_start.grid(row=1, column=3)
entry_stop.grid(row=1, column=5)

entry_function2.grid(row=2, column=1)
entry_start2.grid(row=2, column=3)
entry_stop2.grid(row=2, column=5)

button=Button(window,text="Show graph",command=Makeploat,font="arial 12 bold",width=10,bd=3,bg=color_back,fg=font_color).grid(row=1, column=6)
button_delete=Button(window,text="Clear All",command=Clear_all,font="arial 12 bold",width=10,bd=3,bg=color_back,fg=font_color).grid(row=2, column=6)

window.mainloop()