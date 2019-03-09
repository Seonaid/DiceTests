import random
import csv

def roll_dice(num_dice, sides, discards=0):
    random.seed()
    all_dice=[random.randint(1,sides) for dice in range(num_dice)]
    for i in range(discards):
        all_dice.remove(min(all_dice))
    
    return sum(all_dice)



num_dice = 4
sides = 6
discards = 1
num_rolls = 10000
all_rolls = [roll_dice(num_dice, sides, discards) for dice in range(num_rolls)]
filename='dice_rolls%d%d%d_%d.csv' %(num_dice, sides, discards, num_rolls)
with open(filename, 'w') as current_rolls:
    wr = csv.writer(current_rolls)
    wr.writerow(all_rolls)