from __future__ import division
import math as m

def f1(x):
    alfa=0
    return 2*m.sin(x)+m.sin(2*x)+2*m.sin(3*x)+alfa

def f2(x):
    return 2*m.sin(x)+m.sin(2*x)+2*m.cos(x)+m.cos(2*x)

def f3(x):
    return 2*m.sin(1.1*x)+m.sin(2.1*x)+2*m.sin(3.1*x)

def f1_al(x):
    alfa=0.1
    return 2*m.sin(x)+m.sin(2*x)+2*m.sin(3*x)+alfa



def fa(j,x,func):
    L=50
    a=0
    for i in range(2*L-1):     
        a+=1/L*(func(x[i])*m.cos(j*x[i]))
        #print(a,'   ',func(x[i]))
    return a

def fb(j,x,func):
    L=50
    b=0
    for i in range(2*L-1):
        b+=1/L*(func(x[i])*m.sin(j*x[i]))
    return b

def F(x,xst,Mc,Ms,func):
    sumA=0
    sumB=0
    for j in range(1,Mc):
        sumA+=fa(j,x,func)*m.cos(j*xst)
    for k in range(1,Ms):
        sumB+=fb(k,x,func)*m.sin(k*xst)

    #wynik=[fa(0,x[i],func)/2+sumA+sumB for i in x]
    return fa(0,x,func)/2+sumA+sumB
    #return wynik


#zad 1
plik = open("zad1.dat", 'w')
plik2 = open("zad2.dat", 'w')
plik3 = open("zad3.dat", 'w')
plik4 = open("zad4.dat", 'w')


step=2*m.pi/100
x=[]
xst=0
Ms=5
Mc=5
result=[]
result2=[]

result3=[]
result4=[]
result5=[]

result6=[]
result7=[]


#wspolczynniki:
i=0
while i<2*m.pi:
    x.append(i)
    i=i+step
xst=0
j=0
while xst<2*m.pi:
    result.append(F(x,xst,Mc,Ms,f1))
    result2.append(F(x,xst,Mc,Ms,f2))
    result3.append(F(x,xst,0,5,f3))
    result4.append(F(x,xst,Mc,Ms,f3))
    result5.append(F(x,xst,10,10,f3))
    result6.append(F(x,xst,5,5,f1_al))
    result7.append(F(x,xst,30,30,f1_al))

    plik.write(str(xst)+' '+str(result[j])+' '+str(f1(xst))+"\n")
    plik2.write(str(xst)+' '+str(result2[j])+' '+str(f2(xst))+"\n")
    plik3.write(str(xst)+' '+str(result3[j])+' '+str(result4[j])+' '+str(result5[j])+' '+str(f3(xst))+"\n")
    plik4.write(str(xst)+' '+str(f1_al(xst))+' '+str(result6[j])+' '+str(result7[j])+"\n")



        

    xst=xst+step
    j=j+1
    
plik.close()
#print(len(x))
