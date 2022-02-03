import turtle
import math

leo = turtle.Turtle()
print(
    leo
)  # This tells us that Leo refers to an object with type Turtle as defined in module turle.
# turtle.mainloop()  # Tells the window to wait for the user to do something, although in this case there's not much for the user to do except close the window.

# leo.fd(100) # fd is a distance in pixels
# leo.lt(90)
# leo.fd(100)

# # None function
# def f(x):
#     print("Hi")


# print(f(4))
# # The output of this function is Hi \n none


# # Exercise 1
# for i in range(4):
#     leo.fd(100)
#     leo.lt(90)


# # Exercise 2.1 Encapsulation
# # Wrapping a piece of code up in a function
# def square(t):
#     '''This function takes t parameter, a turtle, and use the turtle 
#         to draw a square'''
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)


# square(leo) # Calling the square function

# raphael = turtle.Turtle()
# square(raphael)


# # Exercise 2.2 Generalization
# # Adding a parameter to a function, makes it more general
# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)

# square(leo, 100)


# # Exercise 2.3
# def polygon(t, n, length):
#     angle = 360 / n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)

# polygon(leo, 7, 70) # Calling the polygon function


# # Exercise 2.4 Interface design
# def circle(t, r):
#     circumference = 2 * math.pi * r
#     n = int(circumference / 3) + 1
#     length = circumference / n
#     polygon(t, n, length)

# circle(leo, 70) # Calling the circle function

# # Refactoring
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n

#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)

# arc(leo, 70, 90) # Calling the arc function


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# polyline(leo, 5, 35, 110)


# Rewriting polygon and arc
def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/3)+1
    step_length = arc_length/n
    step_angle = float(angle)/n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

polygon(leo, 60, 30)
arc(leo, 50, 70)
circle(leo, 60)