# string=raw_input()
string='30 120.00'
money=map(float,string.split())

if (money[0]>money[1]) or money[0]%5!=0 :
	# print 'hi'
	print '%.2f' %money[1]
else:
	print '%.2f' %(money[1]-money[0]-0.5)