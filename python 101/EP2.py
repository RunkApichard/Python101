Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = Runk
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    name = Runk
NameError: name 'Runk' is not defined
name = 'Runk'
print(name)
Runk
type (name)
<class 'str'>
name.lower()
'runk'
name.upper()
'RUNK'
friend = 'Xman'
print('สวัสดี นาย สบายดีไหม')
สวัสดี นาย สบายดีไหม
print('สวัสดี Xman สบายดีไหม')
สวัสดี Xman สบายดีไหม
print ('สวัสดี'+ friend+'สบายดรไหม')
สวัสดีXmanสบายดรไหม
money = 10
print(friend + 'give me' +money)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(friend + 'give me' +money)
TypeError: can only concatenate str (not "int") to str
type (money)
<class 'int'>
>>> print(friend + 'give me' +str(money)+ 'บาท')
Xmangive me10บาท
>>> print('{}ยืมเงิน {} บาท'.format(friend,money))
Xmanยืมเงิน 10 บาท
>>> print(f'{friend}ยืมเงิน {money} บาท')
Xmanยืมเงิน 10 บาท
>>> money = 898989898
>>> print(f'{money:,'}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> print(f'{money:,}')
898,989,898
>>> print(f'{money:,.2f}')
898,989,898.00
>>> import math
>>> math.pi
3.141592653589793
>>> math.pi * (5 ** 2)
78.53981633974483
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2023, 2, 10, 7, 13, 11, 507028)
>>> datetime.now().strftime('%y%m%d  %h:%m:%s')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    datetime.now().strftime('%y%m%d  %h:%m:%s')
ValueError: Invalid format string
>>> datetime.now().strftime('%y%m%d %h:%m:%s')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    datetime.now().strftime('%y%m%d %h:%m:%s')
ValueError: Invalid format string
>>> datetime.now().strftime('%y%m%d %h:%m:%s')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    datetime.now().strftime('%y%m%d %h:%m:%s')
ValueError: Invalid format string
>>> import random
>>> random.randint(1,7)
6
>>> store = ['ป้าส้ม','ลุงดำ']
>>> random.choices(store)
['ลุงดำ']
