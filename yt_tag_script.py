import sys

#To get filepath as a cmd line agrument.
filepath = str(sys.argv[1])

#To open a desired file in read mode.
fin=open(filepath,'r')

#To open a file to write into it.
fout=open("new.csv",'w')

#imports content line by line.
line=fin.readline()
while line:
	#implementation of commas at the end of every line in the file.
	fout.write("{},\n".format( line.strip()))
	line = fin.readline()


fin.close()
fout.close()