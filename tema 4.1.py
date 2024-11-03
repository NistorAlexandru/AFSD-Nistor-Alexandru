import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ['_' for i in range(len(cuvant_de_ghicit))]
print(' '.join(progres))
end_game = False
incercari = 6
caractere_permise = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','x','y','z']

while not end_game:
    litera = input('\n Alege o litera : ')
    if litera in progres:
      print(f'\n ai ales deja litera {litera}')
    if litera not in caractere_permise:
        print(f'\n introdu un caracter valid')
    for j in range(len(cuvant_de_ghicit)):
        if litera in cuvant_de_ghicit[j]:
            progres[j] = litera
    print(f'\n{" ".join(progres) }\n')
    if litera in caractere_permise and litera not in cuvant_de_ghicit:
        incercari-=1
        print(f' Litera {litera} nu e in cuvant \n Incercari ramase: {incercari}')
        if incercari == 0 :

            print(f'Ai pierdut! Cuvântul era: {cuvant_de_ghicit}')
            end_game = True

    if '_' not in progres:
        end_game = True
        print('Felicitări! Ai ghicit cuvântul!')