# Väino Tuisk
# Faktoriaali leidmine
fakt = 1 # korrutamisel alati algväärtus 1
algne = n = 5 # algne hoiab esialgset arvu
while (n > 1):
    fakt *= n
    n -= 1    
print ("Arvu " + str(algne) + " faktoriaal on " + str(fakt))
