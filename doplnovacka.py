"""
doplnovacka.py

Moje kamarádka uèí soukromì nìmèinu. Potøebuje pro klienty pøipravit texty, které se èasem 
nauèí nazpamìò (jedná se o právní pøedpisy). Proto jim pøipravuje stále stejný text, ve kterém vynechá 
nejprve každé 5. slovo, pozdìji každé 4. slovo atd., až se text nauèí zpamìti. Výstupem bude nový soubor.
Pracujte se souborem lorem.py.
Vytvoøte pro ni program, jehož vstupem bude textový soubor a informace, kolikátý znak se má zamìnit.

Rozbor 
naèíst soubor
splitnout slova podle mezery do seznamu
procházet jednotlivá slova seznamu
když se jedná o x-té slovo:
procházet písmenka a:
písmenko nahradit pomlèkou
vynechat interpunkci
upravené slovo pøidat do seznamu
jinak:
pùvodní slovo pøidat do seznamu
seznam spojit pomocí mezery do øetìzce, øetìzec uložit do nového souboru

"""

#1) rozdelit list na seznam 
#2) budem prechadzat prvky seznamu, ked to bude 5 alebo 10, 15, atd slovo, tak: 5 slovo budem chciet nahradit za pomlcky
# bude potrebne vytvorit pomocnu premennu slovo/pravidlo = len (slovo)
# alebo pouzijem cyklus a budem prechadzat znaky (pismenko po pismenku) v tom slovu "slovo/pravidlo += "-"
# vysledek.append (slovo/pr.)
# else: vysledek.append(prvek.seznamu)
#3) vysledek, ktory je ako list budeme musiet spojit so stringu - vysledek -> string -> seznam []


with open ("lorem.txt") as f:
	text = f.read()
f.closed

text = text.repace("  ", " ")
text = text.replace ("\n", "# ")


seznam = []
seznam = text.split(" ")
vysledek = []
interpunkcie = ".,?!-;\""

for i in range(0, len(seznam)):
	slovo = seznam [i]
	slovoUpraveno = ""
	if ((i + 1) % 5 == 0):
		for pismeno in slovo:
			if pismeno in interpunkce:
				slovoUpraveno += "*"
			else:
				slovoUpraveno += pismeno
		vysledek.append(slovoUpraveno)
	else:
		vysledek.append(slovo)

s = " ".join(vysledek)
s = s.replace("# ", "\n")

print(s)