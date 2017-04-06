f = open("50to1.txt", 'w')
for i in range(1, 51):
	f.write("puzzel " + str(i) +" solution \n")
	with open("out/outtest" + str(i) + ".txt") as g:
		lines = g.readlines()
	for l in lines:
		f.write(l)
	f.write("\n\n")
