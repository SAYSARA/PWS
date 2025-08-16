print("Hello, welcome to PWS! (Paint With a Square) Here in the console you will be able to see the coordinates you can press R to reset")
Color_S = input("Please choose a color for the square (Red, Orange, Yellow, Green, Blue, Black): ")

import turtle
import tkinter as tk
import os

root = tk.Tk()
ancho = root.winfo_screenwidth()
alto = root.winfo_screenheight()
root.destroy()

X = 0
Y = 0
en_movimiento = False

win = turtle.Screen()
win.title("PWS")
win.bgcolor("white")
win.setup(width=ancho, height=alto)

cuadrado = turtle.Turtle()
cuadrado.shape("square")
cuadrado.color(Color_S)
cuadrado.penup()
cuadrado.goto(X, Y)
cuadrado.pendown()

def mover(dx, dy):
    global X, Y, en_movimiento
    if en_movimiento:
        return
    en_movimiento = True
    X += dx
    Y += dy
    cuadrado.goto(X, Y)
    print(f"Coordenadas: X={X}, Y={Y}")
    win.ontimer(desbloquear, 100)

def desbloquear():
    global en_movimiento
    en_movimiento = False

def mover_arriba(): mover(0, 50)
def mover_abajo(): mover(0, -50)
def mover_derecha(): mover(50, 0)
def mover_izquierda(): mover(-50, 0)

def reset():
    global X, Y, en_movimiento
    X = 0
    Y = 0
    en_movimiento = False

    cuadrado.clear()
    cuadrado.penup()
    cuadrado.goto(X, Y)
    cuadrado.setheading(0)
    cuadrado.color(Color_S)
    cuadrado.pendown()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Reset")

win.listen()
win.onkey(mover_arriba, "Up")
win.onkey(mover_abajo, "Down")
win.onkey(mover_derecha, "Right")
win.onkey(mover_izquierda, "Left")
win.onkey(reset, "r")

turtle.done()
