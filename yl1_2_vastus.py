## Kirjuta Pythoni avaldis, mis arvutab mitu sekundit on 7h, 21min ja 37 sek.
###################################################
# Testid
# Eemalda kommentaar ainult ühetl testikomplektilt ja kontrolli tulenust

# Test 1 - 
tunde = 7
minuteid = 21
sekundeid = 37


# Test 2 
#tunde = 10
#minuteid = 1
#sekundeid = 7


# Test 3 
#tunde = 1
#minuteid = 0
#sekundeid = 1


###################################################
# Sisesta avaldis siia:
sekundeid_kokku = (tunde * 60 + minuteid) * 60 + sekundeid

###################################################
# Testi väljund
# Ära muuda järgnevat koodi

print str(tunde) + " tundi, " + str(minuteid) + " minutit  ja",
print str(sekundeid) + " sekundit on " + str(sekundeid_kokku) + " sekundit."


###################################################
# Vastused:

# Test 1:

#7 tundi, 21 minutit ja 37 sekundit on 26497 sekundit.

# Test 2:
#10 tundi, 1 minutit ja 7 sekundit on 36067 sekundit.

# Test 3 output:
#1 tundi, 0 minutit ja 1 sekundit on 3601 sekundit.
