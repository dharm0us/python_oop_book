# how to make a class use '+' operator
class SillyInt(int): 
    def __add__(self, num): 
        return 0 

a = SillyInt(1)
b = SillyInt(2)
print(a + b)

'''
Similarly use 
__contains__ for x in myobj
__setitem__ for myobj[i] = x
__getitem__ for x = myobj[i]

There are 33 of these special methods in list
>>> dir(list)

['__add__', '__class__', '__contains__', '__delattr__','__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

Get help>>> help(list.__add__)
Help on wrapper_descriptor:
   
__add__(self, value, /)
    Return self+value.  
'''