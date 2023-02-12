def codex(a,b):
    # if use use a+b/2 the ans wrong becouse operator precedency
    av=(a+b)/2
    return av
    print(av)
n=int(input("enter n1"))
n1=int(input("enter n2"))
print(codex(n,n1))