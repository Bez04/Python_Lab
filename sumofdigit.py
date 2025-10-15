# Sum of digits of number


def sumofdigit(a):
    sum=0
    while(a>0):
        num=a%10
        sum=sum+num
        a=a//10
    print("sum of digit a number:",sum)      
a=int(input("Enter a number:"))
sumofdigit(a)       