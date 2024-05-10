v=0
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
m=0 
_num= input('enter the number in Uppercase Roman Numerals :')
for x in _num:
   if x=="I":
    v=1
    g+=1
   elif x=="V":
    a=5
    h+=1
   elif x=="X":
    b=10
    i+=1
   elif x=="L":
    c=50
    j+=1
   elif x=="C":
    d=100
    k+=1
   elif x=="D":
    e=500
    l+=1
   elif x=="M":
    f=1000
    m+=1
   else:
    print('Invalid data: Please enter all Roman numerals in Uppercase letters')
_a=_num.find("I") 
_b=_num.rfind("V")
_c=_num.rfind('X')
_cc=_num.find("X")
_ce=_num.find("C")
_d=_num.rfind('L')
_e=_num.rfind('C')
_f=_num.rfind('D')
_g=_num.rfind('M')
if (_a<_b or _a<_c) and _a!=-1:
  tot= (v*g+a*h+b*i+c*j+d*k+e*l+f*m)- 2*v
elif (_cc<_d or _cc<_e) and _cc!=-1:
  tot =(v*g+a*h+b*i+c*j+d*k+e*l+f*m)- 2*b
elif (_ce<_f or _ce<_g) and _ce!=-1:
  tot=(v*g+a*h+b*i+c*j+d*k+e*l+f*m) - 2*d
else:
  tot=v*g+a*h+b*i+c*j+d*k+e*l+f*m
print(f"the numeric form of the given roman number is= {tot}")
