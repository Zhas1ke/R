def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def init_pack(n_colors=4,length=13):
	pack = []
	for i in range(n_colors):
		for j in range(length):
			pack.append( [i, j] )
	return pack


def count_prob():
	n = 0
	n_pairs = 0
	n_colors = 4
	length = 13
	pack = init_pack(n_colors, length)

	combs = [list(x) for x in combinations(pack, 5)]
	for choice in combs:
		numbers = []
		for card in choice:
			numbers.append(card[1])
		n += 1
		if len(numbers) != len(set(numbers)):
			n_pairs += 1
	print (n_pairs)
	return n_pairs/float(n)