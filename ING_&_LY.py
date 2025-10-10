#write a program to add 'ing' at end of the given string (length should be atleast 3), 
#if given string already n split 'ing' then add 'ly' instead

str1=input("Enter the strings:")
length=len(str1)
if length>=3:
  if str1[-3:]=='ing':
    str1+='ly'
  else:
    str1+='ing'  
else:
  str1=str1    
print("Add new string:",str1)  