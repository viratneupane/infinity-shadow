# #TO create the tally bar by inserting the frequency
def tallyBar():
 import math
 # We store the tally symbol value in the variable.
 _tally_symbol= "|"
 _crosssymbol="/"
 _var= int(input('Enter the frequency for tally bar conversion: '))
 _z=","
 j=1
 i=0
 count=0
 while j<=_var:
  if _var<=4:
   print(_tally_symbol*_var)
   break
  else:
   i+=1
   j+=1
   if i%5==4:
    stored_tally= 0  
    stored_tally= (_tally_symbol*4)+ _crosssymbol + _z
   count+=1
   continue
 if _var>4:
   trick= _var/5   # we have introduced ceiling function because as stored tally is seperated by comma
   _trick = math.ceil(trick) # as we pass on 5 interval we have to increase the slicing range by 1 as we change the frequency by 5
   extract= stored_tally*count
   realextract=slice(0,(_var+ (_trick-1))) # As the loop runs for the time the variable is assigned we slice the part we need.
   result= extract[realextract]
   final_tally = result.split(",")
   print(' '.join(final_tally)) # Here we are using the join function so that 
tallyBar() # we can extract the value from the list in the general form 


