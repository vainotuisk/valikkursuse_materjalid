
##Merlin-Eliise Salus
##See on programm, mis küsib kasutajalt ridade ning kohtade arvu, siis kuvab istekohtade plaani.
##Pean tõdema, et erinevate versioonide kasutamine on segadusse ajav: 3.0 ja 2.7 juures on print-i kasutamine väga segadusse ajav. Tegin kõik nii nagu tunnis, kuid kodus vanema versiooniga läks reavahetus aia taha.



rida = input("Sisestage ridade arv: ")
koht = input("Sisestage kohtade arv: ")
tulem = ""

for i in range(rida):
    for j in range (1, koht+1):
        tulem+=str(j) + ' '
    tulem+= '\n'

print tulem
