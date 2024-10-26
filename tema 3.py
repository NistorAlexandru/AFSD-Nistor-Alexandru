meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

for student in studenti[::1]:
    istoric_comenzi.append(studenti.pop(0))

print (dict (zip (istoric_comenzi, comenzi)))
print (studenti)


# COMENZI

# Afisați numele studentului și ce a comandat.
# Eliminați studentul din coadă după ce comanda lui a fost procesată.
# Eliminați tava din stivă odată ce comanda a fost servită.
# Eliminați comanda din coadă.
# Actualizați istoricul comenzilor prin adăugarea fiecărei comenzi în lista istoric_comenzi.
