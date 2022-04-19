class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

# my_point = Point()
# my_point.x = 3
# my_point.y = 4
# print(my_point.x)


import math
 
# print(f'({my_point.x},{my_point.y})')
# distance = math.sqrt(my_point.x**2 + my_point.y**2)
# print(distance)


def print_point(p):
    print(f'({p.x},{p.y})')

# print_point(my_point)


# Checking whether an object has a particular attribute:
# print(hasattr(my_point, 'x'))
# print(hasattr(my_point, 'z'))


def distance_between_points(x, y):
    point1 = Point()
    # point1.x = x
    # point1.y = y

    # print(f'({point1.x},{point1.y})')
    distance = math.sqrt(x**2 + y**2)
    return distance

# print(distance_between_points(3, 4))


class Rectangle:
    """Represents a rectangle. 
    attributes: width, height, corner.
    """
# box = Rectangle()
# box.width = 100.0
# box.height = 200.0
# box.corner = Point()
# box.corner.x = 0.0
# box.corner.y = 0.0


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

# center = find_center(box)
# print_point(center)


# Objects are mutable
# box.width = box.width + 50
# box.height = box.height + 100


# Can also write functions to modify objects
def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

# print(box.width)
# print(box.height)
# print('grow')
# grow_rectangle(box, 50, 100)
# print(box.width)
# print(box.height)


# Copying
# p1 = Point()
# p1.x = 3.0
# p1.y = 4.0

# import copy
# p2 = copy.copy(p1)

# print_point(p1)
# print_point(p2)

# Python doesn't know for programmer_defined types, what should be considered equivalent
# print(p1 is p2)
# print(p1 == p2)
