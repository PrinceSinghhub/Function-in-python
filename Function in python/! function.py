def factorial(n):
    f=1
    if n<0:

      for i in range(n,0):
        f=f*i
      
      return f
      
     
    elif n>0: 
         for i in range(1,n+1):
            f=f*i
         return f
n=int(input("enter the"))
print(factorial(n))