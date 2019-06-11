from random import sample

roosters = 4  #aantal roosters
max_keuzes = 6
max_getal = 45
nummers = []

for i in range(1, roosters+1):
    nummers = sorted(sample(range(1, max_getal + 1), max_keuzes ))
    print("forumulier" + str(i) + ": " + str(nummers))
