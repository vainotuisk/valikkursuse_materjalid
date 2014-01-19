## Väino Tuisk
## Funktsioon
##
## Ülesanne 6_2
## Loo funktsioon, mis trükib sellele argumendina etteantud nime alusel lause
## "Euroopa üks pealinnadest on //NIMI//". Kasutades loodud Euroopa pealinnade järjendit,
## kutsu see funktsioon välja iga pealinna puhul.

eurolinnad = ["Pariis","London","Riia","Tallinn","Vilnius","Brüssel"]  

def valjasta_yks_linnadest(linn): # funktsioon defineeritakse enne selle kasutamist
    return("Euroopa üks pealinnadest on " + linn + ".")

for linn in eurolinnad: #tsükli abil funkstiooni väljakutsumine iga järjendi elemendiga
    print (valjasta_yks_linnadest(linn))
