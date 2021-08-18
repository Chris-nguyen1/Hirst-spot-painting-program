import turtle

import colorgram
import turtle
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)

color_list = [(241, 222, 85), (34, 98, 186), (85, 174, 219), (169, 67, 36), (217, 158, 84), (188, 15, 34), (174, 49, 86), (76, 107, 213), (227, 56, 101), (163, 163, 21), (168, 26, 16), (234, 68, 43), (73, 176, 77), (226, 122, 173), (124, 198, 117), (21, 54, 147), (58, 119, 63), (117, 226, 183), (71, 30, 43), (134, 216, 233), (239, 157, 218), (40, 173, 186), (29, 41, 85), (243, 174, 151), (162, 164, 237), (90, 31, 22)]

timmy = turtle.Turtle()
# timmy.penup()
# timmy.setpos(-250, -150)
# position = timmy.pos()[1]
turtle.colormode(255)


def dots():
    for i in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)


def paint():
    timmy.speed('fastest')
    timmy.hideturtle()
    timmy.penup()
    timmy.setpos(-250, -200)
    position = timmy.pos()[1]
    for x in range(10):
        dots()
        position += 50
        timmy.setpos(-250, position)


paint()




screen = turtle.Screen()
screen.exitonclick()