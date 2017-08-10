import matplotlib.pyplot as plt
import numpy as np

def render_func_graph(formula, x_range):
    try:
        fig = plt.figure()    
        x = np.array(x_range)
        y = eval(formula)
        print(y)
        plt.plot(x, y, 'go-')
        plt.scatter(0,0)
        plt.grid(True)
        plt.show()
    except Exception as err:
        print(str(err))  

def main():
    func = input('f(x):')
    render_func_graph(func, range(-10, 10))

if __name__ == '__main__':
    main()

