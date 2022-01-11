from random import randint
import random

la = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# alfabet = ["A", "B", "C", "D", "E", "F"]
print(la)


def los():
    los = randint(0, len(la) - 1)
    return los


def alf():
    for x in range(30):
        a = los()
        b = los()
        print(a, b)
        la[a], la[b] = la[b], la[a]


alf()
print(la)


l = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
random.shuffle(l)
print(l)
