## Väino Tuisk
## Kliinik 2 - nulliga jagamine ja tulemuse täpsus
jagatav = float(input("sisesta jagatav: "))
jagaja = float(input("sisesta jagaja: "))
if (jagaja == 0):
    print ("viga!")
else:
    print ("Jagatis on: " + str(float(jagatav/jagaja)))
