﻿##
# Väino Tuisk        
# Tekstimäng LOSS
# -*- coding: utf-8 -*-

#   Moodusta tühi järjend nimega ruumid
ruumid =[]

# Tee muutuja ruum ja sea see võrduma viieelemendilise järjendiga. Esimene element on ruumi kirjeldus, järgmised 4 on ruumi number kui mängija
# liigub põhja, itta, lõunasse või läände. Kasuta None, kui ruumi pole (mitte jutumärkides). Vajadusel joonista skeem.
ruum = ["Esik",1,2,3,4]

##    Append this room to the room list.
# lisa ruum ruumide järjendisse
ruumid.append(ruum)
ruum = ['Sa oled fuajees. Siin on uks põhja ja itta.', 1, 1, None, None]
ruumid.append(ruum)
# Korda viimaseid tegevusi kõigi ruumide jaoks, mida soovid mängus kasutada.

##    Create a variable called current_room. Set it to zero.
# Tee muutuja asukoht ja sea selle väärtuseks 0.
asukoht = 0

##  Kasutades muutujaid asukoht ja ruumid, väljasta konsoolile selle ruumi andmed, kus parasjagu oled. Tulemus peaks olema midagi sellist:
##  ['Sa oled fuajees. Siin on uks põhja ja itta.', 1, 1, None, None]
print(ruumid[asukoht+1])
lokk=input("mis")
##Muuda väljundit selliselt, et väljastatakse ainult tekst ruumi kohta, mitte järjendi teisi andmeid, nt:
##    "Sa oled fuajees. Siin on uks põhja ja itta."
##    Create a variable called done and set it to False. Then put the printing of the room description in a while loop that repeats until done is set to True.
##    After printing the room description, add a line of code that asks the user what direction they wish to go.
##    Add an if statement to see if the user wants to go north.
##    If the user wants to go north, create a variable called next_room and get it equal to room_list[current_room][1], which should be the number for what room is to the north.
##    Add another if statement to see if the next room is equal to None. If it is, print “You can't go that way.” Otherwise set current_room equal to next_room.
##    Test your program. Can you go north to a new room?
##    Add elif statements to handle east, south, and west. Add an else statement to let the user know the program doesn't understand what she typed.
##    Add several rooms, at least five. It may be necessary to draw out the rooms and room numbers to keep everything straight. Test out the game. You can use \n or triple quotes if you have a multi-line room description.
##    Optional: Add a quit command. Make sure that the program works for upper and lower case directions. Have the program work if the user types in “north” or “n”. 



