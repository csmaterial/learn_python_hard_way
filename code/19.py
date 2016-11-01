#function and via
def cheese_and_crackers(cheese_count,boxes_of_crackers):#crackers:cookies , boom
	print "you have %d cheeses!"% cheese_count
	print "you have %d boxes of crackers"% boxes_of_crackers
	print "man that;s for a party"
	print "get a blanket"
	
print "we can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "or,we can use variable from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "we can even do math inside too:"
cheese_and_crackers(10 + 20, 5 +6) #n+n can be used  

print "and we can combine the two,variables and math:"
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000) #via + numbers is useful 
