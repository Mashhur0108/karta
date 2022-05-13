import random
karta=['6♥','7♥','8♥','9♥','10♥','valet♥','dama♥','karol♥','tuz♥','6♣','7♣','8♣','9♣','10♣','valet♣','dama♣','karol♣','tuz♣','6♦','7♦','8♦','9♦','10♦','valet♦','dama♦','karol♦','tuz♦','6♠','7♠','8♠','9♠','10♠','valet♠','dama♠','karol♠','tuz♠']
partiya=[]
user=[]
comp=[]
a= random.choice(karta)
print(a)
for k in karta:
	partiya.append(k)
	karta.remove(k)
for k in range(6):
	user.append(partiya[k])
	comp.append(partiya[k*2+1])

print(comp)
while True:
	yurish=input()
	if
	pass