def gener(word, key):
    szyfr = ""
    for i in range(len(word)):
        kod = ord(word[i]) + ord(key[i % len(key)]) - 65
        szyfr += chr(kod)
    return szyfr


def deszyfr(word, key):
    zdeszyfrowane = ""
    for i, elem in enumerate(word):
        kod = ord(elem) - ord(key[i % len(key)]) + 65
        zdeszyfrowane += chr(kod)
    return zdeszyfrowane


key = "KOT"
zaszyfrowane = gener("CECHA", key)
zdeszyfr = deszyfr(zaszyfrowane, key)
print('wynik:', zaszyfrowane, zdeszyfr)
