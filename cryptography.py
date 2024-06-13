#This cryptographic programs contexts plain text into cipher text 
#in such a way that the given alphabet will be changed in refrence to the alphabet 6 steps ahead of it 
# and gets * or $ sign based on the odd or even index of the alphabets and numbers will be 
# similarly  converted into * or $ based on the odd or even number.

def encrypted():
    from newpy import recog
    print(' This is the cryptography machine!')
    _a=input('\nenter the information that should be encrypted:')
    _b= _a.lower()
    _c="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    z=[]
    for i in _b:
        if i in _c and _c.index(i)%2==0:
         y=_c.index(i)
         x= '*'+ _c[y+6]  
         z.append(x)
        elif i in _c and _c.index(i)%2!=0:
          y=_c.index(i)
          x='$'+ _c[y+6]
          z.append(x)
        else:
         z.append(i)
    t=''.join(z)
    print(f' The encrypted version of the given plain text is: {t} ')
encrypted()
print('\n Now we can decrypt that encrypted code!')

def decrypted():
 inp=input('To perform the decryption of the code, Please enter the private key::')
 _inp=inp.lower()
 if _inp=='@passkey$':
  _z=[]
  q=input('enter the code that needs to be decrypted: ')
  __c='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
  for j in q:
        if j=='*' or j=='$':
          _u=0
        elif j in __c: 
          _y= __c.index(j)
          _x= __c[_y-6]
          _z.append(_x)
        else:
          _z.append(j)
        _t=''.join(_z)
  print(f'The decrypted version of the encrypted text is: {_t}')
 else:
   cr=0
decrypted()
