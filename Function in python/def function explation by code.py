#positional agrument
def pr(name,age):
    print("Hello",name,"Good morning")
    print("Your age is ",age)
pr("Prince",18)
#key word argument
pr(age=18,name="Prince")

#default argument
def nr(name='prince',age=18):
    print("Heloo",name)
    print("your agr is" ,age)
nr()

#variable argument
def pr(*name):
    for i in name:
        print("Hey",i,"Good morning")
pr("Prince","Singh") 
#return frome function

def si():
    A=(p*r*t)/100
    return A
p=int(input('enter a Price'))
r=float(input('enter a rate'))
t=int(input('enter a time'))         
print("si is",si())

#assining a main function
print("Main function programne")
def si(p,r,t):
    A=(p*r*t)/100
    return A
def main():
    print(si(10000,11.54,6))
if __name__ == '__main__':
    main()
    

