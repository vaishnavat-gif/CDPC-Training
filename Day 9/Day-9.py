# Example 1: Leetcode
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
class Solution:
    def isPalindrome(self, x: int) -> bool:
         s = str(x)
         return s == s[::-1]

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

# Example 1:
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for customer in accounts:
            wealth = sum(customer)
            max_wealth = max(max_wealth, wealth)
        
        return max_wealth

##################
arr=[11,22,33]
for x in range (len(arr)):
    print(arr[x],end=" ")

ans=[]
arr=[[11,22,33],[6,8,3],[5,6,7]]
for x in range (Len(arr)):
    sum=0
    for i in range(Len(arr[x])):
        sum=sum+arr[x][i]
    ans.append(sum)
return max(ans)
#####################

# Complete the 'staircase' function below.
# The function accepts INTEGER n as parameter.
def staircase(n):
    # Write your code here
    for i in range (1,n+1):
        print((n-i)*' '+i*'#')

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

# Complete the 'miniMaxSum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def miniMaxSum(arr):
    total = sum(arr)
    min_val = min(arr)
    max_val = max(arr)
    
    min_sum = total - max_val
    max_sum = total - min_val
    
    print(min_sum, max_sum)

    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

# You are in charge of the cake for a child's birthday. 
# It will have one candle for each year of their total age. They will only be able to blow out the tallest
# of the candles. Your task is to count how many candles are the tallest. Example[4,4,1,3]
# The tallest candles are 4 units high. There are 2 candles with this height, so the function should return 2
ef birthdayCakeCandles(candles):
    # Write your code here
    tallest = max(candles)          # Find tallest candle
    count = candles.count(tallest)  # Count how many times it appears
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def timeConversion(s):
    # Write your code here
    period = s[-2:]          # AM or PM
    time_part = s[:-2]       # HH:MM:SS
    hour = int(time_part[:2])
    
    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    
    return f"{hour:02d}{time_part[2:]}"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)



   