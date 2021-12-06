file = open("osoba.txt","w")
dane = "Oliwia Sieradzka 3c"
tabela = dane.split()
for x in tabela:
    file.write(x)
    file.write("\n")
file.close()

