s = 'AABDCA'
pan_tadeusz = open("pan-tadeusz.txt", "r", encoding='UTF8')
tekst = pan_tadeusz.read().upper()

print(s.count('A'))

print(ord('A'))
print(chr(ord('A')))

alphabet = list(chr(i) for i in range(65, 91))
alphabet.extend(['Ą', 'Ź', 'Ż', 'Ó', 'Ł', 'Ć'])
# print(alphabet)


# result = {'A': 3, 'B': 1, 'C': 1,  E: 0}

def nieoptymalnie():
    dictionary = {}
    for a in alphabet:
        # dictionary[a]=tekst.count(a)
        wyst = 0
        for x in tekst:
            if x == a:
                wyst += 1
        dictionary[a] = wyst

    print(dictionary)


def optymalnie():
    dictionary = {}
    for x in tekst:
        if dictionary.get(x) is None:
            dictionary[x] = 0
        dictionary[x]+=1
    print(dictionary)
# optymalnie()

♦


