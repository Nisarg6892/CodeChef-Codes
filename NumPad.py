t=int(raw_input())
# t=1
dict = {'1':' ','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '}

for x in range(0,t):
	
	string = raw_input()
	temp=0
	last=''
	l=[]

	for x in range (0, len(string)) :

		if string[x] == last :
			l.pop()
			temp+=1
			l.append(dict.get(string[x])[temp])
		else :
			temp=0
			l.append(dict.get(string[x])[temp])
			
		# print dict.get(string[x])[temp]
		last=string[x]
		

	print ''.join(l)