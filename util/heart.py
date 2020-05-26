# -*- coding: utf-8 -*-
from numpy import arange, power, abs, sqrt, sin
from math import pi
from matplotlib.pyplot import plot, title, axis, show


if __name__ == '__main__':
    b = 0
    while True:
        x=arange(-1.80,1.81,0.01)
        y=power(abs(x),2/3)+0.9*sqrt(3.3-x**2)*sin(int(b)*pi*x)
        plot(x,y,color='red')
        title('My heart will go on!')
        axis('off')
        show()
        b += 1