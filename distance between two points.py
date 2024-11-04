def distance_between_points(x1, y1, x2, y2):
    """
    Input: (x1, y1) and (x2, y2), the coordinates of two points on a Cartesian grid
    Prints the distance between the two points
    """
    result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print("The distance between the points is:", str(result))

 # Example for points (5,0) and (2,4)
distance_between_points(8, 0, 2, 4) 
