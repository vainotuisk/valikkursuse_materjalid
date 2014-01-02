# Kirjuta Pythoni programm mis leiab kahe punkti vahelise kauguse.
# Punktide koordinaadid on (x0, y0) ja (x1, y1).

###################################################
# Testid
# Eemalda kommentaar ainult ühetl testikomplektilt ja kontrolli tulenust

# Test 1 
x0 = 2
y0 = 2
x1 = 5
y1 = 6


# Test 2
#x0 = 1
#y0 = 1
#x1 = 2
#y1 = 2


# Test 3 
#x0 = 0
#y0 = 0
#x1 = 3
#y1 = 4


###################################################
# Sisesta avaldis:
kaugus = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5


###################################################
# Väljund
# 

print "Punktide (" + str(x0) + ", " + str(y0) + ") ja ", 
print "(" + str(x1) + ", " + str(y1) + ") vaheline kaugus on " + str(kaugus) + "."


###################################################
# Vastused
# 

# Test 1:
#Punktide (2, 2) ja  (5, 6) vaheline kaugus on 5.0.

# Test 2:
# Punktide ((1, 1) ja (2, 2) vaheline kaugus on 1.41421356237.


# Test 3:
# Punktide 0, 0) ja (3, 4) vaheline kaugus on 5.0.

