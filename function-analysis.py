
function = input("Function: ").replace("^", "**")
a = input("Left Endpoint: ")
b = input("Right Endpoint: ")

def f(x):
    return eval(function.replace("x", str(x)))

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

print(derivative(-1))






"""
print(round(derivative(-3),5))
print(round(derivative(-2),5))
print(round(derivative(-1),5))
print(round(derivative(0),5))
print(round(derivative(1),5))
print(round(derivative(2),5))
print(round(derivative(3),5))
"""

def second(x):
    h = 1/1000000000
    top = derivative(x + h) - derivative(x)
    bottom = h
    answers = top / bottom
    return answers

#print(second(-1))

"""
def secondderivative(x):
    h = 1/1000000000
    rise = f(x + h + h) - f(x + h) - f(x + h) + f(x)
    rise2 = (f(x + (2*h))) - (2*(f(x + h))) + f(x)
    first = f(x + h) + f(x + h)
    first2 = -2 * f(x + h) + f(x + 2*h) - f(x)
    run = h*h
    slope = first2 / run
    return slope

print(secondderivative(-1))
"""
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

