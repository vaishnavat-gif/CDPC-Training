# check no is palindrome
no = int(input("Enter number: "))
rev=0
temp=no 

while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10

if temp==rev:
    print("Palindrome")

else:
    print("Not palindrome")