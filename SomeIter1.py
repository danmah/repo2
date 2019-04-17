import itertools
import copy
import string

import typing as T

itemAllo = range(5, 15)


def Allo(n: int) -> int:
    nr = len(str("Ok" * n))
    return nr if n > 10 else -nr


j = map(Allo, itemAllo)

myList = copy.deepcopy(j)

# print(dir(myList))

# print(myList)

# for a,i in enumerate(j):  # ça va bien.
#     print(i)

s1 = string.ascii_lowercase
j = itertools.compress(s1, map(lambda y: y % 3, range(len(s1))))  # [1,0,1,0,1,1]) # --> A C E F

# print(j) # çca fonctionne bien

# for i in j:
#     print(i, end=" ")


keys = {'AAPL, {:08d}'.format(i).encode() for i in range(0, 1000, 5)}
print()
# print(keys)

# Vecteur = typing.List[int]

PercolationStruct = T.Dict[int, T.Tuple[int, int, T.List[T.Tuple[int, str]]]]

# {"Account", (NbError, NbTuplesdansLaListe, [ (0.34, "GIS1234-O"), (   ), (   ) ... ]  ) }

# d = StructureComplex


def my_cycle(UneListe: T.List[int]) -> T.Generator[int, None, None]:  # Potentiel de générateur infini # Comme cycle()

    while True:
        for j in UneListe:
            yield j
    return


maListe = [1, 3, 4, 6, 7, 9]

j = 0
for i in my_cycle(maListe):
    j += 1
    print(i, end=" ")
    if j == 500:
        break


# Essai à faire avec typing.Iterable et typing.Sequence

'''
typing.Iterable
typing.Sequence

'''
