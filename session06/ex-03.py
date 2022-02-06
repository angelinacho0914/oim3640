import turtle
import math

angie = turtle.Turtle()
print(angie)
# turtle.mainloop()

# Exercise 3.1
def shape1(t, n, angle):
    for i in range(n):
        for j in range(4):
            t.fd(100)
            t.lt(90)
        t.rt(angle)


# shape1(angie, 60, 5)


# Exercise 3.2
def shape2(t, n, angle, length):
    for i in range(n):
        for j in range(4):
            t.fd(length)
            t.lt(90)
        length += 4
        t.rt(angle)


# shape2(angie, 60, 5, 30)


# Exercise 3.3
def star(t, n, length):
    angle = 180 - 36  # angle opposite of 36

    t.lt(36)
    for i in range(n):
        for j in range(5):
            t.fd(length)
            t.lt(angle)
        length += 4
        t.rt(10)


# star(angie, 120, 15)


# Exercise 3.4
def shape4(t, r):
    for i in range(120):
        t.circle(r + i, 60)


shape4(angie, 5)
