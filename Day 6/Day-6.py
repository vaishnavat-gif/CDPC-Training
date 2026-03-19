#Hackerrank 
def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0
    
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    
    return [alice, bob]

#def aVeryBigSum(ar):
    # Write your code here
    total = 0
    for num in ar:
        total += num
    return total

#if we have sample ip this should be code 
# n=int(input())
# ----------------------------
# a=int(input())
# b=int(input())
# ------------------------------
# a,b=map(int,input().split())
# -------------------------------
# a,b,c=map(int,input().split())
# ------------------------------
# arr = list(map(int,input().split()))
# -------------------------------
# arr=list(map(int,input().split()))
# ------------------------------
# arr=eval(input())
# ------------------------------

# Complete the 'diagonalDifference' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    sum1 = 0
    sum2 = 0
    
    for i in range(n):
        sum1 += arr[i][i]
        sum2 += arr[i][n-i-1]
    
    return abs(sum1 - sum2)

# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.
def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    n = len(arr)

    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1

    print(pos/n)
    print(neg/n)
    print(zero/n)

    