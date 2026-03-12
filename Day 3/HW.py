# **Tasks**

# 1. Write a program to check whether a number is even or odd
# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     print("Number is Even")
# else:
#     print("Number is Odd")

# 2. Write a program to find the largest of three numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# n = max(a, b, c)
# print(n)

# 3. Check whether a number is positive, negative, or zero.
# n = int(input("Enter a number: "))
# if n > 0:
#     print("Number is positive")
# elif n < 0:
#     print("Number is negative")
# else:
#     print("Number is zero")

# 4. Write a program to check whether a number is divisible by both 3 and 5.
# n = int(input("Enter a number: "))
# if n % 3 == 0 and n % 5 == 0:
#     print("No. is divisible by both 3 and 5")
# else:
#     print("No. is not divisible by both 3 and 5")

# 5. Write a program to print numbers from 1 to N.
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     print(i)

# 6. Write a program to print all even numbers from 1 to N.
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     if i % 2 == 0:
#         print(i)

# 7. Write a program to calculate the sum of first N natural numbers.
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
# print("Sum =", sum)

# 8. Write a program to calculate the factorial of a number.
# n = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial = factorial * i
# print(factorial)

# 9. Write a program to print the multiplication table of a number.
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)

# 10. Write a program to count the number of digits in a number.
# n = int(input("Enter a number: "))
# count = 0
# while n > 0:
#     n = n // 10
#     count = count + 1
# print(count)

# 11. Write a program to reverse a number.
# n = int(input("Enter a number: "))
# rev = 0
# while n > 0:
#     rem = n % 10
#     rev = rev * 10 + rem
#     n = n // 10
# print(rev)

# 12. Write a program to check whether a number is palindrome
# n = int(input("Enter a number: "))
# n1 = n
# rev = 0
# while n > 0:
#     rem = n % 10
#     rev = rev * 10 + rem
#     n = n // 10
# if n1 == rev:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")

# 13. Write a program to find the sum of digits of a number.
# n = int(input("Enter a number: "))
# sum = 0
# while n > 0:
#     rem = n % 10
#     sum = sum + rem
#     n = n // 10
# print(sum)

# 14. Write a program to check whether a number is an Armstrong number.
# n = int(input("Enter a number: "))
# n1 = n
# sum = 0
# while n > 0:
#     rem = n % 10
#     sum = sum + rem**3
#     n = n // 10
# if n1 == sum:
#     print("Number is Armstrong")
# else:
#     print("Number is not Armstrong")

# 15. Write a program to print numbers divisible by 7 between 1 and N.
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     if i % 7 == 0:
#         print(i)
