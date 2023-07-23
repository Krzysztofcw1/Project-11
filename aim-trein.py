import turtle
import random
import time


tim = turtle.Turtle()
tim.color("red")
tim.shape("square")
tim.penup()
colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "white",
    "pink",
    "cyan",
    "magenta",
    "gold",
    "silver",
    "darkgreen",
    "darkblue",
    "lightblue",
    "violet",
    "indigo"
]
trafienia = []

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("aim-train")
screen.tracer(0)


def wynik(czas):
    trafione = 0
    nie_trafione = 0

    for shot in trafienia:
        if shot == 1:
            trafione += 1
        else:
            nie_trafione += 1

    print("Koniec Gry!!!")
    print(f"Trafione: {trafione}")
    print(f"Nie trafione: {nie_trafione}")
    print(f"trafiasz: {round(trafione/int(czas), 2)} na sekundę")


def random_pos():
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    tim.goto(x, y)


def random_color():
    tim.color(random.choice(colors))


def cheack_click(x, y):
    if tim.distance(x, y) <= 13:
        trafienia.append(1)
        random_pos()
        random_color()
    else:
        trafienia.append(0)


print("Witaj w aim-train!")
czas = input("Poadj ile sekud chcesz  (po wpisaniu będziesz mieał 6 sekund na przygotowanie się): ")
while not czas.isdigit():
    czas = input("Poadj ile sekud chcesz grać: ")
time.sleep(6)
future_tiem = time.time() + int(czas)

screen.onscreenclick(cheack_click)
while time.time() <= future_tiem:
    screen.update()
else:
    wynik(czas)
