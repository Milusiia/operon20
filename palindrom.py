liczba = input("podaj liczbe: ")
num1 = []
for x in liczba:
    num1.append(x)
for y in liczba:
    num2 = num1[::-1]
if num1 == num2:
     print("liczba jest palindromem")
else:
    print("liczba nie jest palindromem")


