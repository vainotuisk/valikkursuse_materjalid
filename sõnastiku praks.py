# -*- coding: utf-8 -*-
# Sõnastikud
# Väino Tuisk

sonastik = {"janku":[(100,250),"red","mjau.vaw"],"raamat":"book","auto":"car","meri":"sea"}
hinded ={"A":96,"B":90,"C":76,"D":66,"E":50}
for i in sonastik:
    print (i,end = " ")
print (" ")
eesti = input("mis sõna tõlkida? ")
print (sonastik[eesti])
##print ("")
##print (sonastik["auto"])
##sonastik["hiir"] = "mouse"
##for i in sonastik:
##    print (i,end = " ")
##del sonastik["raamat"]
##print ("")
##for i in sonastik:
##    print (i,end = " ")
print (sonastik["janku"][2])

