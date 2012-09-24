#!usr/bin/python
import timeit

t = timeit.Timer(stmt= """
chart = {}
def memfibo(n):
	if n in chart:
		return chart[n]
	elif n<=2:
		chart[n]=1 
	else:	
		chart[n] = memfibo(n-1) + memfibo(n-2)
	return chart[n] 


#if __name__ == "__main__":
#	num = input("Enter the number: ")
	print memfibo(25)
""")

print t.timeit(number = 100)




