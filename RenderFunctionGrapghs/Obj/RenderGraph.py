import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, tan, sqrt

def render_func_graph(formula_range_list_dict):
    try:
        # Set the settings to display graph
        fig = plt.figure('Function graph')
        ax = fig.add_subplot(111)
        # Set the Axis OX and OY crossed on zero
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_smart_bounds(True)
        ax.spines['bottom'].set_smart_bounds(True)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.scatter(0, 0)
        plt.grid(True)
        for formula_range_dict in formula_range_list_dict:
            x = np.array(formula_range_dict.get('x_range'))
            y = eval(str(formula_range_dict.get('formula')))
            plt.plot(x, y, 'go-')
        plt.show()
    except Exception as err:
        print('[!!] Error in render_func_graph', str(err))
