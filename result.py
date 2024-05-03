_a="programmer"
va=0
_va=0
_av=0
a=0
b=0
c=0
for i in _a:
 x= input("enter the name of a student")
 y= int(input('enter the marks of the student'))
 z= int(input("enter the roll no of the student"))
 if y>=80 and z<=10:
    print("the student is in group A")
    a+=1
    va=(va+y)
 elif(y>=60 and y<80) and (z>10 and z<=20):
   print("the student is in group B")
   b+=1
   _va=(_va+y)
 else:
    if (y>=40 and y<60) and (z>20 and z<=30):
     print("the student is in group C")
     c+=1
     _av=(_av+y)
    else:
      print("the marks and rollno you entered doesnot follow the right criteria")
 
print(f'the total number of student in group A is={a}')    
print(f"the average marks of the student in group A is={va/(a)}")
print(f"the total number of students in group B is={b}")
print(f"the average marks of the students in group B is={_va/(b)}")
print(f'the total number of students in group C is={c}')
print(f"the average marks of students in group C is={_av/(c)}")
print(f' the number of students that neither fall into any of these group is={10-(a+b+c)}')
   
 
    