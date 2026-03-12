#sum of five digit 
#let numbers are 12345 == 1+2+3+4+5 = 15
no=int(input("enter value: ")) 
n1=no%10   #5
no=no//10  #34
n2=no%10   #4
no=no//10  #3
n3=no%10
no=no//10
n4=no%10
n5=no//10
res=n1+n2+n3+n4+n5
print(res)