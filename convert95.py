
in_file = open("top95.txt",'r')
counter = 1
for line in in_file:
	out_file =open("./95/puzzle" + str(counter) + ".txt", 'w')
	out_file.write(line)
	counter += 1
	out_file.close()



