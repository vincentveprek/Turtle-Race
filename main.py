from turtle import *
from random import randint
speed(100)
penup()
goto(-140, 140)

for step in range(16):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-140,120)

da = Turtle()
da.color('blue')
da.shape('turtle')
da.penup()
da.goto(-140,80)
b.penup()
b.goto(-140, 0)

finish = 160
while True:
  step = randint(1, 3)
  ada.forward(step)
  step = randint(1, 3)
  da.forward(step)
  step = randint(1, 3)


a = Turtle()
a.color('black')
a.shape('turtle')
a.penup()
a.goto(-140,40)

b = Turtle()
b.color('green')
b.shape('turtle')
  a.forward(step)
  step = randint(1, 3)
  b.forward(step)
  if (ada.position()[0] > finish or
    da.position()[0] > finish or
    a.position()[0] > finish or
    b.position()[0] > finish):
    break
