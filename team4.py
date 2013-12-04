#JP #Taylor #Ceasar #Dane

def log10(x):
	"""
	Taking a number, giving it a base and raising it to a power is log
	"""
	temp = x
	count = 0
	while temp >= 10:
		temp = temp / 10
		count += 1
	return count
	
def fib(n):
	"""
	using the % sign you can divide and find out the remainder
	"""
	a, b = 0,1
	wile b < n:
		print b,
		a, b = b, a+b
		
def fib2(n):
	result = []
	a, b =0, 1
	while b < n :
		result.apprnd(b)
		a, b = b, a+b
	return result