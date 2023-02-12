def codex(a,b):
    """this is a programe of average"""
    av=(a+b)/2
    return av
    print(av)
n=int(input("enter n1"))
n1=int(input("enter n2"))
# methode to print doc string
# doc string means the defination of our progrme
print(codex.__doc__)
print(codex(n,n1))