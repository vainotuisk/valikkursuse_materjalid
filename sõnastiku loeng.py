# -*- coding: utf-8 -*-
# Sõnastikud
# Väino Tuisk

# loomine
sonastik = {"Eesti":"Estonia","raamat":"book","auto":"car","meri":"sea"}
hinded ={"A":96,"B":90,"C":76,"D":66,"E":50}
for i in sonastik:
    print i,
print 
eesti = raw_input("Mis sõna tahad tõlkida? ")
print eesti
print (sonastik[eesti])
#lisamine
sonastik["arvuti"] = "computer"
print sonastik
for i in sonastik:
    print i,


