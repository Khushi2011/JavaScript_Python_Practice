# def factorial_iterative(n):
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#     return fac
# print(factorial_iterative(4))
# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
# print(factorial_recursive(5))

def fibbonaci (n):
    if n==1 or n==0:
        return n
    else:
        return fibbonaci(n-1)+fibbonaci(n-2)
n=int(input("Enter total terms:"))
for i in range(n):
    print(fibbonaci(i),end=" ")