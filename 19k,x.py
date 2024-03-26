from turtle import *
def f(n):
    if n==0:
        pensize(6)
        color("green")
        dot(10)
        return
    left(20)
    forward(30*n)
    f(n-1)
    pensize(4)
    backward(30*n)
    right(40)
    forward(30 * n)
    f(n-1)
    pensize(4)
    backward(30 * n)













