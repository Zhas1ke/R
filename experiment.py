import random

n = 100000

def randomizer_choiser():
	summer = 0
	cases = ['best best', 'best', 'most likely', 'most likely','most likely', 'most likely', 'worst', 'worst worst']
	cases_score  = [[4,6,8],[5,7,9],[2,4,6]]
	for j in range(3):
		choice = random.choice(cases)
		if choice == 'best':
			summer += cases_score[j][0]
		if choice == 'most likely':
			summer += cases_score[j][1]
		if choice == 'worst':
			summer += cases_score[j][2]
	return summer

stat = [0]*24

for i in range(n):
	s = randomizer_choiser()
	stat[s] +=1
print (stat)