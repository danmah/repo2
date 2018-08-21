# Exercice 1 (2)
"""Tracé de polygones avec Turtle."""

# Import ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import turtle
from turtle_m import polygone_regulier

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def polygones(npoly, ncotes, longueur):
    rot = 360 / npoly
    for i in range(npoly):
        polygone_regulier(ncotes, longueur)
        turtle.left(rot)

# programme principal =========================================================
turtle.width(3)

polygones(10, 3, 150)

turtle.done()