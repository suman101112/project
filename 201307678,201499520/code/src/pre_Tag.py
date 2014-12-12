import re
#import glob
#file="../Data/Hindi_PreTagged.txt"
file="../Data/Marathi_PreTagged.txt"
f=open("%s"%file,"w")
#rang=("01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25")
rang = ("01")
for fc in rang:
    l=0
	#filename="./Hindi_Marathi/hin_health_set%s.txt"%fc
    filename="../Hindi_Marathi/mar_health_set%s.txt"%fc
    for line in open(filename,"r"):
        l+=1
        if not l==1:
            words=line.split()
            for each in words[1:]:
                word=each.split('\\')
                f.write(word[0]+"_")
                if len(word)==2:
                    tag=word[1].split("_")
		#if len(tag)==2:
                    f.write(tag[0]+" ")
                
            f.write("\n")
##    print fc," file ",l," lines"
fc=0
for fc in rang:
    l=0
	#filename="./Hindi_Marathi/hin_tourism_set%s.txt"%fc
    filename="../Hindi_Marathi/mar_tourism_set%s.txt"%fc
    for line in open(filename,"r"):
        l+=1
        if not l==1:
            words=line.split()
        	#if len(words)>2:
            for each in words[1:]:
                word=each.split('\\')
                f.write(word[0]+"_")
                if len(word)==2:
                    tag=word[1].split("_")
		#if len(tag)==2:
                    f.write(tag[0]+" ")
            f.write("\n")
##    print fc," file ",l," lines"
f.close()
print "preprocessing '"+ str(file)+ "' done... ", fc,"files"
