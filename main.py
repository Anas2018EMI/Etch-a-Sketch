from turtle import Turtle, Screen

s=Screen()
t=Turtle()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_right():
    t.right(5)

def turn_left():
    t.left(5)

s.listen()
s.onkey(move_forward, 'z')
s.onkey(move_backward, 's')
s.onkey(turn_right, 'd')
s.onkey(turn_left, 'q')
s.onkey(t.clear, 'c')


s.exitonclick()