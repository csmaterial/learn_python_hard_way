#function
#this one is like your scripts with argv
def print_two(*args):  #*args is taking all the 
	arg1,arg2 = args
	print "arg1: %r, arg2:%r"% (arg1,arg2)
	
#ok,that *args is actually pointless, we can just do this 
def prin_two_again(arg1,arg2):    #() must be follow the fuction name
	print "arg1: %r, arg2:%r"% (arg1, arg2)
	
#this just takes one argument
def print_one(arg1):
	print "arg1: %r"% arg1

#this onen takes no arguments
def print_none():
	print "I got nothin"
	
print_two("zed","shaw")
prin_two_again("zed","shaw")
print_one ("first!")
print_none()
