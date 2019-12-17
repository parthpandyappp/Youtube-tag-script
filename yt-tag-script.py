import sys

#To get input filepath as a cmd line agrument.
infilepath = str(sys.argv[1])

#To get input output filepath as a cmd line agrument.
outfilepath = str(sys.argv[2])

#To open a desired file in read mode.
fin=open(infilepath,'r')

#To open a file to write into it.
fout=open(outfilepath,'w')

#imports content line by line.
line=fin.readline()
while line:
	#implementation of commas at the end of every line in the file.
	fout.write("{},\n".format( line.strip()))
	line = fin.readline()


fin.close()
fout.close()
