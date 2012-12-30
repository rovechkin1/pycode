Python 3.2.3 (default, Oct 19 2012, 20:13:42) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> print("hello world!")
hello world!
>>> a="i am epic"
>>> b=2
>>> print (a)
i am epic
>>> print (b)
2
>>> c="too"
>>> a+c
'i am epictoo'
>>> c=" too"
>>> a+c
'i am epic too'
>>> d=a+c
>>> (d)
'i am epic too'
>>> b+2
4
>>> a*2
'i am epici am epic'
>>> a+" "
'i am epic '
>>> a=a+" "
>>> d*2
'i am epic tooi am epic too'
>>> a*2
'i am epic i am epic '
>>> a/2
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> a*2/2
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a*2/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> e=1
>>> f=3
>>> print e,b,f
SyntaxError: invalid syntax
>>> print (e,b,f)
1 2 3
>>> 
