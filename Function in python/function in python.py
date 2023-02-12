Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #int
>>> x=int(5.40)
>>> x
5
>>> #float
>>> x=float(3.1415)
>>> x
3.1415
>>> #eval
>>> x=eval(input())
3.1416
>>> x
3.1416
>>> #max
>>> a=(25,20,6,10,6,5,60)
>>> max(a)
60
>>> #min
>>> a=(25,20,6,10,6,5,60)
>>> min(a)
5
>>> #abs
>>> a=abs(-399)
>>> a
399
>>> #type
>>> a=50
>>> type(a)
<class 'int'>
>>> x=5030.60
>>> type(x)
<class 'float'>
>>> s="Prince Singh"
>>> type(s)
<class 'str'>
>>> #length
>>> a="Sage university indore"
>>> len(a)
22
>>> #round
>>> round(4.6)
5
>>> round(4.5)
4
>>> round(10.15)
10
>>> round(6.8)
7
>>> #moduls
>>> import random
>>> help(random)

>>> random.random()
0.2700190914243721
>>> random.randrange(1,6)
4
>>> random.randrange(1,6)
1
>>> random.randrange(1,6)
2
>>> random.randrange(1,6)
4
>>> random.randint(1,6)
6
>>> random.randint(1,6)
5
>>> random.randint(1,6)
6
>>> random.randint(1,6)
5
>>> random.randint(1,6)
4
>>> random.uniform(1,6)
4.930936651770564
>>> random.uniform(1,6)
5.90165298239601
>>> random.uniform(1,6)
2.6243580107816697
>>> random.uniform(1,6)
3.651008016519654
>>> random.uniform(1,6)
1.010626431003074
>>> direction=("guru ji","creat","my","future")
>>> random.choice(direction)
'my'
>>> random.choice(direction)
'guru ji'
>>> random.choice(direction)
'guru ji'
>>> random.choice(direction)
'my'
>>> #math
>>> import math as m
>>> m.cos(45)
0.5253219888177297
>>> m.sin(90)
0.8939966636005579
>>> m.e
2.718281828459045
>>> m.log(40)
3.6888794541139363
>>> m.e**0
1.0
>>> m.pi
3.141592653589793
>>> m.log(1)
0.0
>>> #string
>>> import string as s
>>> s.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> dir(s)
['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_sentinel_dict', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
>>> s="prince"
>>> type(s)
<class 'str'>
>>> len(s)
6
>>> 