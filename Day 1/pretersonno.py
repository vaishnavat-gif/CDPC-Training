#a no is said to be preterson if sum of factorial of each digit is equal to no itself.
num = int(input("Enter a number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    
    # factorial calculation
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i
    
    sum = sum + fact
    num = num // 10

if sum == temp:
    print("It is a Peterson number")
else:
    print("It is not a Peterson number")