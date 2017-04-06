f = open("95to1.txt", 'w')
for i in range(1, 96):
	f.write("Puzzel " + str(i) +" solution \n")
	with open("95_out/out" + str(i) + ".txt") as g:
		lines = g.readlines()
	for l in lines:
		f.write(l)
	f.write("\n\n")
