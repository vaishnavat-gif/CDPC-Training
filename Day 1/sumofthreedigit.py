#sum of 3 digit
no=int(input("enter value: "))
n1=no%10  #5
no=no//10  #34
n2=no%10   #4
n3=no//10   #3
res=n1+n2+n3
print(res)