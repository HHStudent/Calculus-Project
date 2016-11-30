"""
Dimitri's Function Analysis Python Program
"""

function = input("Function: ").replace("^", "**")
#a = float(input("Left Endpoint: "))
#b = float(input("Right Endpoint: "))
#print(function.replace("x", "("+str(-1.0)+")"))
#print(eval(function.replace("x", "("+str(-1.0)+")")))

def f(x):
    return eval(function.replace("x", "("+str(x)+")"))

a = -1.0
b = 1.0

"""
First Derivative Tests
"""

def derivative(x):
    h = 1/1000000
    rise = f(x + h) - f(x)
    run = h
    slope = rise / run
    return slope

derivative_list = []

for x in range(int(a)*1000, (int(b)*1000)+1):
    r = x/1000
    derivative_list.append([r, derivative(r)])

local_extrema = [[a, round(derivative(a), 3)]]
for q in range(1,len(derivative_list)-1):
    this_deriv = derivative_list[q][1]
    if this_deriv > 0:
        prev_deriv = derivative_list[q-1][1]
        next_deriv = derivative_list[q+1][1]
        if next_deriv < 0 and prev_deriv > 0:
            local_extrema.append([round((derivative_list[q+1][0]+derivative_list[q][0])/2, 3), round((next_deriv+this_deriv)/2, 2)])
        if next_deriv > 0 and prev_deriv < 0:
            local_extrema.append([round((derivative_list[q-1][0]+derivative_list[q][0])/2, 3), round((prev_deriv+this_deriv)/2, 2)])
    elif this_deriv == 0:
        prev_deriv = derivative_list[q-1][1]
        next_deriv = derivative_list[q+1][1]
        if next_deriv > 0 and prev_deriv < 0:
            local_extrema.append(derivative_list[q])
        elif next_deriv < 0 and prev_deriv > 0:
            local_extrema.append(derivative_list[q])


local_extrema.append([b, round(derivative(b), 2)])

l_extrema = "Extrema Points (X, Y): "
for ty in local_extrema:
    l_extrema = l_extrema + " (" + str(ty[0]) + ", " + str(round(f(ty[0]), 3)) + ") "
print(l_extrema)

increasing_ivals = "Increasing: "
decreasing_ivals = "Decreasing: "
isdone = False
current_index = 0
while not isdone:
    ival1 = local_extrema[current_index]
    ival2 = local_extrema[current_index + 1]
    is_increasing = False
    if f(ival1[0]) < f(ival2[0]):
        is_increasing = True
        increasing_ivals = increasing_ivals + " [" + str(ival1[0]) + ", " + str(ival2[0]) + "]"
    else:
        decreasing_ivals = decreasing_ivals + " [" + str(ival1[0]) + ", " + str(ival2[0]) + "]"
    current_index += 1
    if current_index > (len(local_extrema) - 2):
        isdone = True

print(increasing_ivals)
print(decreasing_ivals)


"""
Second Derivative Tests
"""

def second(x):
    h = 1/1000000
    rise = derivative(x + h) - derivative(x)
    run = h
    slope = rise / run
    return slope    

seconds_list = []

for x in range(int(a)*1000, (int(b)*1000)+1):
    r = x/1000
    seconds_list.append([r, second(r)])

inflection_points = [[a, round(derivative(a), 3)]]
for q in range(1, len(seconds_list)-1):
    this_second = seconds_list[q][1]
    if this_second > 0:
        prev_second = seconds_list[q-1][1]
        next_second = seconds_list[q+1][1]
        if next_deriv > 0 and prev_deriv < 0:
            inflection_points.append([round((seconds_list[q+1][0]+seconds_list[q][0])/2, 3),round((next_second+this_second)/2, 3)])
        if next_deriv < 0 and prev_deriv > 0:
            inflection_points.append([round((seconds_list[q-1][0]+seconds_list[q][0])/2, 3),round((prev_second+this_second)/2, 3)])
    elif this_second == 0:
        prev_second = seconds_list[q-1][1]
        next_second = seconds_list[q+1][1]
        if next_deriv > 0 and prev_deriv < 0:
            inflection_points.append(seconds_list[q])
        if next_deriv < 0 and prev_deriv > 0:
            inflection_points.append(seconds_list[q])

inflection_points.append([b, round(derivative(b), 3)])

i_points = "Points of Inflection (X, Y): "
for ty in inflection_points:
    i_points = i_points + " (" + str(ty[0]) + ", " + str(round(f(ty[0]), 3)) + ") "
print(i_points)


#print(seconds_list)
