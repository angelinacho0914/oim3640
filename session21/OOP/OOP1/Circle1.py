from Point1 import Point, Rectangle, distance_between_points, print_point
import copy


class Circle:
    """Represents a circle.

    Attributes: center, radius
    """


def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary).

    point: Point object
    circle: Circle object
    """
    d = distance_between_points(point, circle)
    print(d)
    # return true if d <= circle.radius


def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    point1 = copy.copy(rect.corner)
    # print_point(point1)   # Checking
    if not point_in_circle(point1, circle):
        return False

    point1.x += rect.width
    # print_point(point1)
    if not point_in_circle(point1, circle):
        return False

    point1.y -= rect.height
    if not point_in_circle(point1, circle):
        return False

    point1.x -= rect.width
    if not point_in_circle(point1, circle):
        return False
    
    return True


def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """


def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    # print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    # print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()
