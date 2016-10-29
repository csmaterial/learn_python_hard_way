from sys import argv #sys is a software bag,it means take argv out from the bag(sys)

script, filename = argv

print "we're going to erase %r." %filename
print "if you don't want that,hit CTRL-C(^C)."
print "if you do want that, hit RETURN."

raw_input("?")

print "opening the file..."
target = open(filename,'w')#open and start to write

print "truncating the file. Goodbye!"
target.truncate()#truncate means making it shorter

print "now I'm going to ask you for three lines"

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "i'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally we close it."
target.close()
