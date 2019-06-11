from random import sample

roosters = 4  #aantal roosters
nummers = [] 
sterren = []

for i in range(1, roosters+1):
    nummers = sorted(sample(range(1, 51), 6 ))
    sterren = sorted(sample(range(1, 13), 2))
    print("forumulier" + str(i) + ": " + str(nummers) + ',' + str(sterren))
