avail = {
	"statue" : (15, 30000),
	"mask" : (9, 16000),
	"urn" : (8, 15000),
}

limit = 20
takenl = ["mask","urn"]
'''
# this is the long procedure not using the list comprehension
def taken(avail, limit, taken):
	sum = 0
	for x in takenl:
		sum += (avail[x])[0]
	if sum <= limit:
		return True
	else:
		return False
'''
def taken(avail,limit,taken):
	return sum([(avail[x])[0] for x in takenl]) <= limit
	
def taken2(avail, limit, taken):
	return sum([(avail[x])[1]  for x in takenl])

if __name__ == "__main__":
	print taken(avail, limit, taken)
	print taken2(avail, limit, taken)
