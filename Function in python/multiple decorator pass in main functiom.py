def decorator1(pr):
    def inner():
        a=pr()
        m=a*5
        return m
    return inner
def decorator2(pr):
    def inner():
        a=pr()
        add=a+5
        return add
    return inner
#@decorator1  #becouse we have a tow decorater
def decorator3(pr):
    def inner():
        a=pr()
        m=a-10
        return m
    return inner
#use decorator
@decorator3
@decorator2
@decorator1
def pr():
    return n
n=int(input("N"))
#n1=decorator3(decorator2(decorator1(pr)))
print(pr())