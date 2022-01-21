#Kenny Ruan, TE20D, 
#Moment 04 A
#Frågar användaren om Sidorna
sida_1 = int(input("Sida 1:"))
sida_2 = int(input("Sida 2:"))
#Räknar ut Arean
area = sida_1 * sida_2
print(area)
#Den säger att det är en kvadrat, eftersom båda sidorna är lika långa.
if sida_1 == sida_2:
    print("Det blev en kvadrat")
else:
    pass
#räknar ut volymen
for loop in range(11):
    volymen = sida_1 * sida_2 * loop
    print(volymen)