'''
syntax of function

def function_name(arg):
    #stmts
    return

function_name(parameters)

example:
def wish(name):
    print(f'Hello {name}, Welcome to "python 100 days of program"')
wish('prudhvi')
wish('nandhan')
wish('reddy')

positional arguments:

def display(username,email,password):
    print("Username:",username)
    print("Email:",email)
    print("Password:",password)

display('prudhvi','prudhvi@gmail.com','p@123')
display('nandhan','nandhan@gmail.com','n@456')
display('reddy','reddy@gmail.com','r@789')


keyword arguments:
    
def display(username,email,password):
    print("Username:",username)
    print("Email:",email)
    print("Password:",password)

display(username='prudhvi',email='nandhan@gmail.com',password='p@123')
display(email='prudhvi@gmail.com',username='prudhvi',password='p@123')
display(password='p@123',email='nandhan@gmail.com',username='prudhvi')


default arguments:
   
def display(username,email,password='',phoneno='+91'):
    print("Username:",username)
    print("Email:",email)
    print("Password:",password)
    print("Phone no:",phoneno)
    
display('prudhvi','@gmail.com','p@123','1234567890')
display('nandhan','@gmail.com')


def display(*names):
    print(names)

display('prudhvi','nandhan','reddy')
display('prudhvi','nandhan')
display('prudhvi')
'''
def display(**names):
    print(names)

display(n1='prudhvi',n2='nandhan',n3='reddy')
display(n1='prudhvi',n2='nandhan')
display(n1='prudhvi')
