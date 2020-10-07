# def bijection(f, x1, x2):
#     if f(x1)*f(x2) > 0:
#         print("No root exist within the given interval.")
#     if f(x1) == 0:
#         print(x1, "is one of the root")
#     if f(x2) == 0:
#         print(x2, "is one of the root")
#     for i in range(0, 100):
#         xh = (x1+x2)/2
#         if y(x1)*y(x2) < 0:
#             x2 == xh
#         else:
#             x1 == xh
#         i == j
#         if abs(y(x1) < 0.000001:
#             i == 100

#     return j, x1

# bijection(F(x), x1, x2)
# F(X)=2*X**2-5*X+3
# x1 == 6
# x2 == 1.2
# print(j, x1)


# from math import sin


# def RFmeth(f, x1, x2, tolerance=1.0e-6, maxfpos=100):
#     xh = 0
#     if f(x1)*f(x2) < 0:
#         fpos = 0
#         for fpos in range(0, maxfpos-1):
#             j = fpos
#             xh = (x2-x1)/(f(x2)-f(x1)) * f(x2)
#             if abs(f(xh)) < tolerance:
#                 fpos = maxfpos-1
#             elif f(x1)*f(xh) < 0:
#                 x2 = xh
#             else:
#                 x1 = xh
#     else:
#         print("No root exist in between the given interval")
#     return xh, j


# x1 = float(input('Enter x1:'))
# x2 = float(input('Enter x2:'))
# def y(x): return x-5


# print(RFmeth(y, x1, x2))
