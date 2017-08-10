import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
xlist, ylist = [], []
func = input('f(x):')

for x in range(-5, 5):
    try:
        new_func = func.replace('x', str(x))
        ylist.append(eval(new_func))
        xlist.append(x)
    except Exception as err:
        print(str(err))

fig = plt.plot(xlist, ylist, 'go-')

plt.scatter(0,0)
plt.grid(True)
plt.show()
