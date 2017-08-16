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
        self.mainSizer = wx.BoxSizer(wx.VERTICAL) # Main vertical sizer

        self.system_of_eq = False
        
        # ____________v
        self.inputBoxId = 0
        self.displayList = []
        self.inputSizer = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.ComboBox(self, -1) # Current calculation
##        self.display.Bind(wx.EVT_KILL_FOCUS, self.OnFocus)
        self.inputSizer.Add(self.display, 0, wx.EXPAND) # Add to main sizer
        self.displayList.append(self.display)
        
        self.mainSizer.Add(self.inputSizer, 0, wx.EXPAND)
        # [7][8][9][/] 
        # [4][5][6][*]
        # [1][2][3][-]
        # [0][.][C][+]
        gsizer = wx.GridSizer(4, 5, 1)
        self.buttonSizer = wx.BoxSizer(wx.VERTICAL)
        for row in (('sin()', 'cos()', 'tan()', 'x'),
                    ('|', '(', ')', '^'),
                    ('7', '8', '9', '÷'),
                    ('4', '5', '6', '*'),
                    ('1', '2', '3', '-'),
                    ('0', '√()','{', '+'),
                    'C'):
            for label in row:
                b = wx.Button(self, -1, label)
                gsizer.Add(b)
                self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        self.buttonSizer.Add(gsizer, 1, wx.EXPAND)

        # [    =     ]
        b = wx.Button(self, -1, '=')
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        self.buttonSizer.Add(b, 0, wx.EXPAND)
        self.equal = b

        self.mainSizer.Add(self.buttonSizer, 0, wx.EXPAND)
        
        # Set sizer and center
        self.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)
        self.CenterOnScreen()


##    def OnFocus(self, evt):
##        self.focused = evt.GetEventObject()

        
    def OnButton(self, evt):
        '''Handle button click event'''
        # Get title of clicked button
        label = evt.GetEventObject().GetLabel() 
        if label == '{':
            
            if not self.inputBoxId == 2:
                self.system_of_eq = True
                self.inputBoxId+=1
                try:
                    del(self.newDisplay)
                except:
                    pass
                self.newDisplay = wx.ComboBox(self, -1)
    ##            self.display2.Bind(wx.EVT_KILL_FOCUS, self.OnFocus)
                self.inputSizer.Add(self.newDisplay, 0, wx.EXPAND)
                self.mainSizer.Layout()
                self.displayList.append(self.newDisplay)
                self.display.SetValue('')
        if label == '=': # Calculate
            try:
                formula_range_list_dict = []
                for inp in self.displayList:
                    compute = inp.GetValue()
                    # Ignore empty calculation
                    if not compute.strip():
                        return

                    # Add to history
                    inp.Insert(compute, 0)
                    
                    self.format_input = FormatInput(compute)
                    finished_formula, x_range = self.format_input.wrapper_format_input(system_of_eq = self.system_of_eq)
                    if x_range:
                        formula_range_list_dict.append(dict({'formula': finished_formula,
                                                             'x_range': x_range}))
                    else:
                        formula_range_list_dict.append(dict({'formula': finished_formula,
                                                             'x_range': np.arange(-cfg.shape_of_x_range,
                                                                        cfg.shape_of_x_range,
                                                                        cfg.x_step)}))

                    inp.SetValue('')
                render_func_graph(formula_range_list_dict)
                if len(self.displayList)==2:
                    self.inputSizer.Remove(1)
                    self.mainSizer.Layout()
                    self.displayList.pop(1)
                self.system_of_eq = False
            except Exception as e:
                wx.LogError(str(e))
                return

        elif label == 'C': # Clear
            for inp in self.displayList:
                inp.SetValue('')

        else: # Just add button text to current calculation
##            self.focused.SetValue(self.focused.GetValue() + label)
            self.display.SetValue(self.display.GetValue() + label)

##            self.equal.SetFocus() # Set the [=] button in focus
##
