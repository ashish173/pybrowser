# List of all the items availabla in the meuseum...
# in a dict {name : (weight, cost)}
avail = {
	"statue" : (15, 30000),
	"mask" : (9, 16000),
	"urn" : (8, 15000),
}

limit = 20	#max limit of weight
takenl = ["mask","urn"]		#items chosen
'''
# long procedure not using the list comprehension
def taken(avail, limit, taken):
	sum = 0
	for x in takenl:
		sum += (avail[x])[0]
	if sum <= limit:
		return True
	else:
		return False
'''
def taken(avail,limit,taken):		#List comprehension
	return sum([(avail[x])[0] for x in takenl]) <= limit
	
def taken2(avail, limit, taken):
	return sum([(avail[x])[1]  for x in takenl])

if __name__ == "__main__":
	print taken(avail, limit, taken)
	print taken2(avail, limit, taken)
