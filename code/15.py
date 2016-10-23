from sys import argv #sys is a software bag,it means take argv out from the bag(sys)

script, filename = argv

txt = open(filename)

print "here's your file %r:"% filename
print txt.read()

print "type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
