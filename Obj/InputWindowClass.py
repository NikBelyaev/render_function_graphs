#-*-coding: utf-8-*-
from tkinter import *
import numpy as np
from Obj.FormatInputClass import FormatInput
from Obj.RenderGraph import render_func_graph
import Obj.config as cfg

class InputWindow:
    def equals(self):
        """when the equal button is pressed"""
        formula_range_list_dict = []
        self.format_input = FormatInput(self.e.get())
        
        self.finished_formula = self.format_input.wrapper_format_input()
        formula_range_list_dict.append(dict({'formula': self.finished_formula,
                                             'x_range': np.arange(-cfg.shape_of_x_range,
                                                        cfg.shape_of_x_range,
                                                        cfg.x_step)}))
        self.e.delete(0, END)
        render_func_graph(formula_range_list_dict)
        

    def clearall(self):
        """when clear button is pressed,clears the text input area"""
        self.e.delete(0, END)

    def clear1(self):
        self.txt = self.e.get()[:-1]
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def action(self, argi):
        """pressed button's value is inserted into the end of the text area"""
        self.e.insert(END, argi)

        
    def __init__(self):
        """Constructor method"""
        root = Tk()
        root.title('Calulator')
        root.geometry()
        self.e = Entry(root, width=100)
        self.e.grid(row=0, column=0, columnspan=6, pady=3)
        self.e.focus_set()  # Sets focus on the input text area
        self.newdiv = '÷'

        # Generating Buttons
        Button(root, text="=", width=50, height=3, command=lambda: self.equals()).grid(
            row=5, column=4, columnspan=2)
        Button(root, text='AC', width=8, height=3,
               command=lambda: self.clearall()).grid(row=1, column=4)
        Button(root, text='C', width=8, height=3,
               command=lambda: self.clear1()).grid(row=1, column=5)
        Button(root, text="+", width=8, height=3,
               command=lambda: self.action('+')).grid(row=4, column=3)
        Button(root, text="*", width=8, height=3,
               command=lambda: self.action('*')).grid(row=2, column=3)
        Button(root, text="-", width=8, height=3,
               command=lambda: self.action('-')).grid(row=3, column=3)
        Button(root, text="÷", width=8, height=3, command=lambda: self.action(
            self.newdiv)).grid(row=1, column=3)
        Button(root, text="%", width=8, height=3,
               command=lambda: self.action('%')).grid(row=4, column=2)
        Button(root, text="7", width=8, height=3,
               command=lambda: self.action(7)).grid(row=1, column=0)
        Button(root, text="8", width=8, height=3,
               command=lambda: self.action(8)).grid(row=1, column=1)
        Button(root, text="9", width=8, height=3,
               command=lambda: self.action(9)).grid(row=1, column=2)
        Button(root, text="4", width=8, height=3,
               command=lambda: self.action(4)).grid(row=2, column=0)
        Button(root, text="5", width=8, height=3,
               command=lambda: self.action(5)).grid(row=2, column=1)
        Button(root, text="6", width=8, height=3,
               command=lambda: self.action(6)).grid(row=2, column=2)
        Button(root, text="1", width=8, height=3,
               command=lambda: self.action(1)).grid(row=3, column=0)
        Button(root, text="2", width=8, height=3,
               command=lambda: self.action(2)).grid(row=3, column=1)
        Button(root, text="3", width=8, height=3,
               command=lambda: self.action(3)).grid(row=3, column=2)
        Button(root, text="0", width=8, height=3,
               command=lambda: self.action(0)).grid(row=4, column=0)
        Button(root, text=".", width=8, height=3,
               command=lambda: self.action('.')).grid(row=4, column=1)
        Button(root, text="(", width=8, height=3,
               command=lambda: self.action('(')).grid(row=2, column=4)
        Button(root, text=")", width=8, height=3,
               command=lambda: self.action(')')).grid(row=2, column=5)
        Button(root, text="√", width=8, height=3,
               command=lambda: self.action('√()')).grid(row=3, column=4)
        Button(root, text="|", width=8, height=3,
               command=lambda: self.action('|')).grid(row=4, column=4)
        Button(root, text="^", width=8, height=3,
               command=lambda: self.action('^')).grid(row=3, column=5)
        Button(root, text="sin", width=8, height=3,
               command=lambda: self.action('sin()')).grid(row=1, column=6)
        Button(root, text="cos", width=8, height=3,
               command=lambda: self.action('cos()')).grid(row=2, column=6)
        Button(root, text="tan", width=8, height=3,
               command=lambda: self.action('tan()')).grid(row=3, column=6)

        root.mainloop()
