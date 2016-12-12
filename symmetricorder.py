set = 1
while (True):
	num = int(raw_input())
	if num == 0:
		break

	count = 0
	inc_list = []
	dec_list = []
	for _ in range(num):
		if count % 2 == 0:
			inc_list.append(raw_input())
		else:
			dec_list.insert(0, raw_input())
		count += 1

	inc_list.extend(dec_list)
	print "SET " + str(set)
	set += 1
	for i in range(len(inc_list)):
		print inc_list[i]
