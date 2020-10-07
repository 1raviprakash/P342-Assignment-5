import math
import My_lib


def function(x):
    return (- x - math.cos(x))


a = [-1.2, 0.2]

if(My_lib.bisection_Root(function, a)):
    print("Root using bisection method = ",
          ((a[1] + a[0]) / 2), " +/- ", pow(10, -6)/2)

b = [-1.2, 0.2]
if(My_lib.regularfalsi_Root(function, b)):
    print("Root using Regular Falsi = ", b[1], " +/- ", pow(10, -6))

x = -1.2
print("Root using Newton Raphson = ", My_lib.newtonraphson_Root(function, x))


# Output
# Root using bisection method =  -0.7390852451324463  +/-  5e-07
# Root using Regular Falsi =  -0.7390851015096833  +/-  1e-06
# Root using Newton Raphson =  -0.7390851332151607
