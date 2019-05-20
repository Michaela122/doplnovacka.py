"""
doplnovacka.py

Moje kamar�dka u�� soukrom� n�m�inu. Pot�ebuje pro klienty p�ipravit texty, kter� se �asem 
nau�� nazpam�� (jedn� se o pr�vn� p�edpisy). Proto jim p�ipravuje st�le stejn� text, ve kter�m vynech� 
nejprve ka�d� 5. slovo, pozd�ji ka�d� 4. slovo atd., a� se text nau�� zpam�ti. V�stupem bude nov� soubor.
Pracujte se souborem lorem.py.
Vytvo�te pro ni program, jeho� vstupem bude textov� soubor a informace, kolik�t� znak se m� zam�nit.

Rozbor 
na��st soubor
splitnout slova podle mezery do seznamu
proch�zet jednotliv� slova seznamu
kdy� se jedn� o x-t� slovo:
proch�zet p�smenka a:
p�smenko nahradit poml�kou
vynechat interpunkci
upraven� slovo p�idat do seznamu
jinak:
p�vodn� slovo p�idat do seznamu
seznam spojit pomoc� mezery do �et�zce, �et�zec ulo�it do nov�ho souboru

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