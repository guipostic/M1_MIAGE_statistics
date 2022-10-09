import random

def add_x_dices_y(x, y): # ajout de x dés à y faces
    total = 0
    for dice in range(x):
        total+=random.randrange(1,y+1)
    return total


for i in (2, 3, 4, 5, 10, 100): # i est le nombre de dés
    filename = str(i)+".txt"
    with open(filename, 'w') as fileout:
        for roll in range(10000): # nombre de lancers
            fileout.write(str(add_x_dices_y(i, 6))+"\n")
