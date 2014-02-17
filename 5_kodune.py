## Väino Tuisk
## Telefoniraamatu moodustamine
## Valikkursuse 5. kodune ülesanne
run = True
raamat = {}
while run:
    nimi = input("Sisesta nimi, lõpetamiseks sisesta q: ")
    if nimi == "q":
        run = False
    else:
        nummer = input("sisesta number: ")
        raamat[nimi] = nummer
for key in raamat:
    print(key,raamat[key]) 

                   
