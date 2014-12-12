name="marathi_100sentences"
f_Qi="../Intermediate_Data/%s_QIs.txt"%name
f_In="../Intermediate_Data/%s_tokenized.txt"%name
f_Out="../../Results/%s_Tagged.txt"%name
f_pretag="../Input/%s_PreTagged.txt"%name

Q={}
l=0
## Reading all Qi s values... & getting most probable tags...
for line in open(f_Qi,"r"):
    key=line.split()[0]
    l+=1
    pro=0.0
    for word in line.split()[1:]:
        word=word.split("_")
        if float(word[1])>float(pro):
            tag=word[0]
            pro=word[1]
    Q[key]=tag

##for q,t in Q.items():
##    print q+"-"+t

## Assigning Tags to target language sentences....
f=open(f_Out,"w")
for line in open(f_In,"r"):
    for word in line.split():
        if word in Q:
            f.write(word+"_"+Q[word]+" ")
        else:
            f.write(word+"_UNK ")
    f.write("\n")
f.close()

## Calculating Tagging Accuracy.....
total=0
corct=0
New=open(f_Out)
Prv=open(f_pretag)
line_N=next(New)
line_P=next(Prv)
ln=0
while line_N and line_P and ln<99:
    ln+=1
    lN=line_N.split()
    lP=line_P.split()
    #if len(lN)==len(lP):
    for i in range(len(lN)):
        #print ln," ",i
        if lN[i]==lP[i]:
            corct+=1
        total+=1
    line_N=next(New)
    line_P=next(Prv)

accr=(float(corct)/total)*100
accr=float("{0:.2f}".format(accr))
print "Tagging done with ",accr,"% Accuracy..."
