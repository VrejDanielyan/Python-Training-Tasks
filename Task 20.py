# 20. Function to check if given point (coordinate, tuple) is in triangle (by coordinates of 3 tops)

def check_triangle():
    A = (0,0)
    B = (10,30)
    C = (20, 0)
    points = (5, 15)

    if (A[0] > points[0] or B[0] > points[0] or C[0] > points[0]) and (A[1] > points[1] or B[1] > points[1] or C[1] > points[1]):
        print("The points lies inside the triangle")
    else:
        print("The points lies outside the triangle")
check_triangle()

