#int,float,str,list,tuple,set,dict

def display(n):
    n+=(8,9)
    print("Inside:",n)

n=(1,2,3,4)
display(n)
print("Outside:",n)
