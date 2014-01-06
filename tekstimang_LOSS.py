##
# Väino Tuisk        
# Tekstimäng LOSS


#   Moodusta tühi järjend nimega ruumid
ruumid =[]

# Tee muutuja ruum ja sea see võrduma viieelemendilise järjendiga. Esimene element on ruumi kirjeldus, järgmised 4 on ruumi number kui mängija
# liigub põhja, itta, lõunasse või läände. Kasuta None, kui ruumi pole (mitte jutumärkides). Vajadusel joonista skeem.
ruum = ["Sa oled fuajees. Siin on uks p6hja.",1,None,None,None]

## lisa ruum ruumide järjendisse
ruumid.append(ruum)
ruum = ['Sa oled koridoris. Siin on uks läände ja lõunasse.', None, None,1,1]
ruumid.append(ruum)
# Korda viimaseid tegevusi kõigi ruumide jaoks, mida soovid mängus kasutada.
ruum = ['Sa oled õuduste toas. Siin on uks põhja, läände ja itta.',1,1, None,1]
ruumid.append(ruum)
ruum = ['Sa oled sahvris. Siin on uks itta.', None,1, None,None]
ruumid.append(ruum)
ruum = ['Sa oled verandal. Siin on uks itta ja lõunasse.', None,1,1,None]
ruumid.append(ruum)
ruum = ['Sa oled saalis. Siin on uks läände ja lõunasse.', None, None,1,1]
ruumid.append(ruum)
ruum = ['Sa oled salatoas, leidsid aarde! Siin on uks põhja.', None, None,1,1]
ruumid.append(ruum)

# Tee muutuja asukoht ja sea selle väärtuseks 0.
asukoht = 0

##  Kasutades muutujaid asukoht ja ruumid, väljasta konsoolile selle ruumi andmed, kus parasjagu oled. Tulemus peaks olema midagi sellist:
##  ['Sa oled fuajees. Siin on uks põhja ja itta.', 1, 1, None, None]
print(ruumid[asukoht])
##Muuda väljundit selliselt, et väljastatakse ainult tekst ruumi kohta, mitte järjendi teisi andmeid, nt:
##    "Sa oled fuajees. Siin on uks põhja ja itta."
print(ruumid[asukoht][0])

##Tee muutuja tehtud ja anna sellele väärtuseks False
tehtud = False

##Seejärel pane ruumikirjelduse väljastamine while tsüklisse, mis toimib kuni tehtud saab väärtuseks True
while not tehtud:
    print(ruumid[asukoht][0])

##    Peale ruumi kirjelduse väljastamist, lisa rida, mis küsib kasutajalt mis suunas ta soovib liikuda
    suund = raw_input("Mis suunas soovid edasi liikuda? (n/e/s/w) ")
##    Add an if statement to see if the user wants to go north.
## lisa if-lause, mis kontrollib kas valiti põhjasuund (n)
    if suund == "n":
##    If the user wants to go north, create a variable called next_room and get it equal to room_list[current_room][1],
##                  which should be the number for what room is to the north.
##    Kui kasutaja soovib suunduda põhja (n) siis tee muutuja jargmine_ruum sea see võrduma ruumid[asukoht][1]] mis on põhjasuuna ruumi tähis
        jargmine_ruum = ruumid[asukoht][1]

##    Lisa veel üks if-lause, mis kontrollib kas jargmine_ruum on võrdne None. Kui see on nii siis prindi välja midagi selllist: "Sa ei saa selles suunas minna".
        if jargmine_ruum == "None":
            print("Sa ei saa selles suunas minna.")
            
##    Muul juhul sea asukoht võrduma jargmine_ruum väärtusega
        else:
            asukoht = jargmine_ruum

##  Testi oma programmi, kas saad minna uude ruumi?            

##  Lisa elif-laused ida-, lõuna- ja läänesuuna valikuks. Samuti lisa else-lause juhuks kui programm ei saa aru, mis märk sisestati.           
            

##    Lisa ruume juurde, vähemalt 5. Vajadusel tee joonis, et saada ülevaade ruumide asetusest
    
##  Testi mängu
## Arendusvõimalusi:
##  Lisa mängust väljumise valik, lisa võimalus, et programm töötaks ka suurte tähtedega            




