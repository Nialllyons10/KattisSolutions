one = raw_input()
line = raw_input()
nums = [int(s) for s in line.split()]
count = 0
for num in nums:
	if num < 0:
		count = count + 1

print(count)
