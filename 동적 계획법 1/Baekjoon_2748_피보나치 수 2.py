import sys

N = int(sys.stdin.readline())

def Fibonacci(n):
    if(n == 0):
        return 0
    if (n == 1):
        return 1
    else:
        return Fibonacci(n-2) + Fibonacci(n-1)

print(Fibonacci(N))