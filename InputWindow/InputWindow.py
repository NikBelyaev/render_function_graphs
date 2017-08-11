#-*-coding: utf-8-*-
from tkinter import *
import math
from FormatInput.FormatInputClass import FormatInputClass

class FormulaInput:
    def equals(self):
        """when the equal button is pressed"""

        self.format_input = FormatInputClass(self.e.get(), self.x_range)
        self.finished_formula = self.format_input.wrapper_format_input()
        self.e.delete(0, END)

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

    def __init__(self, master, formula):
        """Constructor method"""
        master.title('Calulator')
        master.geometry()
        self.finished_formula = formula
        self.e = Entry(master, width=100)
        self.e.grid(row=0, column=0, columnspan=6, pady=3)
        self.e.focus_set()  # Sets focus on the input text area
        self.newdiv = '÷'

        # Generating Buttons
        Button(master, text="=", width=50, height=3, command=lambda: self.equals()).grid(
            row=5, column=4, columnspan=2)
        Button(master, text='AC', width=8, height=3,
               command=lambda: self.clearall()).grid(row=1, column=4)
        Button(master, text='C', width=8, height=3,
               command=lambda: self.clear1()).grid(row=1, column=5)
        Button(master, text="+", width=8, height=3,
               command=lambda: self.action('+')).grid(row=4, column=3)
        Button(master, text="*", width=8, height=3,
               command=lambda: self.action('*')).grid(row=2, column=3)
        Button(master, text="-", width=8, height=3,
               command=lambda: self.action('-')).grid(row=3, column=3)
        Button(master, text="÷", width=8, height=3, command=lambda: self.action(
            self.newdiv)).grid(row=1, column=3)
        Button(master, text="%", width=8, height=3,
               command=lambda: self.action('%')).grid(row=4, column=2)
        Button(master, text="7", width=8, height=3,
               command=lambda: self.action(7)).grid(row=1, column=0)
        Button(master, text="8", width=8, height=3,
               command=lambda: self.action(8)).grid(row=1, column=1)
        Button(master, text="9", width=8, height=3,
               command=lambda: self.action(9)).grid(row=1, column=2)
        Button(master, text="4", width=8, height=3,
               command=lambda: self.action(4)).grid(row=2, column=0)
        Button(master, text="5", width=8, height=3,
               command=lambda: self.action(5)).grid(row=2, column=1)
        Button(master, text="6", width=8, height=3,
               command=lambda: self.action(6)).grid(row=2, column=2)
        Button(master, text="1", width=8, height=3,
               command=lambda: self.action(1)).grid(row=3, column=0)
        Button(master, text="2", width=8, height=3,
               command=lambda: self.action(2)).grid(row=3, column=1)
        Button(master, text="3", width=8, height=3,
               command=lambda: self.action(3)).grid(row=3, column=2)
        Button(master, text="0", width=8, height=3,
               command=lambda: self.action(0)).grid(row=4, column=0)
        Button(master, text=".", width=8, height=3,
               command=lambda: self.action('.')).grid(row=4, column=1)
        Button(master, text="(", width=8, height=3,
               command=lambda: self.action('(')).grid(row=2, column=4)
        Button(master, text=")", width=8, height=3,
               command=lambda: self.action(')')).grid(row=2, column=5)
        Button(master, text="√", width=8, height=3,
               command=lambda: self.action('√()')).grid(row=3, column=4)
        Button(master, text="|", width=8, height=3,
               command=lambda: self.action('|')).grid(row=4, column=4)
        Button(master, text="^", width=8, height=3,
               command=lambda: self.action('^')).grid(row=3, column=5)
        Button(master, text="sin", width=8, height=3,
               command=lambda: self.action('sin()')).grid(row=1, column=6)
        Button(master, text="cos", width=8, height=3,
               command=lambda: self.action('cos()')).grid(row=2, column=6)
        Button(master, text="tan", width=8, height=3,
               command=lambda: self.action('tan()')).grid(row=3, column=6)
