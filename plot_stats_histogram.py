import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

dice_rolls = pd.read_csv('dice_rolls461_10000.csv', header=None)

print(dice_rolls.size)
plt.hist(dice_rolls)
plt.xlabel('Character Stats')
plt.ylabel('Number of Instances')
plt.title('Random Character Stats Generator')
plt.show()