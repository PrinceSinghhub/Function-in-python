def decorator(pr):
    def inner():
        a=pr()
        add=a+5
        return add
    return inner
@decorator
def pr():
    return n
n=int(input("N"))
print(pr()) 