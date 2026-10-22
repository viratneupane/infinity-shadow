#This program is based on the logic to create a login and signup with the
#use of os module as well as the file handling methods.

import os
try:
    _as="E:/"
    name='Login1'
    d=os.path.join(_as,name)
    os.mkdir(d)
except FileExistsError:
  cr=0
try:
    _ab="E:/"
    name1='Login2'
    e=os.path.join(_ab,name1)
    os.mkdir(e)
except FileExistsError:
  cr=0
print('Welcome to the Login and Sign up page\n')
try:
 v=int(input("Would you like to 1.Login OR 2. Signup(Creating a New account)::"))
except ValueError:
  print('\nPlease select the option (1) or (2)')
for_=0
cc=0
if v==2:
 _a=input('Enter your username:')
 _b=input('Enter your password:')
 with open(f"E:/Login1/{_a}.txt","w") as sa:
  sa.write(f'{_a}//')
  sa.write(f'{_b}\n')
 print('\n You have successfully created your account')

elif v==1:
 j=True
 while j:
  _c= input('\n Please enter your username:')
  _d= input('\n Please enter your password:')
  with open(f'E:/Login2/{_c}.txt',"a") as sa1:
    sa1.write(f'{_c}//')
    sa1.write(f'{_d}\n')
  with open(f'E:/Login2/{_c}.txt',"r") as sa1:
       b=sa1.readline()
  with open(f'E:/Login1/{_c}.txt','r') as sa2:
         a=sa2.read()
  if b==a:
            print('You have succesfully logged in!\n')    
            from datetime import date
            c=date.today()
            if for_<=1:
             with open(f'E:/Login2/{_c}.txt',"a") as sa1:
              sa1.write(f'{c}')
              for_=+1
            with open(f'E:/Login2/{_c}.txt',"r") as sa1:
             while cc<=len(sa1.readline())-2:
               u=sa1.readline()
               c=+1
             if u==c:
                cr=0
             else:
                for_=+1
            j=False
            print(f'\n You have logged in for{for_} times')           
  else: 
         print('\nplease enter the correct username and password')
         j=True
else:
   print('\nPlease select the option (1) or (2)')



# Use of w+,r+, and a+
# 1. use of w+ is it is used to give permission for both read and write of the file.
# 2. use of r+  is it is used to give permision for both read and write same as w+.
# 3. Use of a+ is it is used to give permission for both append and read.

