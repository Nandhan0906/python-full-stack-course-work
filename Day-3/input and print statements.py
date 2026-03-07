Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name=input("Enter the name: ")
Enter the name: prudhvi
name
'prudhvi'
age=input("Enter the age: ")
Enter the age: 20
age
'20'
age=int(input("Enter the age: "))
Enter the age: 20
age
20
type(age)
<class 'int'>
price=input("Enter the price: ")
Enter the price: 110.99
price
'110.99'
type(price)
<class 'str'>
'prudhvi nandhan reddy'
'prudhvi nandhan reddy'
'prudhvi nandhan reddy'.split()
['prudhvi', 'nandhan', 'reddy']
'prudhvi nandhan reddy'.split(',')
['prudhvi nandhan reddy']
KeyboardInterrupt
'prudhvi nandhan reddy'.split(',')
['prudhvi nandhan reddy']
names=input("Enter the names: ")
Enter the names: prudhvi nandhan reddy
names
'prudhvi nandhan reddy'
names=input("Enter the names: ").split()
Enter the names: prudhvi nandhan reddy
names
['prudhvi', 'nandhan', 'reddy']
numbers=int(input("Enter the numbers: ").split())
Enter the numbers: 1 2 3
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    numbers=int(input("Enter the numbers: ").split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
numbers=list(map(int,input("Enter the numbers: ").split()))
Enter the numbers: 1 2 3 4 5 6
numbers
[1, 2, 3, 4, 5, 6]
numbers=list(map(float,input("Enter the numbers: ").split()))
Enter the numbers: 7 8 5 6 
numbers
[7.0, 8.0, 5.0, 6.0]
numbers=tuple(map(float,input("Enter the numbers: ").split()))
Enter the numbers: 5 8 6 2 9
numbers
(5.0, 8.0, 6.0, 2.0, 9.0)
numbers=list(map(int,input("Enter the numbers: ").split()))
Enter the numbers: 8 9 6 4 2 
numbers
[8, 9, 6, 4, 2]
numbers=tuple(map(int,input("Enter the numbers: ").split()))
Enter the numbers: 8 9 6 4  7 3
numbers
(8, 9, 6, 4, 7, 3)
numbers=tuple(map(float,input("Enter the numbers: ").split()))
Enter the numbers: 8 5.6 9 7.4 2.8 3
numbers
(8.0, 5.6, 9.0, 7.4, 2.8, 3.0)
names=tuple(input("Enter the names: ").split())
Enter the names: prudhvi nandhan reddy
names
('prudhvi', 'nandhan', 'reddy')
names=set(input("Enter the names: ").split())
Enter the names: prudhvi nandhan reddy
names
{'reddy', 'nandhan', 'prudhvi'}
numbers=set(map(float,input("Enter the numbers: ").split()))
Enter the numbers: 8 5 2 6 9 3 
numbers
{2.0, 3.0, 5.0, 6.0, 8.0, 9.0}
numbers=set(map(int,input("Enter the numbers: ").split()))
Enter the numbers: 8 5 2 6 9 3
numbers
{2, 3, 5, 6, 8, 9}
d=eval(input("Enter the input: "))
Enter the input: {5:6, 9:8, 4:7}
d
{5: 6, 9: 8, 4: 7}
d=eval(input("Enter the input: "))
Enter the input: [1,2,3,4,5,6]
d
[1, 2, 3, 4, 5, 6]
username,password=['py','py123']
username
'py'
password
'py123'
username,password=input("Enter the username and password: ").split()
Enter the username and password: prudhvi prudhvi@123
>>> username
'prudhvi'
>>> password
'prudhvi@123'
>>> a,b,c=list(map(int,input("enter the sides: ").split()))
enter the sides: a
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a,b,c=list(map(int,input("enter the sides: ").split()))
ValueError: invalid literal for int() with base 10: 'a'
>>> a,b,c=list(map(int,input("enter the sides: ").split()))
enter the sides: 10 20 30
>>> a
10
>>> b
20
>>> c
30
>>> a=10
>>> b=5
>>> a+b
15
>>> a-b
5
>>> a*b
50
>>> a/b
2.0
>>> a<b
False
>>> a>b
True
>>> a>=b
True
>>> a<=b
False
>>> a==b
False
>>> a!=b
True
>>> a=20
>>> a=a+10
>>> a
30
>>> 6
6
