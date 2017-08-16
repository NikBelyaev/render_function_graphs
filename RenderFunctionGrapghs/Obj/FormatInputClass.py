import re
import numpy as np
from Obj.config import *

class FormatInput:
    def __init__(self, formula):
        self.formula = formula


    def basic_format(self):
        self.formula = self.formula.replace(' ', '')
        self.formula = self.formula.replace('÷', '/')
        self.formula = self.formula.replace('^', '**')
         
    def format_vertical_slashes(self):
        """Replaces vertical slashes (|) with abs() method"""
        re_result_list = re.findall('(\|.*?\|)', self.formula)
        for re_result in re_result_list:
            self.formula = self.formula.replace(re_result,
                                                'abs(' + re_result.strip('|') + ')')

    def format_sqrt_symbol(self):
        re_result_list = re.findall('(√\(.*?\))', self.formula)
        for re_result in re_result_list:
            self.formula = self.formula.replace(re_result,
                                                'sqrt(' + re_result[2:len(re_result)-1] + ')')

    def format_multiply(self):
        # Find with regex
        possible_mult_constr = ['[\d(\dx)[^]]]+[\(]', '\d+[x]', '\)\(']
        for mult_constr in possible_mult_constr:
            for res in re.findall(mult_constr, self.formula):
                # Adding *
                tmp = res.split(res[len(res)-1:])[0]+'*'+res[len(res)-1:]
                self.formula = self.formula.replace(res, tmp)


    def format_comma_statement(self):
        comp_symbols = ['>[^=]', '<[^=]', '>=', '<=', '[^<>]=']
        
        self.formula, new_comp = self.formula.split(',')

        for comp_symbol in comp_symbols:
            re_result = re.search(comp_symbol, new_comp)
            if re_result is not None:
                re_result = re.sub('\d', '', re_result.group(0))
                x_value = int(new_comp.split(re_result)[1])
                if comp_symbol == '>[^=]':
                    self.x_range = np.arange(x_value + 1,
                                             x_value + shape_of_x_range + 1,
                                             x_step)
                elif comp_symbol == '<[^=]':
                    self.x_range = np.arange(x_value - shape_of_x_range + 1,
                                             x_value - 1, x_step)
                elif comp_symbol == '>=':
                    self.x_range = np.arange(x_value,
                                             x_value + shape_of_x_range,
                                             x_step)
                elif comp_symbol == '<=':
                    self.x_range = np.arange(x_value - shape_of_x_range,
                                             x_value, x_step)
            else:
                self.x_range = None
        
##
##    def format_system_of_equations(self):
##        """Splits system of equations to simple equations"""
##        comp_symbols = ['>[^=]', '<[^=]', '>=', '<=', '[^<>]=']
##        list_of_dicttype_formulas = []
##        for n_formula in self.formula[1:].replace(' ', '').split(';'):
##            new_formula, new_comp = n_formula.split(',')
##            for comp_symbol in comp_symbols:
##                re_result = re.search(comp_symbol, new_comp)
##                if re_result is not None:
##                    re_result = re.sub('\d', '', re_result.group(0))
##                    x_value = int(new_comp.split(re_result)[1])
##                    if comp_symbol == '>[^=]':
##                        self.x_range = np.arange(x_value + 1,
##                                                 x_value + shape_of_x_range + 1,
##                                                 x_step)
##                    elif comp_symbol == '<[^=]':
##                        self.x_range = np.arange(x_value - shape_of_x_range + 1,
##                                                 x_value - 1, x_step)
##                    elif comp_symbol == '>=':
##                        self.x_range = np.arange(x_value,
##                                                 x_value + shape_of_x_range,
##                                                 x_step)
##                    elif comp_symbol == '<=':
##                        self.x_range = np.arange(x_value - shape_of_x_range,
##                                                 x_value, x_step)
##                    list_of_dicttype_formulas.append(dict(
##                        {'formula': new_formula, 'x_range': self.x_range}))
##        return list_of_dicttype_formulas

    def wrapper_format_input(self, system_of_eq=False):
        """Wraps all the formating input functions"""
        try:
            self.basic_format()
            self.format_vertical_slashes()
            self.format_sqrt_symbol()
            self.format_multiply()
            if system_of_eq:
                self.format_comma_statement()
                return self.formula, self.x_range
            else:   
                return self.formula
        except Exception as error:
            print('[!!] Error in FormatInput', str(error))
