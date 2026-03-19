#accept 4 numbers and five max no
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# min = a

# if b < min:
#     min = b
# if c < min:
#     min = c
# if d < min:
#     min = d

# print("Minimum number is:", min)

#find min and max element in list

# arr=[5,3,2,7]
# max = arr[0]
# for i in range(1,len(arr)):
#     if max<arr[i]:
#         max=arr[i]

# print(max)

# arr=[5,3,2,7]
# min = arr[0]
# for i in range(1,len(arr)):
#     if min>arr[i]:
#         min=arr[i]

# print(min)

#check leap year

# year=int(input("enter year: "))
# if year%100!=0:
#     if year%4==0:
#         print("non century leap year")
#     else:
#         print("not leap year")
# else:
#     if year%400==0:
#         print("century leap year")
#     else:
#         print("not leap year")

#techb no
no = 2025
n1 = no%100
n2 = no//10
sum = n1 + n2
sq = sum**2
if sq==no:
    print ("tech no")
else:
    print("not tech no")

#rearrange pos and neg no