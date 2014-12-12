import collections

name="marathi_100sentences"
fileSmlr="../Intermediate_Data/%s_Simlr.txt"%name
File_Nbr="../Intermediate_Data/%s_Nbr.txt"%name
File_5Nbr="../Intermediate_Data/%s_5Nbr.txt"%name
F_cntr="../Intermediate_Data/%s_Centers.txt"%name

print "Filtering unique center word trigrams....."
CNbr=collections.OrderedDict()
c=0
Cntr=collections.OrderedDict()
C=collections.OrderedDict()
d=0
r=open(F_cntr,"w")
for evry in open("../Intermediate_Data/%s_tri_grams.txt"%name,"r"):
    evry=evry.split()
    if not evry[1] in Cntr:
        Cntr[evry[1]]=d
        CNbr[d]=[]
        r.write(evry[1])
        r.write("\n")
        d+=1
    CNbr[Cntr[evry[1]]].append(c)
    C[c]=evry[1]
    c+=1
r.close()

print "Finding closest Neighbours of each word..."
FNbr=open(File_Nbr,"w")
l=0     ## Trigram Counter
S=[]    ## Reverse Sorted Similarity Scores
for each in open(fileSmlr,"r"):
    FNbr.write(C[l])
    l+=1
    each=map(float,each.split())
    S=sorted(each,reverse=True)
    S=S[1:6]
    Nbr=[]      ## Neighbour indices
    NbrW=[]     ## Neighbour Scores
    W=[]        ## Neighbour words
    for i in S:
        if not i==0.0:
            NbrW.append(i)
            m=each.index(i)
            Nbr.append(m)
            W.append(C[m])
    for k in range(len(NbrW)):
        FNbr.write(" ")
        FNbr.write(W[k])
        FNbr.write("_")
        FNbr.write(str(NbrW[k]))
        FNbr.write(" ")
    FNbr.write("\n")
FNbr.close()

print "Combining common center word Trigram's Similarity Scores..."
F_5Nbr=open(File_5Nbr,"w")
All_Nbrs=open(File_Nbr,"r").readlines()
All_Nbrs=[i.rstrip() for i in All_Nbrs]
wrds=[]
Q=""
for i in range(0,len(CNbr)):
    Top_Nbr=[]
    for e in CNbr[i]:
        if not e==11932:
            Q=All_Nbrs[e].split()[0]
            wrds=All_Nbrs[e].split()[1:]
        for k in wrds:
            Top_Nbr.append(k)
    Top_Nbr.sort(key=lambda x: (float(x.split("_")[1])),reverse=True)
    c=0
    R=[]
    F_5Nbr.write(Q)
    F_5Nbr.write("#")
    for k in Top_Nbr:
        if c<min(5,len(Top_Nbr)):
            N=k.split("_")[0]
            X=float(k.split("_")[1])
            X=float("{0:.4f}".format(X))
            if (not N==Q) and (not N in R):
                R.append(N)
                F_5Nbr.write(N)
                F_5Nbr.write("_")
                F_5Nbr.write(str(X))
                F_5Nbr.write(" ")
                c+=1
        else:
            break
    F_5Nbr.write("\n")
F_5Nbr.close()




