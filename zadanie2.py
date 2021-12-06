file = open("osoba.txt")
file2 = open("aboso.txt","w")

dane = file.read()

tabela = dane.split()
print(tabela)

for x in tabela:
    file2.write(x[::-1])
    file2.write("\n")
