def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)

    print (indices)

    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1

        print (indices[i])
        print (indices)

        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


pack = [0,1,2,3,4,5]
s = combinations('ABCD', 2)
for ss in s:
	print (ss)


# s = combinations('ABCD', 2)
# for ss in s:
# 	print (ss)