print "Calculating Similarity Factor between each trigram pair..."
name="marathi_100sentences"
fc=0
sim=0.0
Sim_File=open("../Intermediate_Data/%s_Simlr.txt"%name,"w")
Tris=open("../Intermediate_Data/%s_Tris.txt"%name).readlines()
Sum=[]
Trig=[]
flag=0
for line in Tris:
        line=line.rstrip()
        if len(line)==0:
                fc+=1
                #print "S",fc
                if len(Sum)>0:
                        for S in Sum:
                                Sim_File.write(str(S)+"\t")
                else:
                        for S in Trig:
                                Sim_File.write(str(S)+"\t")
                Sim_File.write("\n")
                Trig=[]
                Sum=[]
        else:
                if len(Trig)>0:
                        if len(Sum)==0:
                                for i in Trig:
                                        Sum.append(i)
                        else:
                                for i in range(0,len(Sum)):
                                        Sum[i]=Sum[i]+Trig[i]
                        Trig=[]
                tri_f=line.split()
                q=0
                for each in Tris:
                        each=each.rstrip()
                        if not len(each)==0:
                                tri2_f=each.split()
                                for feature in tri_f:
                                        feature=feature.split('_')
                                        F1=feature[1].split('#')
                                        for ftr in tri2_f:
                                                ftr=ftr.split('_')
                                                f1=ftr[1].split('#')
                                                if feature[0]==ftr[0] and len(F1)==len(f1):
                                                        if len(F1)==3:
                                                                if (F1[0]==f1[0] or F1[1]==f1[1]) or (F1[2]==f1[2]):
                                                                        sim=sim+(float(feature[2])+float(ftr[2]))
                                                        elif len(F1)==2:
                                                                if (F1[0]==f1[0]) and (F1[1]==f1[1]):
                                                                        sim=sim+(float(feature[2])+float(ftr[2]))
                        else:
                                q+=1
                                Trig.append(sim)
                                sim=0.0
        
Sim_File.close()

print "Similarity Matrix calculated Successully... "
