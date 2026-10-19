'''def hello():
    print("this is a hello function so I am doing hello")

hello()

def sum(a,b):
    c = a+b
    print("the sum of a and b is ",c)

sum(10,20)

def hello(name,age):
    print(f"your name is {name} and your age is {age}")

hello(age = 20 ,name = "nandini")



def palindrome(st):
    reversed = ""

    for i in range(len(st)-1, -1, -1):
        reversed = reversed + st[i]

    if reversed == st:
        print(f"{st} is a palindrome")
    else:
        print(f"{st} is not a palindrome")


palindrome("NAMAN")
palindrome("CURSOR")

def pallindrome(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
         rev = rev + st[i]
    
    if rev == st:
        print(f"{st} is a pallindrome")
    else:
         print(f"{st} is not a not a pallindrome")

PALINDROME = input("enter a string to check whether it is a pallindrome or not : ")
pallindrome(P9ALINDROME)'''


def factorial(n):
    if  n == 1:
        return 1
    return n * factorial(n-1)
    

result = factorial(6)
print(f"The factorial of 6 is: {result}")
