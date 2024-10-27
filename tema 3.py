meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

istoric_comenzi_de_printat = []

n = len(studenti)

for n in range(n):
    istoric_comenzi_de_printat.append([studenti[n] + " a comandat " + comenzi[n] ])

for n in range(n+1):
    tavi.pop()
    istoric_comenzi.append(comenzi.pop(0))
    studenti.pop(0)

print(istoric_comenzi_de_printat)
print ("La coada avem " + str(len(studenti))+ " studenti")

print("- au mai ramas " + str(len(tavi)) + " tavi")
print ('- au ramas ' + str(meniu.count('ceafa') - istoric_comenzi.count('ceafa')) + ' portii de ceafa')
print ('- au ramas ' + str(meniu.count('papanasi') - istoric_comenzi.count('papanasi')) + ' portii de papanasi')
print ('- au ramas ' + str(meniu.count('guias') - istoric_comenzi.count('guias')) + ' portii de guias')

update_meniu =[meniu.count('papanasi') - istoric_comenzi.count('papanasi'), meniu.count('ceafa') - istoric_comenzi.count('ceafa'),meniu.count('guias') - istoric_comenzi.count('guias')]

for n in range (3):
    print(' Mai sunt '+ preturi[n][0] + ': ' + str(bool(update_meniu[n]>0)))

incasari = preturi[0][1] * istoric_comenzi.count('papanasi') + preturi[1][1] * istoric_comenzi.count('ceafa') + preturi[2][1] * istoric_comenzi.count('guias')

print("S-au incasat in total: "+ str(incasari) + ' lei')


preturi_filtrate =[]
for element in preturi:
     if element[1] < 8:
        preturi_filtrate.append(element)
print('Preturi de cel mult 7 lei: ',  preturi_filtrate)