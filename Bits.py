my_input = int(raw_input())

for tc in xrange(my_input):
	new_input = raw_input()
	emptystr = ''
	count = 0
	for i in xrange(len(new_input)):
		emptystr += new_input[i]
		bins = bin(int(n))[2:]
		ones = sum([int(x) for x in bins])
		count = max(ones, count)
	print(m)
