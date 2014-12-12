import re
import glob
listt=""
file="Marathi.txt"
##def pre_hin(file):
f=open("%s"%file,"w")

fc=0
for filename in glob.glob("./Hindi_Marathi/mar*.txt"):
    fc+=1
    l=0
    for line in open(filename,"r"):
        l+=1
        words=line.split()
        if len(words)>2:
            for each in words[1:]:
                word=each.split('\\')
                f.write(word[0]+" ")
            f.write("\n")
    print fc," file ",l," lines"
f.close()
print "preprocessing '"+ str(file)+ "' done... ", fc,"files"
