class LenClass:
  def __len__(self):
    return 1

l = LenClass()
print(len(l))

class OddContainer: 
    def __contains__(self, x): 
        if not isinstance(x, int) or not x % 2: 
            return False 
        return True 

from collections import Container
print(Container.__abstractmethods__) # will return __contains__
help(Container.__contains__)
oc = OddContainer()
# both the conditions below are True even though
# OddContainer doesn't inherit from Container
# but it implements the required abstract methods
# defined in the Container class
# this is duck typing
print(isinstance(oc, Container))
print(issubclass(OddContainer, Container))
print(1 in oc) # this is how contains is actually used
print(2 in oc)

# Python's ABCs help to supply the functionality of interfaces without compromising on the benefits of duck typing.
# This is how you define an abstract class
import abc 
 
class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented
  
class Wav(MediaLoader): 
    #It's still an abstract class since it doesn't implement
    #the required methods, hence its instantiaon would fail
    pass

# this would fail
# w = Wav()

class Ogg(MediaLoader):
  ext = ".ogg"
  def play(self):
    pass

o = Ogg() # this is fine

# we can implement MediaLoader without inheriting from it
class Ogg1():
    ext = '.ogg' 
    def play(self):
       print("this will play an ogg file")

print(issubclass(Ogg1, MediaLoader))
print(isinstance(Ogg1(), MediaLoader))ls