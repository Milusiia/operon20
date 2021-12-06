file = open("liczby.txt","w")

for x in range(1,2001):
    if x%2==0:
        file.write(str(x))
        file.write("\n")
file.close()