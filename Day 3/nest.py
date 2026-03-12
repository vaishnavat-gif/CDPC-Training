#nested loop to print 1 22 333 4444
for i in range(1,5):             
    for j in range(1,i+1):   #so that loop will be run only till i
        print(i,end="")
    print()