import math
import My_lib

c = [1, -3, -7, 27, -18]


def polynomial(c, i, x):
    return ((c[0-i] * pow(x, 4))+(c[1-i] * pow(x, 3))+(c[2-i] * pow(x, 2))+(c[3-i] * pow(x, 1))+c[4-i])


a0 = 10
r = []
My_lib.synthetic_Division(polynomial, c, a0, r)

print("Roots of the Polynomial are : ")
for i in range(len(r)):
    print(r[i])
if(c[0] > 0):
    print(-c[1])
else:
    print(c[1])


# OUTPUT
# Roots of the Polynomial are :
# 3.000000352399201
# 1.9999992184518156
# 1.000000454591186
# -3.0000000254422026
