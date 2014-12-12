from math import log
from collections import Counter
import collections,re

## Global Variables...
global C1,C2,C3,C5
global Fi_Dict,T_Dict
Fi_Dict=collections.OrderedDict()
T_Dict=collections.OrderedDict()
B={}
U={}
C1=0
C2=0
C3=0
C5=0

name="marathi_100sentences"
filen="../Input/%s.txt"%name
filename="../Intermediate_Data/%sP.txt"%name
f_toknz="../Intermediate_Data/%s_tokenized.txt"%name

reg_sym=r'(\")|(\()|(\))|(\,)|(\')|(\`)'
reg_wsym=r'^((\-)|.|(\s+)(\'+))$'

## Padding start & end words...
print "Pre-processing Data..."
pd=open(filename,"w")
for line in open(filen):
        s1="!"
        s2="!"
        e2="$"
        e1="$"
        pd.write(s1+" "+s2+" "+line.rstrip()+" "+e2+" "+e1+"\n")
pd.close()

## Functions to calculate tokens & Ngram counts................................................
def bigram(line,bi):
        for i in range(len(line)-1):
                bi.append((line[i],line[i+1]))

def trigram(line,tri):
        for i in range(len(line)-2):
                if line[i+1]==line[i+2] and line[i+1]=="$":
                        pass
                elif line[i]==line[i+1] and line[i+1]=="!":
                        pass
                else:
                        tri.append((line[i],line[i+1],line[i+2]))

def figram(line,fi):
        for i in range(len(line)-4):
                fi.append((line[i],line[i+1],line[i+2],line[i+3],line[i+4]))

def tokenizeNgram(filename):
        ft=open(f_toknz,"w")
        global C1,C2,C3,C5
        l=0
        uni=[]
        bi=[]
        tri=[]
        fi=[]
        for line in open(filename,"r"):                 #Getting each line from input file
                token_list=[ ]
                words=line.split()      ##Getting all words from the line
                for word in words:                      ##Getting each word/unit from words of line
                        if re.search(reg_sym, word):
                                word=re.sub(reg_sym,'',word)
                        if not word=="":
                                if not re.search(reg_wsym,word):
                                        token_list.append(word)
                                        ft.write(word+" ")
                                        uni.append(word)
                                elif word=="!" or word=="$":
                                        token_list.append(word)
                                        uni.append(word)
                bigram(token_list,bi)
                trigram(token_list,tri)
                figram(token_list,fi)
                ft.write("\n")
        ft.close()
        print "Calculating Ngrams..."
        f=open("../Intermediate_Data/%s_uni_grams.txt"%name,"w")
        for k,v in Counter(uni).most_common():
                C1+=1
                U[k]=v
                f.write(k+" "+str(v))
                f.write("\n")
        f.close()
        f=open("../Intermediate_Data/%s_bi_grams.txt"%name,"w")
        for k,v in Counter(bi).most_common():
                C2+=1
                br=k[0]+","+k[1]
                B[br]=v
                f.write(k[0]+" "+k[1]+" "+str(v))
                f.write("\n")
        f.close()
        f=open("../Intermediate_Data/%s_tri_grams.txt"%name,"w")
        for k,v in Counter(tri).most_common():
                C3+=1
                trig=k[0]+","+k[1]+","+k[2]
                T_Dict[k]=v
                f.write(k[0]+" "+k[1]+" "+k[2]+" "+str(v))
                f.write("\n")
        f.close()
        f=open("../Intermediate_Data/%s_five_grams.txt"%name,"w")
        for key,v in Counter(fi).most_common():
                C5+=1
                trig=key[1]+","+key[2]+","+key[3]
                cntx=key[0]+"#"+key[4]+"#"+str(v)
                if not trig in Fi_Dict:
                        Fi_Dict[trig]=[]
                Fi_Dict[trig].append(cntx)
                f.write(key[0]+" "+key[1]+" "+key[2]+" "+key[3]+" "+key[4]+" "+str(v))
                f.write("\n")
        f.close()
##=================================================================================================================================

print "Tokenizing..."
tokenizeNgram(filename)
print C1,"C1",C2,"C2",C3,"C3",C5,"C5"

Tr=0
fl=1
print "length of Fi_Dict: ",len(Fi_Dict)
print "length of T_Dict: ",len(T_Dict)

print "Calculating PMI values for all features of each trigram type.."
f=open("../Intermediate_Data/%s_Tris.txt"%name,"w")
for trigram in T_Dict.keys():
        Tr+=1
       # print "F",Tr
        trig=trigram[0]+","+trigram[1]+","+trigram[2]
        F_set=""
        if trig in Fi_Dict:
                for F in Fi_Dict[trig]:
                        F=F.split("#")
                        w=[F[0],trigram[0],trigram[1],trigram[2],F[1]]
                        PMI=0.0
                        L=w[0]+","+w[1]
                        R=w[3]+","+w[4]
                        
                        TC=w[1]+","+w[3]
                        LCRW=w[0]+","+w[1]+","+w[3]
                        LWRC=w[1]+","+w[3]+","+w[4]

                        P=float(F[2])/C5
                        P1=float(U[w[0]])/C1
                        P2=float(U[w[1]])/C1
                        P3=float(U[w[2]])/C1
                        P4=float(U[w[3]])/C1
                        P5=float(U[w[4]])/C1                      
                        PMI=P/(P1*P2*P3*P4*P5)
                        if not PMI==0.0:
                                PMI=(log(PMI,10))
                        F_set='C'+"_"+w[0]+"#"+w[4]+"_"+str(PMI)+" "

                        P=float(T_Dict[trigram])/C3
                        PMI=P/(P2*P3*P4)
                        if not PMI==0.0:
                                PMI=(log(PMI,10))
                        F_set+='T'+"_"+w[1]+"#"+w[2]+"#"+w[3]+"_"+str(PMI)+" "

                        P=float(B[L])/C2
                        PMI=P/(P1*P2)
                        if not PMI==0.0:
                                PMI=(log(PMI,10))
                        F_set+='L'+"_"+w[0]+"#"+w[1]+"_"+str(PMI)+" "

                        P=float(B[R])/C2
                        PMI=P/(P4*P5)
                        if not PMI==0.0:
                                PMI=(log(PMI,10))
                        F_set+='R'+"_"+w[3]+"#"+w[4]+"_"+str(PMI)+"\n"
                        f.write(F_set)
                f.write("\n")

f.close()
