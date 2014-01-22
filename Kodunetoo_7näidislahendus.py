## Väino Tuisk
## Valikkurususe 7. koduse töö näidislahendus
## Ülesanne:
##    Koosta programm mis loeb failist andmed.txt 4 arvu: ridade arvu saalis,
##    kohtade arvu reas, sinu istekoha rea ja istekoha numbri reas.
##    Arvud võivad olla failis eraldi ridadel. Tulemusena väljastatakse faili tulemus.txt
##    saali plaan (nagu 3. nädala ülesandes), kus istekohtad on märgitud mingi märgiga
##    (mitte numbriga) ja etteantud istekoht on saalis märgistatud erineva sümboliga.

fail =open("andmed.txt","r")
andmed = fail.read() # andmed loetakse muutujasse
fail.close()
fail = open("tulemus.txt","w")

andmed = andmed.split("\n") # moodustatakse järjend ridadest

ridade_arv = int(andmed[0]) # need muutujad pole vajalikud, kuid aitavad koodi mõista
toolide_arv = int( andmed[1])
rida = int(andmed[2])
koht = int(andmed[3])
tulemus = "" # see muutuja hoiab tulemuse sõne
for i in range(ridade_arv):
    for j in range(toolide_arv):
        if i == rida +1 and j == koht + 1: # NB! Järjendi indeks!
            print("X ",end ="") # ka konsoolile väljastatakse kontrolli mõttes
            tulemus += "X "
        else:
            print(". ",end ="")
            tulemus += ". "
    print()
    tulemus += "\n"
fail.write(tulemus)
fail.close()

    
    

