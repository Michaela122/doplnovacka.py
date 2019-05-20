with open("lorem.txt") as f:
	text = f.read()
f.closed

hviezdicka = int(input("Zadaj ko¾ké slovo bude nahradené hviezdièkou. ")
text = text.replace("\n", "# ")

seznam = []
seznam = text.split(" ")
print(seznam)
vysledek = []
interpunkcie = ",.!-;\""

for i in range(0, len(seznam)):
	slovo = seznam[i]
	slovoUpraveno = ""
	if ((i + 1) % hviezdicka ==0):
		for pismeno in slovo:
			if pismeno not in interpunkcie:
				slovoUpraveno += "*"
		else:
			slovoUpraveno +=pismeno
		vysledek.append(slovoUpraveno)
	else:
		vysledek.append(slovo)

s = " ".join(vysledek)
s = s.replace("# ", "\n")
print(s)