def pr():
    for i in range (n1,n2+1):
        if n1>1:
            for j in range (2,i):
                if (i%j)==0:
                    break
            
            else:
                print(i)
n1=int(input("Enter a number"))
n2=int(input("Enter a number"))
pr()
# import os
# print(os.listdir())