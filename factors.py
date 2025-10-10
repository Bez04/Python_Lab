# Find The Factor of Number

import math
num = int(input("Enter a number: "))
print("Factorial of", num, "is:", math.factorial(num))
               

num=int(input("Enter a number:"))
fact=1
for i in range(1,num + 1):
    fact=fact*i
print("Factorial of",num,"is",fact)
    

