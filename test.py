f = open("95.sh", 'w')
for i in range(1, 96):
	f.write("python top95.py 95/puzzle" + str(i) + ".txt \n")
	f.write ("minisat cnf_format.cnf out.txt \n")
	f.write("python sat2su.py 95_out/out" + str(i) + ".txt \n")
	f.write("\n")