s = 'XYZ'
k = 2

#DUZE 65-90 male 97-122

def cezar(key, string):
    wynik = ''
    for x in string:
        liczbowo = ord(x) + key
        if ord(x)>64 and ord(x)<91:
            if liczbowo > 90:
                liczbowo = liczbowo % 90 + 64
            elif liczbowo < 65:
                liczbowo = 91 - (65 % liczbowo)
        elif ord(x)>96 and ord(x)<123:
            if liczbowo > 122:
                liczbowo = liczbowo % 122 + 96

            elif liczbowo < 97:
                liczbowo = 123 - (97 % liczbowo)
        czar = chr(liczbowo)
        wynik += czar
    return wynik

zaszyfrowane = cezar(k, s)
print(zaszyfrowane)
print(cezar(-k, zaszyfrowane))
