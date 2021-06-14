>>> while True pint('Hello world')
  File "<stdin>", line 1
    while True pint('Hello world')
               ^
SyntaxError: invalid syntax

 >>> 10 * {1/10}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'int' and 'set'
>>> 10 * (1/10)
1.0
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
  
>>> while True:
...     try:
...             x = int(input("Please enter a number: "))
...             break
...     except ValueError:
...             print("Oops!  That was no valid number.  Try again...")
...
Please enter a number: t
Oops!  That was no valid number.  Try again...
Please enter a number: 5
  
...     except (RuntimeError, TypeError, NameError):
...             pass

>>> class B(Exception):
...     pass
...
>>> class C(B):
...     pass
...
>>> class D(C):
...     pass
...
>>> for cls in [B, C, D]:
...     try:
...         raise cls()
...     except D:
...         print("D")
...     except C:
...         print("C")
...     except B:
...         print("B")
...
B
C
D

>>> import sys
>>> try:
...     f = open('myfile.txt')
...     s = f.readline()
...     i = int(s.strip())
... except OSError as err:
...     print("OS error: {0}".format(err))
... except ValueError:
...     print("Could not convert data to an integer.")
... except:
...     print("Unexpected error:", sys.exc_info()[0])
...     raise
...

>>> for arg in sys.argv[1:]:
...     try:
...             f = open(arg, 'r')
...     except OSError:
...             print('cannot open', arg)
...     else:
...             print(arg, 'has', len(f.readlines()), 'lines')
...             f.close()
...
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)
...     print(inst)
...
...     x, y = inst.args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs

>>> def this_fails():
...     x = 1/0
...
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
  
>>> raise ValueError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError

raise ValueError  # shorthand for 'raise ValueError()'

>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
  
# exc must be exception instance or None.
raise RuntimeError from exc

>> def func():
...     raise IOError
...
>>> try:
...     func()
... except IOError as exc:
...      raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
OSError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
  
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError

>>> class Error(Exception):
...     pass
... class InputError(Error):
  File "<stdin>", line 3
    class InputError(Error):
    ^
SyntaxError: invalid syntax
>>> class Error(Exception):
...     pass
...
>>> class InputError(Error):
...     def __init__(self, expression, message):
...             self.expression = expression
...             self.message = message
...
>>> class TransitionError(Error):
...     def __init__(self, previous, next, message):
...             self.previous = previous
...             self.next = next
...             self.message = message
...

>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt

>>> def bool_return():
...     try:
...              return True
...     finally:
...             return False
...

>>> for line in open("myfile.txt"):
...     print(line, end="")
...

>>> with open("myfile.txt") as f:
...     for line in f:
...             print(line, end="")
...
