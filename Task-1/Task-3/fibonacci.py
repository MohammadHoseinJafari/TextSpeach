# Task 1-3
# Time complexity : O(n)

def fibo(n):
    series = [0, 1]
    for i in range(2, n):
        series.append(series[i-1] + series[i-2])
    return series

n = int(input("Enter a Number : "))
print( n==0 if 0 else fibo(n))