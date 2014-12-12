import collections

## Calculating Ri values for connected(Marathi<=>Hindi) words...
name="marathi_100sentences"
f_cnt="../Input/Aligned_count.txt"
f_ri="../Intermediate_Data/%s_QIs.txt"%name
Centers="../Intermediate_Data/%s_Centers.txt"%name
Nbrs="../Intermediate_Data/%s_5Nbr.txt"%name

print "Finding Tag Distribution Score(Ri)s for connected(Marathi<=>Hindi) words..."
R=collections.OrderedDict()
f=open(f_ri,"w")
word=""
total=0
for each in open(f_cnt,"r"):
    each=each.split()
    if len(each)==2:
        word=each[0]
        total=int(each[1])
        R[each[0]]=[]
    else:
        r=(float(each[2])/total)
        f.write(each[0]+" "+each[1]+" "+str(r))
        R[each[0]].append(each[1]+"_"+str(r))
        f.write("\n")
f.close()
        
print "Finding Tag Distribution Score(Qi)s for All words..."
v=0.000002  #hyperparameter
TAG=open("../Input/Tags.txt","r").readlines()
TAG=[t.rstrip() for t in TAG]
Tags=len(TAG)     #Total Tags

## calculation of Ki(denominator)...
K=collections.OrderedDict()
Nbr={}
for Nj in open(Nbrs,"r"):
    key=Nj.split("#")[0]
    Nj=Nj.split("#")[1]
    Nbr[key]=Nj         ## Storing nbr_info for later use..
    Nj=Nj.split()
    val=0
    for i in Nj:
        val+=float(i.split("_")[1])
    K[key]=v+val


## Final calculation of Qi..
U=float(1)/Tags
Q=collections.OrderedDict()
for w in open(Centers,"r"):
    w=w.rstrip()
    if not w in Q:
        Q[w]=[]
    if w in R:
        for tag in TAG:
            done=[x for x in R[w] if (x.split("_")[0])==tag]
            if len(done):
                Q[w].append(done[0])
            else:
                Q[w].append(tag+"_0.0")
    else:
        for tag in TAG:
            for Iter in range(0,10):
                prv=[tg for tg in Q[w] if tg.split("_")[0]==tag]
                if len(prv):
                    for pr in prv:
                        Q[w].remove(pr)
                prv_WQj=0.0
                Wght=0.0
                Qj=0.0
                if w in Nbr:
                    if not len(Nbr[w].split())==0:
                        for each in Nbr[w].split():
                            each=each.split("_")
                            if each[0] in Q:
                                Qj=[float(e.split("_")[1]) for e in Q[each[0]] if e.split("_")[0]==tag][0]
                            prv_WQj+=(float(each[1])*Qj)
                        Numrt=(prv_WQj)+(v*U)
                        Qw=float(Numrt)/K[w]
                        Q[w].append(tag+"_"+str(Qw))
f=open(f_ri,"w")
for q,v in Q.items():
    f.write(q+" ")
    f.write(" ".join(v))
##    f.write(str(v))
    f.write("\n")
f.close()
