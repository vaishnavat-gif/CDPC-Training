# hw - #accept 9 digit no and sum of 1 and last digit
no=int(input("enter value: ")) 
n1=no%10   #5
no=no//10  #34
n2=no%10   #4
no=no//10  #3
n3=no%10
no=no//10
n4=no%10
no=no//10
n5=no%10
no=no//10
n6=no%10
no=no//10
n7=no%10
no=no//10
n8=no%10
no=no//10
n9=no%10
res=n1+n9
print(res)