import math
import My_lib


def function(n):
    return (math.log(n) - math.sin(n))


a = [1.5, 2.5]

if(My_lib.bisection_Root(function, a)):
    print("Root using bisection method = ",
          (abs(a[1] + a[0]) / 2), " +/- ", pow(10, -6)/2)

b = [1.5, 2.5]
if(My_lib.regularfalsi_Root(function, b)):
    print("Root using Regular Falsi = ", b[1], " +/- ", pow(10, -6))

x = 1.5
print("Root using Newton Raphson = ", My_lib.newtonraphson_Root(function, x))


# Output
# Root using bisection method =  2.219107151031494  +/-  5e-07
# Root using Regular Falsi =  2.2191071418525734  +/-  1e-06
# Root using Newton Raphson =  2.219107148913746
