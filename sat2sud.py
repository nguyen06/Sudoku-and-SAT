import re
f = open('out.cnf', 'r')
 
f.readline()
numbers = " " + f.readline()
li = []
li = re.findall(' \d+',numbers)
 
counter = 0
for i in li:
    li[counter] = i[1:]
    counter += 1
li.pop()
print li
print len(li)
 
pout = open('puzzleout.txt','w')
x = int(li[0])
counter = 0
for x in li:
	x = int(x)
	counter = counter + 1
	i = x / 100
	i = i
	x = x % 100
	j = x / 10
	j = j
	x = x % 10
	k = x
	pout.write(str(k))
	if(counter % 9 == 0):
		pout.write('\n')
pout.close()
