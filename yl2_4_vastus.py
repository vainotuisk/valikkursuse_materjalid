# Koosta programm, mis küsib kasutajalt aastaarvu
# ning väljastab ekraanile kas see on liigaasta.

###################################################
# 

# Sisestus konsoolilt	
aasta = input("Sisesta aastaarv: ")

# Liigaasta kontroll
if ((aasta % 4) == 0 and ((aasta % 100) != 0 or (aasta % 400) == 0)):
    print aasta, " on liigaasta."
else:
    print aasta, " ei ole liigaasta."





###################################################
# Mõned vastused:
# 

#2000 on liigaasta.
#1996 on liigaasta.
#1800 ei ole liigaasta.
#2013 ei ole liigaasta.
