import sys
my_dict = {}

my_input = raw_input()
while my_input != '':
	splitted_input = my_input.split()
	my_dict[splitted_input[1]] = splitted_input[0]
	my_input = raw_input()

lines = sys.stdin.readlines()
for line in lines:
	if line[:-1] in my_dict:
		print my_dict[line[:-1]]
	else:
		print 'eh'
