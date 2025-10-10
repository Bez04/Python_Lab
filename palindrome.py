# Find the Palindrome

a=input("Enter the string or number:")
reverse=a[::-1]
if(a==reverse):
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")
