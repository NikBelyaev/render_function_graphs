'''wxPython Calculator Demo in 50 lines of code'''
import wx
import numpy as np
from numpy import sin, cos, tan, sqrt # So we can evaluate 'sqrt(8)'
from Obj.FormatInputClass import FormatInput
from Obj.RenderGraph import render_func_graph
import Obj.config as cfg


class InputWindow(wx.Dialog):
    '''Main calculator dialog'''
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'Render Graph')    
        sizer = wx.BoxSizer(wx.VERTICAL) # Main vertical sizer

        # ____________v
        self.display = wx.ComboBox(self, -1) # Current calculation
        sizer.Add(self.display, 0, wx.EXPAND) # Add to main sizer

        # [7][8][9][/] 
        # [4][5][6][*]
        # [1][2][3][-]
        # [0][.][C][+]
        gsizer = wx.GridSizer(4, 5, 1)
        for row in (('sin()', 'cos()', 'tan()', 'x'),
                    ('|', '(', ')', '^'),
                    ('7', '8', '9', '÷'),
                    ('4', '5', '6', '*'),
                    ('1', '2', '3', '-'),
                    ('0', '√()','C', '+')):
            for label in row:
                b = wx.Button(self, -1, label)
                gsizer.Add(b)
                self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(gsizer, 1, wx.EXPAND)

        # [    =     ]
        b = wx.Button(self, -1, '=')
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(b, 0, wx.EXPAND)
        self.equal = b

        # Set sizer and center
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.CenterOnScreen()

        
    def OnButton(self, evt):
        '''Handle button click event'''
        # Get title of clicked button
        label = evt.GetEventObject().GetLabel() 

        if label == '=': # Calculate
            try:
                compute = self.display.GetValue()
                # Ignore empty calculation
                if not compute.strip():
                    return

                # Add to history
                self.display.Insert(compute, 0)
                
                formula_range_list_dict = []
                self.format_input = FormatInput(compute)
                self.finished_formula = self.format_input.wrapper_format_input()
                formula_range_list_dict.append(dict({'formula': self.finished_formula,
                                                     'x_range': np.arange(-cfg.shape_of_x_range,
                                                                cfg.shape_of_x_range,
                                                                cfg.x_step)}))

                self.display.SetValue('')
                render_func_graph(formula_range_list_dict)
            except Exception as e:
                wx.LogError(str(e))
                return

        elif label == 'C': # Clear
            self.display.SetValue('')

        else: # Just add button text to current calculation
            self.display.SetValue(self.display.GetValue() + label)
            self.equal.SetFocus() # Set the [=] button in focus
