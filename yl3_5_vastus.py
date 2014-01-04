##
# Väino Tuisk        
# Kordused for ja while
# Harjutuse 5 lahendus

## Koosta mäng, kus saate ära arvata salajase arvu ühest kahekümneni.

salajane_arv = 7

sisestatud_arv = -1 # anname esialgu muutujale mingi väärtuse
print("Mõtlesin ühele arvule 1-20ni, mis arv see on?")
while(sisestatud_arv < salajane_arv) or (sisestatud_arv > salajane_arv):
# korratakse kuni sisestatakse õige arv    
    sisestatud_arv = input(" ") # sisestusele eelneb tühik lihtsalt ilu pärast :)
    if (sisestatud_arv < salajane_arv):
        print("Arv on suurem, proovi uuesti.")
    elif(sisestatud_arv > salajane_arv):
        print("Arv on väiksem, proovi uuesti.")
#  while-tsüklist väljumisel:     
print("Tubli, arvasid ära. Arv oli " + str(sisestatud_arv) +".")
