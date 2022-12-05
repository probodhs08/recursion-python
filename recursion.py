'''def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter yournumber:"))
print("factorial", factorial(n))
'''
n=int(input("enter the value:"))
ans=1
while n>1:
    ans*=n
    n=n-1
print("factorial",ans)
