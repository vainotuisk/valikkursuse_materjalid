##
# V2ino Tuisk        
# Tekstim2ng LOSS


#   Moodusta tu'hi j2rjend nimega ruumid
ruumid =[]

# Tee muutuja ruum ja sea see v6rduma viieelemendilise j2rjendiga. Esimene element on ruumi kirjeldus, j2rgmised 4 on ruumi number kui m2ngija
# liigub p6hja, itta, l6unasse v6i l22nde. Kasuta None, kui ruumi pole (mitte jutum2rkides). Vajadusel joonista skeem.
ruum = ["Sa oled fuajees, saad ennast peeglitest imetleda.\nSiin on uks p6hja.",1,None,None,None]

## lisa ruum ruumide j2rjendisse
ruumid.append(ruum)
ruum = ['Sa oled koridoris, p2ris hubane koht aga kitsas.\nSiin on uks l22nde ja l6unasse.', None, None,1,1]
ruumid.append(ruum)
# Korda viimaseid tegevusi k6igi ruumide jaoks, mida soovid m2ngus kasutada.
ruum = ['Sa oled 6uduste toas ja v2ga 6udne olla.\n Siin on uks p6hja, l22nde ja itta.',1,1, None,1]
ruumid.append(ruum)
ruum = ['Sa oled sahvris, riiulitel on moosi ja suitsuvorsti.\nSiin on uks itta.', None,1, None,None]
ruumid.append(ruum)
ruum = ['Sa oled verandal, p2ike paistab ja vaade on suurep2rane.\nSiin on uks itta ja l6unasse.', None,1,1,None]
ruumid.append(ruum)
ruum = ['Sa oled saalis, klaver on h22lest 2ra ja pildid on igavad.\nSiin on uks l22nde ja l6unasse.', None, None,1,1]
ruumid.append(ruum)
ruum = ['Sa oled salatoas, leidsid aarde!\nSiin on uks p6hja.', None, None,1,1]
ruumid.append(ruum)
print ruumid
# Tee muutuja asukoht ja sea selle v22rtuseks 0.
asukoht = 0

##  Kasutades muutujaid asukoht ja ruumid, v2ljasta konsoolile selle ruumi andmed, kus parasjagu oled. Tulemus peaks olema midagi sellist:
##  ['Sa oled fuajees. Siin on uks p6hja ja itta.', 1, 1, None, None]
print(ruumid[asukoht])
##Muuda v2ljundit selliselt, et v2ljastatakse ainult tekst ruumi kohta, mitte j2rjendi teisi andmeid, nt:
##    "Sa oled fuajees. Siin on uks p6hja ja itta."
print(ruumid[asukoht][0])

##Tee muutuja tehtud ja anna sellele v22rtuseks False
tehtud = False

##Seej2rel pane ruumikirjelduse v2ljastamine while tsu'klisse, mis toimib kuni tehtud saab v22rtuseks True
while not tehtud:
    print(ruumid[asukoht][0])

##    Peale ruumi kirjelduse v2ljastamist, lisa rida, mis ku'sib kasutajalt mis suunas ta soovib liikuda
    suund = raw_input("\nMis suunas soovid edasi liikuda? (n/e/s/w) ")
##    Add an if statement to see if the user wants to go north.
## lisa if-lause, mis kontrollib kas valiti p6hjasuund (n)
    if suund == "n":
##    If the user wants to go north, create a variable called next_room and get it equal to room_list[current_room][1],
##                  which should be the number for what room is to the north.
##    Kui kasutaja soovib suunduda p6hja (n) siis tee muutuja jargmine_ruum sea see v6rduma ruumid[asukoht][1]] mis on p6hjasuuna ruumi t2his
        jargmine_ruum = ruumid[asukoht][1]

##    Lisa veel u'ks if-lause, mis kontrollib kas jargmine_ruum on v6rdne None. Kui see on nii siis prindi v2lja midagi selllist: "Sa ei saa selles suunas minna".
        if jargmine_ruum == "None":
            print("Sa ei saa selles suunas minna.")
            
##    Muul juhul sea asukoht v6rduma jargmine_ruum v22rtusega
        else:
            asukoht = jargmine_ruum

##  Testi oma programmi, kas saad minna uude ruumi?            

##  Lisa elif-laused ida-, l6una- ja l22nesuuna valikuks. Samuti lisa else-lause juhuks kui programm ei saa aru, mis m2rk sisestati.
    elif suund == "e":
        jargmine_ruum = ruumid[asukoht][2]
        if jargmine_ruum == "None":
            print("Sa ei saa selles suunas minna.")
        else:
            asukoht = jargmine_ruum
    elif suund == "s":
        jargmine_ruum = ruumid[asukoht][3]
        if jargmine_ruum == "None":
            print("Sa ei saa selles suunas minna.")
        else:
            asukoht = jargmine_ruum
    elif suund == "w":
        jargmine_ruum = ruumid[asukoht][4]
        if jargmine_ruum == "None":
            print("Sa ei saa selles suunas minna.")
        else:
            asukoht = jargmine_ruum
    else:
        print("Ei saanud sinust aru.")

##    Lisa ruume juurde, v2hemalt 5. Vajadusel tee joonis, et saada u'levaade ruumide asetusest
    
##  Testi m2ngu
## Arendusv6imalusi:
##  Lisa m2ngust v2ljumise valik, lisa v6imalus, et programm to'o'taks ka suurte t2htedega            




