f = open('sud', "r+")

#change 100 to be the number of lines in this file
for i in range(1,10):
	for j in range (1,10):
		for k in range (1,10):
			f.write(str(i) + str(j) + str(k) + " ")
		f.write("0\n")


for i in range(1, 10):
	for k in range(1, 10):
		for j in range(1,9):
			for l in range(j+1, 10):
				x = -100 * i - 10 * j - k
				y =  -100 * i - 10 * l - k
				f.write(str(x) + " " + str(y) + " 0\n")

for j in range(1, 10):
	for k in range(1, 10):
		for i in range(1,9):
			for l in range(i+1, 10):
				x = -100 * i - 10 * j - k
				y =  -100 * l - 10 * j - k
				f.write(str(x) + " " + str(y) + " 0\n")

for k in range (1,10):
	for a in range(0,3):
		for b in range (0,3):
			for u in range (1,4):
				for v in range(1,3):
					for w in range(v+1,4):
						x = -(((3*a+u)*100) +(3*b +v) * 10 + k) 
						y = -((3*a+u)*100+(3*b+w)*10+k)
						f.write(str(x) + " " + str(y) +  " 0\n")

for k in range (1,10):
	for a in range(0,3):
		for b in range (0,3):
			for u in range (1,3):
				for v in range(1,4):
					for w in range(u+1,4):
						for t in range(1,4):
							x = -((3*a+u)*100 + (3*b+v)*10 +k )
							y = -((3*a + w)*100 + (3*b+t)*10 + k)
							f.write(str(x) + " " + str(y) + " 0\n")


pf = open('puzzle.txt', 'r')

puzzle = list()	

while True:
	ch = pf.read(1)
	if ch == '\n': continue
	puzzle.append(ch)
	if not ch: break
puzzle.pop()	
print len(puzzle)
##
for i in range(0, 9):
	for j in range(0, 9):
		index = i*9 + j
		k = puzzle[index]
		if str(k) == '0':
			continue
		#print "i is: %d j is:  %d  k is: %d\n\n" %(i,j,int(k))
		xx = (100 * i + 10 *j + int(k) + 110)
		f.write(str(xx) + " 0\n")

f.close()
total_line_count = sum(1 for line in open("sud"))
file = open('sud2', 'w')

file.write("p cnf " + " 999 " + str(total_line_count) + "\n")
f.close()

with open('sud') as f:
	lines = f.readlines()

for l in lines:
	file.write(l)
