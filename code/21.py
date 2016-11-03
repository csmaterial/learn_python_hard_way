# function and return
def add(a,b):
	print "adding %d + %d"% (a, b)
	return a + b
	
def substract(a,b):
	print "substracting %d - %d"% (a, b)
	return a-b
	
def multiply(a, b):
	print "multiply %d * %d"% (a,b)
	return a*b

def divide(a,b):
	print "dividing %d / %d"% (a,b)
	return a/b
	
print "let's do some math with just function"

age = add(30, 5)
height = substract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "age:%d ,height: %d ,weight: %d,iq: %d"% (age, height,weight,iq)

# a puzzle for the extra credit, type it in anyway.
print "here is a puzzle"

what = add(age, substract(height,multiply(weight,divide(iq,2))))

print "that becomes:",what,"can you do it by hand?"

