from numpy import *
from sympy import *
y = symbols('y')
def final_distance(x_2, function1, function2):
    distance = []
    for b in range (0, 100):
        print(x_2[b])
        xtwo = x_2[b]
        print(xtwo)
        x2 = int(xtwo)
        print(x2)
        xone = b + 1
        x1 = int(xone)
        r = sqrt((x2 - x1)**2 + (function1.subs(y, x1) - function2.subs(y, x2))**2)
        distance.append(r)
    return distance;
