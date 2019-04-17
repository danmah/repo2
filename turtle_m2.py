# Exercice 1 (2)
"""Tracé de polygones avec Turtle."""

# Import ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import turtle
from turtle_m import polygone_regulier

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def polygones(npoly, ncotes, longueur):
    turtle.width(3)
    rot = 360 / npoly
    for i in range(npoly):
        polygone_regulier(ncotes, longueur)
        turtle.left(rot)


def uneautre_Figure():
    turtle.color('purple', 'cyan')
    turtle.width(1)
    turtle.begin_fill()

    while True:
        turtle.forward(400)
        turtle.right(170)
        if abs(turtle.pos()) < 1:
            break

    turtle.end_fill()


# programme principal =========================================================

#  polygones(10, 3, 150)

uneautre_Figure()

turtle.done()
