import re
import numpy as np
from config import shape_of_x_range, x_step

class FormatInputClass:
    def __init__(self, formula, x_range):
        self.formula = formula
        self.x_range = x_range


    def format_vertical_slashes(self):
        """Replaces vertical slashes (|) with abs() method"""
        re_result_list = re.findall('(\|.*?\|)', self.formula)
        for re_result in re_result_list:
            self.formula = self.formula.replace(re_result,
                                            'abs('+re_result.strip('|')+')')
        return self.formula


    def format_trigon_funcs(self):
        """Adds prefix (np.) before all trigon. functions"""
        trigon_funcs = ['[^c]sin', '[^c]cos', '[^c]tan',
                        'arcsin', 'arccos', 'arctan']
        for trigon_func in trigon_funcs:
            if trigon_func in self.formula:
                self.formula = self.formula.replace(trigon_func,
                                                    'np.'+trigon_func)
        return self.formula


    def format_system_of_equations(self):
        """Splits system of equations to simple equations"""
        comp_symbols = ['>[^=]', '<[^=]', '>=', '<=','[^<>]=']
        list_of_dicttype_formulas = []
        for n_formula in self.formula[1:].replace(' ', '').split(';'):
            new_formula, new_comp = n_formula.split(',')
            for comp_symbol in comp_symbols:
                re_result = re.search(comp_symbol, new_comp)
                if re_result is not None:
                    re_result = re.sub('\d', '', re_result.group(0))
                    x_value = int(new_comp.split(re_result)[1])
                    if comp_symbol == '>[^=]':
                        self.x_range = np.arange(x_value+1,
                                                 x_value+shape_of_x_range+1,
                                                 x_step)
                    elif comp_symbol == '<[^=]':
                        self.x_range = np.arange(x_value-shape_of_x_range+1,
                                                 x_value-1, x_step)
                    elif comp_symbol == '>=':
                        self.x_range = np.arange(x_value,
                                                 x_value+shape_of_x_range,
                                                 x_step)
                    elif comp_symbol == '<=':
                        self.x_range = np.arange(x_value-shape_of_x_range,
                                                 x_value, x_step)
                    list_of_dicttype_formulas.append(dict(
                        {'formula':new_formula, 'x_range':self.x_range}))
        return list_of_dicttype_formulas

    
    def wrapper_format_input(self):
        """Wraps all the formating input functions"""
        try:
            if self.formula[0] == '{':
                return self.format_system_of_equations()
            else:
                self.formula = self.format_vertical_slashes()
                self.formula = self.format_trigon_funcs()
                return [{'formula':self.formula, 'x_range':self.x_range}]
        except Exception as error:
            print(str(error))
