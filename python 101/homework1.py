Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape("classic")
tao.shape("arror")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tao.shape("arror")
  File "C:\Python311\Lib\turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named arror
tao.shape("arrow")
tao.shape("circle")
for i in rang (3):
    tao.circle(20)
    tao.forward(20)

    
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    for i in rang (3):
NameError: name 'rang' is not defined. Did you mean: 'range'?
for i in range (3):
    tao.circle(20)
    tao.forward(20)

    
tao.home()
tao.clear()
for i in range (4)
SyntaxError: incomplete input
for i in range (4):
tao.reset()
SyntaxError: expected an indented block after 'for' statement on line 1

tao.reset()
tao.shape("arrow")
tao.color('red')
for i in range(4):
    tao.forward(20)
    tao.circle(20)

    
tao.home()
tao.goto('-20','-20')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tao.goto('-20','-20')
  File "C:\Python311\Lib\turtle.py", line 1777, in goto
    self._goto(Vec2D(x, y))
  File "C:\Python311\Lib\turtle.py", line 3182, in _goto
    diff = (end-start)
  File "C:\Python311\Lib\turtle.py", line 264, in __sub__
    return Vec2D(self[0]-other[0], self[1]-other[1])
TypeError: unsupported operand type(s) for -: 'str' and 'int'
tao.goto('-20,-20')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    tao.goto('-20,-20')
  File "C:\Python311\Lib\turtle.py", line 1775, in goto
    self._goto(Vec2D(*x))
TypeError: Vec2D.__new__() takes 3 positional arguments but 8 were given
tao.goto(-20,-20)
tao.reset()


tao.color(red)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    tao.color(red)
NameError: name 'red' is not defined
tao.color('red')
for i in renge(4)
SyntaxError: incomplete input
for i in range(4)
SyntaxError: incomplete input
tao.reset()

tao.color('pink')
for i in range(4)
SyntaxError: incomplete input
for i in range(4):
    tao.penup()
    tao.forward(20)
    tao.pendown()
    tao.circle(20)

    
tao.home()
tao.undo()

tao.clear()

for i in range (4)
SyntaxError: incomplete input



for i in range(4):


tao.clear()
SyntaxError: expected an indented block after 'for' statement on line 1
tao.clear()


tao.goto(-100,-100)
tao.clear()
tao.home()
tao.clear()




tao.shape(circle)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    tao.shape(circle)
NameError: name 'circle' is not defined
tao.shape('circle')
tao.colcor('green')
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    tao.colcor('green')
AttributeError: 'Turtle' object has no attribute 'colcor'. Did you mean: 'color'?
tao.color('green')
tao.penup()
tao.forward(100)
for i in range(4)
SyntaxError: incomplete input
for i in range(4):
    tao.circle(50)
    tao.pendown()
    tao.circle(50)
    tao.forward(50)
... 
...     
>>> tao.penup()
>>> tao.goto('-100,-100')
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    tao.goto('-100,-100')
  File "C:\Python311\Lib\turtle.py", line 1775, in goto
    self._goto(Vec2D(*x))
TypeError: Vec2D.__new__() takes 3 positional arguments but 10 were given
>>> tao.goto('-10,-10')
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    tao.goto('-10,-10')
  File "C:\Python311\Lib\turtle.py", line 1775, in goto
    self._goto(Vec2D(*x))
TypeError: Vec2D.__new__() takes 3 positional arguments but 8 were given
>>> tao.home()
