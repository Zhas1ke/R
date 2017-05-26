def init_pack(n_colors=4,length=4):
	pack = []
	for i in range(n_colors):
		for j in range(length):
			pack.append( [i, j] )
	return pack

n = 0
n_pairs = 0

n_colors = 4
length = 4
pack = init_pack(n_colors, length)
# print (len(pack))
# exit()
numbers = []
choice = []

for i1 in range(len(pack)):
	choice1= pack[i1]
	choice.append(choice1)
	numbers.append(choice1[1])
	pack.remove(choice1)

	for i2 in range(len(pack)):
		choice2 = pack[i2]
		choice.append(choice2)
		numbers.append(choice2[1])
		pack.remove(choice2)

		for i3 in range(len(pack)):
			choice3 = pack[i3]
			choice.append(choice3)
			numbers.append(choice3[1])
			pack.remove(choice3)

			for i4 in range(len(pack)):
				choice4 = pack[i4]
				choice.append(choice4)
				numbers.append(choice4[1])
				pack.remove(choice4)

				for i5 in range(len(pack)):
					choice5 = pack[i5]
					choice.append(choice5)
					numbers.append(choice5[1])
					pack.remove(choice5)

					if len(numbers) != len(set(numbers)):
						n_pairs += 1
					n+=1
					# print (i1,i2,i3,i4,i5)
					pack = init_pack(n_colors, length)
					numbers = []
					choice = []

print (n)
print (n_pairs)
print (n_pairs/float(n))
print (i1,i2,i3,i4,i5)