#with out use @decorator
def pr():
    print("Hi")
    print("Prince")

def decorator(p):
    def inner():
        print("Before")
        p()
        print("After")
    return inner
r=decorator(pr)
r()  

#ude decodatro
def decorator(p):
    def inner():
        print("Before")
        p()
        print("After")
    return inner
@decorator
def pr():
    print("Hi")
    print("Prince")
pr()
