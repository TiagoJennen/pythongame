import turtle
import time
import random

delay = 0,1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake game by Stijn & Tiago")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []