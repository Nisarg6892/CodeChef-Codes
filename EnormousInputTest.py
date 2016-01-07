string=raw_input()
# string='7 3'
string_int=map(int,string.split())
count=0

for i in range(0,string_int[0]):

	num = raw_input()
	
	if int(num) % 3 == 0: 
		count+=1

print count
