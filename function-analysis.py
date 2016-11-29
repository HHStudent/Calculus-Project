"""
function = str(input("Function: "))
a = str(input("Left Endpoint: "))
b = str(input("Right Endpoint: "))
"""

def f(x):
    return x**2

#def f(x):
#    return x**2

a = -1
b = 1

def derivative(x):
    h = 1/1000000000
    rise = f(x + h) - f(x)
    run = h
    slope = rise / run
    return slope

print(derivative(-3))
print(derivative(-2))
print(derivative(-1))
print(derivative(0))
print(derivative(1))
print(derivative(2))
print(derivative(3))



def secondderivative(x):
    h = 1/100000
    rise = f(x + h) - f(x)
    run = h
    slope = rise / run
    return slope

#for x in range [a,b]
#    if derivative(x)>0
#        increasing = x
#    elif derivative(x)<0
#        decreasing = x
#    else:
#        store x in critical-points


    
#for x in range [a,b]
#    if derivativetwo(x)>0:
#        store x in concave-up
#    elif derivativetwo(x)<0:
#        store x in concave-down
#    else:
#        store x in inflectionpoint

