# simplest class
class Simplest:
  pass
'''
multi
line 
comment
using single quotes
It's called docstring as well.
'''
s = Simplest()
print(s)
"""
multi
line 
comment
using double quotes
It's called docstring as well.
"""
# add attributes on the fly
s.x = 10
print(s.x)

# loading the file interactively
# python -i main.py
# then do
# help(ClassWithInit) - its docstring will be printed
# similarly for help(ClassWithInit.desc)

class ClassWithInit:
  '''
  Initializer is different from constructor.
  Constructor is __new__.
  But it's rarely used.
  '''
  def __init__(self):
    self.y = 100
  
  def desc(self):
    '''
    self method
    '''
    pass

c = ClassWithInit()
print(c.y)

# don't use import *, makes it difficult to figure out where a particular class came from