import random

def init_pack():
	pack = []
	for i in range(4):
		for j in range(13):
			pack.append( [i, j] )
	return pack

def run_test():
	n = 0
	n_pairs = 0
	for i in range(100000):
		choice = []
		numbers = []
		pack = init_pack()

		for i in range(5):
			card = random.choice(pack)
			pack.remove(card)
			choice.append(card)
			numbers.append(card[1])

		if len(numbers) != len(set(numbers)):
			n_pairs += 1
		n += 1
	return (n_pairs/float(n))

from pairs_3 import *
acc_prob = count_prob()
print (acc_prob)
results = []
for i in range(10):
	prob = run_test()
	results.append(prob)
	print (i, prob, prob - acc_prob)

avg = sum(results)/len(results)
print (avg, avg - acc_prob)