# Tähekaupa väljastamine
sona = raw_input("Sisesta sõna? ") # versioonist 3 alates, kasuta input
i = 1
for taht in sona:  # sõne on ühtlasi järjend ja sealt saab tähti vaadelda elementidena
    valjund = str(i)+". täht on: " + taht
    print valjund
    i += 1


