n=5
fact=1
for i in range(1,n+1):
    fact*=i
if n<0:
    print("print positive values")
else:
    print(f'factorial of {n} is :{fact}')
