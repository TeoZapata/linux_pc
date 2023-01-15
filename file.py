import matplotlib.pyplot as plt 
import numpy as np


x = np.linspace(0,10,100)

def f(x):
    return np.sinh(x)

y = f(x)

fig, axes  = plt.subplots()

axes.scatter(x,y)
axes.axhline(2000)

plt.savefig("sinofx.jpg")



