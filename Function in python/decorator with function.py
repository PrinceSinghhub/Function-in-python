def pr():
    print("Prince")
a=pr
del pr
a()

#return function by function
def pr(n):
    if n==0:
        return print
    if n==1:
        return int
p=pr(1)
print(p)

#put function in function as aargument
def pr(a):
     a("hi prince")
pr(print)