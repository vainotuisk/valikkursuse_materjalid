## Failioperatsioonid
## Väino Tuisk

##fail = open("luuletus.txt","r")
##andmed = fail.read()
##read = andmed.split("\n")
####print (andmed)
##for i in read:
##    print (i)
##fail.close()

fail = open("valjund.txt","w")
fail.write("Esimene rida \n")
print ("Esimene rida")
fail.write("Teine rida")
print ("Teine rida")
fail.close()
