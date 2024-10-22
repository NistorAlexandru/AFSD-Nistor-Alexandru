my_text="""Inaintea duelului direct, finalista Champions League din sezonul trecut ocupă poziția a 7-a în clasament, cu 10 puncte înregistrate, în timp ce oaspeții sunt pe locul al 15-lea, la egalitate de puncte cu Hoffenheim (4 puncte), care este pe loc de baraj pentru divizia secundă.

În ultima etapă dinaintea pauzei pentru meciurile echipelor naționale, "Galbenii" au pierdut partida din deplasare cu Union Berlin, scor 1-2.

De cealaltă parte, St. Pauli a înregistrat la rândul lor un eșec pe teren propriu, cu Mainz, scor 0-3 ."""

lungimea = len(my_text)
print("lungimea textului este")
print(lungimea)

my_text_partea_intai = my_text[:262:1]
my_text_partea_intai = my_text_partea_intai.upper()
my_text_partea_intai = my_text_partea_intai.strip()

my_text_partea_a_doua = my_text[262::]
my_text_partea_a_doua = my_text_partea_a_doua [262::-1]
my_text_partea_a_doua = my_text_partea_a_doua [0:1].upper() + my_text_partea_a_doua[1:len(my_text_partea_a_doua)-1]

my_text_partea_a_doua = my_text_partea_a_doua.replace(".","" )
my_text_partea_a_doua = my_text_partea_a_doua.replace(",","" )
my_text_partea_a_doua = my_text_partea_a_doua.replace("!","" )
my_text_partea_a_doua = my_text_partea_a_doua.replace("?","" )

my_text_final = my_text_partea_intai + my_text_partea_a_doua
print(my_text_final)

