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

if v==2:
 _a=input('Enter your username:')
 _b=input('Enter your password:')
 with open(r"E:\Login1\signup.txt","a") as sa:
  sa.write(f'{_a}//')
  sa.write(f'{_b}\n')
 print('\n Now you can login to your account')

j=True
k=False
while j:
  _c= input('\n Please enter your username again:')
  _d= input('\n Please enter your password again:')
  with open(r'E:\Login2\signup1.txt','w') as sa1:
    sa1.write(f'{_c}//')
    sa1.write(f'{_d}\n')
  with open(r'E:\Login1\signup.txt','r') as sa:
   if j:
    for a in sa.readlines():
       with open(r'E:\Login2\signup1.txt','r') as sa1:
        b=sa1.read()
       if a==b:
        print('You have succesfully logged in!\n')
        j=False
        k=True
   if not k:
      print('\nplease enter the correct username and password')
      j=True
   
