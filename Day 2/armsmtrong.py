#check no is arsmstrong ex:153 = 1 5 3 = 1^3+5^3+3^3 = 1+125+27 =153
no = int(input("Enter number: "))
rev=0
temp=no 
#count no 
count = 0
while no > 0:
    no = no // 10
    count = count + 1

while no>0:
    rem=no%10
    sum=sum+rem**count
    no=no//10

if temp==sum:
    print("arsmstrong")
else:
    print("not arsmstrong")