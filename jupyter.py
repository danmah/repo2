import random

'''
# Écrire un script qui calcule les 50 premiers termes de la table de multiplication par 13, 
# mais n'affiche que les termes qui sont multiples de 7

d =  [n for n in [i*13 for i in range(1,51)] if n%7 == 0]

# print(d) # Ça fonctionne


def kaprekar(lnum : list, nn : int = 4) -> list :
    if lnum.count(lnum[0]) == nn : # Get out if all numbers are the same!
        return 0
    
    i = 10**(nn+1)
    cible = 6174 if nn==4 else 495 # nn must be 4 or 3
    myFormat = "%04d" if nn==4 else "%03d"
    mylist = lnum 
    nTry = 0 
    while i != cible and nTry < 50 :
        PG = sorted(mylist, reverse=True)
        PP = PG[::-1]
        i = int("".join(PG)) - int("".join(PP))
        mylist = list(myFormat % i)
        nTry += 1
        # print(f"nTry={nTry}, {mylist}")
    return nTry

for k in range(50) :
    depart = random.randint(100,10000)
    nn = 3 if depart < 1000 else 4
    myFormat = "%04d" if nn==4 else "%03d"

    res = kaprekar(list(myFormat % depart), nn)

    print(f"Pour {depart} : {res} essais.")

# Exercice 1
# """Approximation de 'e'."""

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fact(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

# Programme principal =========================================================
n = int(input("n ? "))
exp = 0.0
for i in range(n):
    exp = exp + 1.0/fact(i)

print("Approximation de 'e' : {:.3f}".format(exp))
'''


class Domino(object):
    def __init__(self, val1, val2):
        self.extremite1 = val1
        self.extremite2 = val2

    def appariement(self, autre) -> bool:
        # '''
        # return self.extremite1 == autre_ex.extremite1 or self.extremite2 == autre_ex.extremite1 or \
        #        self.extremite1 == autre_ex.extremite2 or self.extremite2 == autre_ex.extremite2
        # '''
        "Retourne la marque du premier côté apparié trouvé, sinon None."

        for n in (self.extremite1, self.extremite2):
            if n in (autre.extremite1, autre.extremite2):
                return True
        return False

    def __str__(self):
        return f"Ex1={self.extremite1}, Ex2={self.extremite2}"


'''
Jeu = []

for i in range(28) :
    Jeu.append( Domino(random.randint(0,6), random.randint(0,6)))

random.shuffle(Jeu)

Joueur1 = Jeu[:7]
Joueur2 = Jeu[7:14]

for i in range(len(Joueur1)) :
    for j in range(len(Joueur2)) :

        if Joueur1[i].appariement(Joueur2[j]) :
            # print("Appariement")
            print(f"Appariment pour {i} sur {j}, entre <{str(Joueur1[i])}> et <{str(Joueur2[j])}>." )
        else:
            # print("Pas d'appariement.")
            pass

'''

import string
import struct
import difflib


s1 = "Le monde est beau en été sous le joug du président."
s2 = "Le monde est sale en hiver sous le joug du président"

cmp = difflib.SequenceMatcher(None, s1, s2)


print(f"ratio = {cmp.ratio()}")

for b in cmp.get_matching_blocks():
    print(b)

for c in cmp.get_opcodes():
    print(c)

#     print(f"{b} et {b} matchent pour {b} éléments.")

c = 1


print(dir(difflib))


b = 10
d = {'allo'+str(a): b+a for a in range(10)}

print(type(d))


def RamssesII():
    pass


f = list()


def s(y): return "allo" if y < 10 else "bonjour"


f.append(s)
print(f[0](9))


import sys
import io


heureTrav = random.randint(1, 70)
tauxHoraire = random.randint(1, 60) + 100

AccountVentilTuple = (5, ((0.30, "Dan"), (0.10, "Mike"), (0.05, "Joe"), (0.01, "Vic"), (0.54, "Jim")))
Ac2 = (0, 1)
dada = "GIS-1234-C"
dada2 = "GIS-1234-R"

D_AccountList = {}


D_AccountList["GIS-1234-O"] = Ac2
D_AccountList.update({"Moron": Ac2})
D_AccountList.update(Foo=Ac2)
D_AccountList.update(dada=AccountVentilTuple)  # Attention, l'entrée sera indiquée dada dans le dict()
D_AccountList[dada2] = Ac2


# D_AccountList["GIS-1234-O"].append(AccountVentilTuple)

# D_AccountList.setdefault("GIS-1234-P", []).append(AccountVentilTuple)
# # ça fait une liste dont la clé est l'account

print(f"D_AccountList={D_AccountList}.")

print(f"Heures Travaillées : {heureTrav}, Taux: {tauxHoraire}, Ventilation:{AccountVentilTuple}")

'''
first = True 
prefix = ""
with open("ventile.txt", "w") as fout :
    for i in Repartir(heureTrav, tauxHoraire, AccountVentilTuple) :
        fout.write(f"{prefix}{i}")
        if first:
            first = False
            prefix = "\t"
'''


def Repartir(temps: float, taux: float, tventile: tuple) -> tuple:
    for i in range(tventile[0]):
        yield round(temps * taux * tventile[1][i][0], 6), tventile[1][i][1]
    return


s = tuple(k for k in Repartir(heureTrav, tauxHoraire, AccountVentilTuple))
print(s)


def RepartirTuple(temps: float, taux: float, tventile: tuple) -> tuple:
    return tuple((temps * taux * tventile[1][i][0], tventile[1][i][1]) for i in range(tventile[0]))
    # return tuple((round(temps*taux*tventile[1][i][0],6),tventile[1][i][1]) for i in range(tventile[0]))


print(RepartirTuple(heureTrav, tauxHoraire, AccountVentilTuple))


# Fonction anonyme!!!
def RepartirLambda(tventile: tuple) -> tuple:
    return lambda x, y: ((x * y * tventile[1][i][0], tventile[1][i][1]) for i in range(tventile[0]))
    # return lambda x,y :  tuple(((round(x*y*tventile[1][i][0],6),tventile[1][i][1]) for i in range(tventile[0])))


f1 = RepartirLambda(AccountVentilTuple)

for i, j in f1(heureTrav, tauxHoraire):
    print(i, j)


# Fonction anonyme qui utilise un yield alors qu'elle est déjà un itérateur!!!
def RepartirLambdaYield(tventile: tuple):
    yield lambda x, y: ((x * y * tventile[1][i][0], tventile[1][i][1]) for i in range(tventile[0]))
    # return lambda x,y :  tuple(((round(x*y*tventile[1][i][0],6),tventile[1][i][1]) for i in range(tventile[0])))


# f2 = RepartirLambdaYield(AccountVentilTuple)


import itertools

lst = [(1, 'A'), (1, 'B'), (2, 'C')]
dct = dict((key, tuple(v for (k, v) in pairs))
           for (key, pairs) in itertools.groupby(lst, lambda pair: pair[0]))
print(dct)
# {1: ('A', 'B'), 2: ('C',)}
