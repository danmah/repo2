# Exercice 1 (1)
"""Module de tracé de polygones réguliers avec Turtle."""

# import ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import turtle 



# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def polygone_regulier(ncotes, longueur):
    angle = 360/ncotes
    for i in range(ncotes):
        turtle.forward(longueur)
        turtle.left(angle)


# Auto-test ===================================================================
if __name__=='__main__':
    turtle.width(3)

    polygone_regulier(3, 300)
    polygone_regulier(4, 80)
    polygone_regulier(8, 100)
    polygone_regulier(100, 5)

    turtle.done()
