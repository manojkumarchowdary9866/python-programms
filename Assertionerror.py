from math import factorial
def fact(n):
    if n==0 or n==1:
        return 0
    return n*fact(n-1)


assert fact(5)==factorial(5),"answerdoesn't match"
        
