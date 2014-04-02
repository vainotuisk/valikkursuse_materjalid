fail = open("luuletus.txt","r")
andmed = fail.read()
##read = andmed.split("\n")
read = fail.readline()
print (read)
##print (andmed)
for i in read:
    print (i)
fail.close()
