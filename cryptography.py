#This cryptographic programs contexts plain text into cipher text 
#in such a way that the given alphabet will be changed in refrence to the alphabet 6 steps ahead of it 
# and gets * or $ sign based on the odd or even index of the alphabets and numbers will be 
# similarly  converted into * or $ based on the odd or even number.
def cr():
    from newpy import recog
    print(' This is the cryptography machine!')
    _a=input('\nenter the information that should be encrypted:')
    _b= _a.lower()
    _c="abcdefghijklmnopqrstuvwxyz"
    z=[]
    _z=[]
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
    print('\n Now we can decrypt that encrypted code')
    for j in t:
      if j=='*' or j=='$':
        _u=0
      elif j in _c: 
        _y= _c.index(j)
        _x= _c[_y-6]
        _z.append(_x)
      else:
        _z.append(j)
      _t=''.join(_z)
    print(f'The decrypted version of the encrypted text is {_t}')
cr()
