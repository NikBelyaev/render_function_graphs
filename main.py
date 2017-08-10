import matplotlib.pyplot as plt
import numpy as np

def render_func_graph(formula, x_range):
    try:
        x = np.array(x_range)
        y = eval(formula)
        ## Instructions for func graph rendering
        fig = plt.figure('Function graph')        
        ax = fig.add_subplot(111)
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_smart_bounds(True)
        ax.spines['bottom'].set_smart_bounds(True)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.scatter(0,0)
        plt.grid(True)
        plt.plot(x, y, 'go-')
        plt.show()
    except Exception as err:
        print(str(err))

def main():
    func = input('f(x):')
    render_func_graph(func, np.arange(-5, 5, 0.5))

if __name__ == '__main__':
    main()

