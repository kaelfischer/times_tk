#!/usr/bin/python

import tkinter as tk
from tkinter.font import Font

from random import randint



top = tk.Tk()

BOLD = Font(top, weight='bold',size="30")
BIG = Font(top, size=30)
PIXEL = tk.PhotoImage(width=1, height=1)

top.CORRECT = False

top.correct_answer = None

frame = tk.Frame(top, pady=25,padx=80)#width=800,height=600)
#frame.grid_propagate(0)
frame.pack(fill=tk.BOTH, expand=True)


class ScoreGrid (tk.Toplevel):

    def __init__(self):
        super().__init__(top,bg='#666')
        self.cells = []
        for row in range(13):
            self.cells.append([])
            for column in range(13):
                cell = tk.Label(self, width=20, height=20, bd=1, bg='red', text='',
                                 image=PIXEL, compound='c')
                cell.grid(row=row,column=column)
                self.cells[-1].append(cell)

    def mark_cell(self,color):
        row,column = top.number1,top.number2
        print( row, column)
        cell = self.cells[row][column]
        cell.configure(background=color)
        cell.grid(row=row,column=column)
        print(cell.configure())


def check_answer(event):
    if top.CORRECT:
        for widget in swap_color_widgets:
            widget.config(bg='white')
        reset_problem()

    else:
        if top.correct_answer == int(answer_area.get()):
            for widget in swap_color_widgets:
                widget.config(bg='lightgreen')
                score_grid.mark_cell('green')
            top.CORRECT = True


        else:
            for widget in swap_color_widgets:
                widget.config(bg='#f44')
            top.CORRECT = False


def reset_problem():
    top.number1 = randint(1,12)
    top.number2 = randint(1,12)
    top.correct_answer = top.number1 * top.number2
    top.CORRECT = False

    str1.set(str(top.number1))
    str2.set(str(top.number2))
    answer_area.delete(0,100)


top.CORRECT = False
top.bind('<Return>',check_answer)

str1 = tk.StringVar()
label1 = tk.Label(frame, textvariable=str1, font=BOLD)

str2 = tk.StringVar()
label2 = tk.Label(frame, textvariable=str2, font=BOLD)

operator_label = tk.Label(frame, text="X")
eq_label = tk.Label(frame, text='=')

answer_area = tk.Entry(frame, width=5, bd=3, font=BOLD)

reset_problem()

score_grid = ScoreGrid()
#score_grid.mark_cell('green')

label1.grid(column=1, row=1)
operator_label.grid(column=2, row=1)
label2.grid(column=3, row=1)
eq_label.grid(column=4,row=1)
answer_area.grid(column=5,row=1)

swap_color_widgets = (label1,label2,operator_label,eq_label,frame)

top.mainloop()
