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
    '''Print the point in human readable format.'''
    print(f'({p.x},{p.y})')

# print_point(my_point)


# Checking whether an object has a particular attribute:
# print(hasattr(my_point, 'x'))
# print(hasattr(my_point, 'z'))


def distance_between_points(x, y):
    '''
    Computes the distance between two Point objects.
    '''
    p1_d = y.x - x.x
    p2_d = y.y - x.y
    distance = math.sqrt(p1_d**2 + p2_d**2)
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
    '''
    Find the center point of a rectagle.
    '''
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


def print_rectangle(rect):
    '''
    Print out the width, height, and lower-left corner of the Rectangle.
    '''
    print(f'width: {rect.width}, height: {rect.height}')
    print('the lower-left corner: ')
    print_point(rect.corner)
