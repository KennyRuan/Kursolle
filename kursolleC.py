#Kenny Ruan, TE20D, 
#Moment 04 C
#funktion för kvadraten
def kvadrat(sida_1,sida_2):
    if sida_1 == sida_2:
        kvadrat = "ja det är en kvadrat "
    else:
        kvadrat = "nej det är inte en kvadrat"
    return kvadrat

#Funktion för area
def area(sida_1,sida_2):
    area = sida_1 * sida_2
    return area

#Listor
kvadrat_lista = []
sida_1_lista = []
sida_2_lista = []
area_lista = []
Variabel = 0


#While 
while True:
    user_answer = str(input("Vill du göra beräkningen (ja eller nej)?:"))
    if user_answer == "nej":
        break

    while True:
        try:
            height = int(input("höjden: "))
            break
        except:
            print("Det ska vara heltal")

    if height < 0:

        height = 1

    elif height > 10:

        height = 10
       

    Variabel += 1
    #Frågar användaren om sidornas längd
    sida1 = int(input("Sida 1:"))
    sida2 = int(input("Sida 2:"))

    #lägger till sida1 i sida_1_lista, och Sida2 i sida_2_lista
    sida_1_lista.append(sida1)
    sida_2_lista.append(sida2)
    area_lista.append(area(sida1,sida2))

    kvadrat_lista.append(kvadrat(sida1,sida2))
    print(f"{kvadrat(sida1,sida2)} kvadrat")

    #samma som A
    for loop in range(11):
        volymen = loop * sida1 * sida2
        print(volymen)

#detta printas efter du tackar nej(samma som A)
for looper in range(Variabel):
    print(f"{looper} Den har sidorna {sida_1_lista[looper]} {sida_2_lista[looper]} och om det är en kvadrat? {kvadrat_lista[looper]}. arean blev {area_lista[looper]}.")