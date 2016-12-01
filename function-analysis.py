"""
Dimitri's Function Analysis Python Program
"""

"""
Inputs
"""

#Inputs where user types in functions and endpoints
function = input("Function: ").replace("^", "**")
a = float(input("Left Endpoint: "))
b = float(input("Right Endpoint: "))

#Formats function input as a mathematical function of x
def f(x):
    return eval(function.replace("x", "("+str(x)+")"))

"""
First Derivative Tests
"""

#Defenition of a derivative
def derivative(x):
    h = 1/1000000
    rise = f(x + h) - f(x)
    run = h
    slope = rise / run
    return slope

#Makes a list of the derivative at every thousandth of a point in the interval
derivative_list = []
for x in range(int(a)*1000, (int(b)*1000)+1):
    r = x/1000
    derivative_list.append([r, derivative(r)])

#Finds critical points in the list, by checking if the values to the left and right of them change sign
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

#Adds endpoints to critical points list
local_extrema.append([b, round(derivative(b), 2)])

#Neatly formats and prints Local Extrema
l_extrema = "Extrema Points (X, Y): "
for ty in local_extrema:
    l_extrema = l_extrema + " (" + str(ty[0]) + ", " + str(round(f(ty[0]), 3)) + ") "
print(l_extrema)

#Identifies increasing and decresing intervals using critical points, by checking first interval then alternating for next intervals
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

#Formats and prints intervals
print(increasing_ivals)
print(decreasing_ivals)


"""
Second Derivative Tests
"""

#Defenition of second derivative using defenition of first
def second(x):
    h = 1/1000000
    rise = derivative(x + h) - derivative(x)
    run = h
    slope = rise / run
    return slope    

#Makes a list of the second derivative at every thousandth of a point in the interval
seconds_list = []
for x in range(int(a)*1000, (int(b)*1000)+1):
    r = x/1000
    seconds_list.append([r, second(r)])

#Finds inflection points in the list, by checking if the values to the left and right of them change sign
inflection_points = [[a, round(second(a), 3)]]
for q in range(1,len(seconds_list)-1):
    this_deriv = seconds_list[q][1]
    if this_deriv > 0:
        prev_deriv = seconds_list[q-1][1]
        next_deriv = seconds_list[q+1][1]
        if next_deriv < 0 and prev_deriv > 0:
            inflection_points.append([round((seconds_list[q+1][0]+seconds_list[q][0])/2, 3), round((next_deriv+this_deriv)/2, 2)])
        if next_deriv > 0 and prev_deriv < 0:
            inflection_points.append([round((seconds_list[q-1][0]+seconds_list[q][0])/2, 3), round((prev_deriv+this_deriv)/2, 2)])
    elif this_deriv == 0:
        prev_deriv = seconds_list[q-1][1]
        next_deriv = seconds_list[q+1][1]
        if next_deriv > 0 and prev_deriv < 0:
            inflection_points.append(seconds_list[q])
        elif next_deriv < 0 and prev_deriv > 0:
            inflection_points.append(seconds_list[q])
inflection_points.append([b, round(second(b), 2)])

#Neatly formats and prints points of inflection
i_points = "Points of Inflection (X, Y): "
for ty in inflection_points:
    i_points = i_points + " (" + str(ty[0]) + ", " + str(round(f(ty[0]), 3)) + ") "
print(i_points)

#Identifies concave up and concave down intervals using points of inflection, by checking first interval then alternating for next intervals
conup = "Concave Up: "
condown = "Concave Down: "
isfinished = False
current_order = 0
while not isfinished:
    ival1 = inflection_points[current_order]
    ival2 = inflection_points[current_order + 1]
    is_increasing = False
    if derivative(ival1[0]) < derivative(ival2[0]):
        is_increasing = True
        conup = conup + " (" + str(ival1[0]) + ", " + str(ival2[0]) + ")"
    else:
        condown = condown + " (" + str(ival1[0]) + ", " + str(ival2[0]) + ")"
    current_order += 1
    if current_order > (len(inflection_points) - 2):
        isfinished = True

#Prints concave up and concave down intervals
print(conup)
print(condown)


