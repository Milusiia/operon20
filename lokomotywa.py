file = open("lokomotywa.txt", "r")
tekst = file.read()
tekst = tekst.split()

for x in tekst:
    y = (len(x))
    if y%2==1:
        tekst.remove(x)

print(tekst)