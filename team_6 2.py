def add(a,b):
    return a + b 

print "The first number you want to add?" 
a = int(raw_input("First no: "))
print "What's the second number you want to add"
b = int(raw_input("Second no: "))

result = add(a,b)
"""
This function adds two numbers
"""
print "The result is: %r." % result
"""
this prints the results
"""
def sub(a,b):
    return a - b 

print "The first number you want to subtract?" 
a = int(raw_input("First no: "))
print "What's the second number you want to subtract"
b = int(raw_input("Second no: "))
"""
This function subtracts two numbers
"""
result = sub(a,b)
"""
this prints the results
"""
print "The result is: %r." % result

def opp(a):
    return a * -1

print "Number you want to change"
a = int(raw_input("Number to change: "))

result = opp(a)
"""
This function changes the sign of the number
"""
print "The result is: %r." % result 
"""
this prints the results
"""
