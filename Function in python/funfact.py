def ft (n):
    f=1
    for i in range (n,-1):
        f=f*i
    return f
a=int(input("enter a number"))
z=ft(a)
print(z)