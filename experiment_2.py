import random
import numpy as np

n = 50000

def randomizer_choiser():
	summer = 0
	cases = ['best best', 'best', 'most likely', 'most likely','most likely', 'most likely', 'worst', 'worst worst']
	cases_score  = [[4,5,6,6,6,6,7,8],[5,6,7,7,7,7,8,9],[2,3,4,4,4,4,5,6]]
	for j in range(3):
		choice = random.randint(0,7)
		summer += cases_score[j][choice]
	return summer

stat = [0]*24

for i in range(n):
	s = randomizer_choiser()
	stat[s] +=1
print (stat)

print (np.cumsum(stat)/500.0)