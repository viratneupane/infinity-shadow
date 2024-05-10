#This unique python program finds the index of two numbers in a list that ultimately create 
# a given target number by adding each other. 
_a=0
_b=0
_c=0
_d=0
_e=0
_f=0
_ee=0
_zzz=int(input('enter how many numbers you want to keep in a list:'))
if _zzz==1:
 z=input('enter the first integer in the list:')
elif _zzz==2:
 z=input('enter the first integer in the list:'),input('second:')
elif _zzz==3:
 z=input('enter the first integer in the list:'),input('second:'),input('third:')
else:
 z= input('enter the first integer in the list:'),input('second:'),input('third:'),input('fourth:') 
g=list(z)
print(f'the list you created is{g}')
h= int(input('Enter the target number which should be created:'))
for v  in g:
    if g.index(v)==0 and g.count(v)<=1:
      _a=int(v)
    elif g.index(v)==1 and g.count(v)<=1:
       _b=int(v)
    elif g.index(v)==2 and g.count(v)<=1:
       _c=int(v)
    elif g.index(v)==3 and g.count(v)<=1:
       _d=int(v)
    elif g.index(v)==0 and g.count(v)>1:
        _e=int(v)
    elif g.index(v)!=0 and g.count(v)>1:
       _ee= int(v)
if (_a+_b)==h and _a!=0 and _b!=0:
  d=[g.index(f'{_a}'),g.index(f'{_b}')]
  print(f'the required index of the numbers adding to the target is:{d}')
elif (_a+_c)==h and _a!=0 and _c!=0:
  e=[g.index(f'{_a}'),g.index(f'{_c}')]
  print(f'the required index of the numbers adding to the target is:{e}')
elif (_a+_d)==h and _a!=0 and _d!=0:
  f=[g.index(f'{_a}'),g.index(f'{_d}')]
  print(f'the required index of the numbers adding to the target is:{f}')
elif (_b+_c)==h and _b!=0 and _c!=0:
   i=[g.index(f'{_b}'),g.index(f'{_c}')]
   print(f'the required index of the numbers adding to the target is:{i}')
elif (_b+_d)==h and _b!=0 and _d!=0:
   j=[g.index(f'{_b}'),g.index(f'{_d}')]
   print(f'the required index of the numbers adding to the target is:{j}')
elif (_c+_d)==h and _c!=0 and _d!=0:
   k=[g.index(f'{_c}'),g.index(f'{_d}')]
   print(f'the required index of the numbers adding to the target is:{k}')
elif 2*(_e)==h and _e!=0:
   _zz= "-".join
   l=[g.index(f'{_e}'),g.index(f'{_ee}')]
   print(f'the required index of the number adding to the target is:{l}')
else:
   print('Cannot Compute the Calculation')
