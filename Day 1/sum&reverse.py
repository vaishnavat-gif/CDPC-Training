#sum of 9 digit number and reverse it
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
res=n1+n2+n3+n4+n5+n6+n7+n8+n9
res1=n1*100000000+n2*10000000+n3*1000000+n4*100000+n5*10000+n6*1000+n7*100+n8*10+n9
print(res)
print(res1)
sum1=res%10
res=res//10
sum2=res%10
res=res//10
sum3=res%10
rev_sum=sum1*100 + sum2*10 + sum3
print(rev_sum)

