#copy one file to the other
from sys import argv #sys is a software bag,it means take argv out from the bag(sys)

from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s." % (from_file, to_file)

#we could do these two on one line too,how?
in_file = open(from_file)
indata = in_file.read()

print "the input file is %d Bytes long "% len(indata)

print "does the output file exist?%r"% exists(to_file) #exists is testing whether the file is existings
print "ready,hit return to continue,ctrl-c to abort"
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "alright, all done"

out_file.close()
in_file.close()
