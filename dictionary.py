_i=0
L=[['ormang','oormngo','angmo','apank'],
   [ 'oorgnaeo','orrange','rampak','graneo'],
   ['ananabss','lalana','aanbba','ananba']
   ]
L2=['mango','orange','banana']
v=[]
q=[] 
for i in L:
   for x in L2:
    for j in i:  
      if len(j)==len(x): 
        for _b in j:
         v.append(_b)
        for _c in x:
         q.append(_c) 
        v.sort()
        q.sort() 
        if v==q:
         print(f'the index of the element similar to {x} is {i.index(j)} in the  sub-list{L.index(i) }')
        v.clear()
        q.clear()

    
        