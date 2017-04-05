import sys
#create lists 
list_variable = []
list_result = []
file_out = open(sys.argv[1],'w')
def get_possitive_from_minisat_out_put():

	
	num_of_variable = 0
	num_of_clause = 0
	num = ''
	with open("out.txt") as f:
		f.readline()
		for lines in f:
			for ch in lines:
				if ch != " " and ch != "\n":
					num += ch
				
				else:
					#print(num)
					if int(num) > 0:
						#num_of_variable += 1
						list_variable.append(num)
						#print(num_of_variable)
						num = ''
					else:
						num = ''
	#print(list_variable)
	
def convert_to_solve_puzzel():
	list_num = map(int,list_variable)
	count = 0
	printList = ""
	for element in list_num:
		x = element 
		count = count +1
		i = x / 100

		x = x %100
		j = x /10
		x = x %10
		k = x
		#print(str(i) + " " + str(j) + " " + str(k))
		printList += str(k)
		if(count %9 == 0):
			print(printList)
			printList = ""

		list_result.append(k)

	

if __name__ == '__main__':
	get_possitive_from_minisat_out_put()
	convert_to_solve_puzzel()
	count = 1
	for i in list_result:
		if count < 10:
			file_out.write(str(i) + " ")
			count += 1
		else:
			file_out.write("\n")
			file_out.write(str(i) + " ")
			count = 2
	file_out.write("\n")		
