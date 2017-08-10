import matplotlib.pyplot as plt
import numpy as np
import re

def format_input_func(formula):
    # Search for | symbols and replace it with abs() method
    re_result_list = re.findall('(\|.*?\|)', formula)
    for re_result in re_result_list:
        formula = formula.replace(re_result, 'abs('+re_result.strip('|')+')')
    return formula

def render_func_graph(formula, x_range):
    try:
        x = np.array(x_range)
        y = eval(formula)
        ## Set the settings to display graph
        fig = plt.figure('Function graph') 
        plt.xticks(np.arange(min(x), max(x)+1, 1.0))
        ax = fig.add_subplot(111)
        ## Set the Axis OX and OY crossed on zero
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_smart_bounds(True)
        ax.spines['bottom'].set_smart_bounds(True)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.xticks(np.arange(min(x), max(x)+1, 1.0))
        plt.plot(x, y, 'go-')
        plt.scatter(0,0)
        plt.grid(True)
        plt.show()
    except Exception as err:
        print(str(err))  

def main():
    print('Type "q" to exit the program.\n\n')
    while True:
        func = input('f(x):')
        if func=='q':
            break
        formula = format_input_func(func)
        print(formula)
        render_func_graph(formula, np.arange(-5, 5, 0.5))

if __name__ == '__main__':
    main()

