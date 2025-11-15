file1=input ("Enter the source file to be copied:")
file2=input ("Enter the destination file name:")

Fr=open (file1,"r")

Fw=open(file2,"w")

for line in Fr.readlines():
   Fw.write(line)
#close the file
Fr.close()
Fw.close()


