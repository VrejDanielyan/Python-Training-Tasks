# 20. Function to check if given point (coordinate, tuple) is in triangle (by coordinates of 3 tops)

a = (0, 0)
b = (10, 30)
c = (20, 0)
p = (30, 15)

if (a[0] > p[0] or b[0] > p[0] or c[0] > p[0]) and (a[1] > p[1] or b[1] > p[1] or c[1] > p[1]):
    print(True)
else:
    print(False)
