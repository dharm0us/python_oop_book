#by the virtue of being immutable, tuples can be used as dictionary keys

#both the below tuple assignments are identical in outcome
#so, for creating a tuple, parenthese are optional
t = ("winnie", 12, 3)
t1 = "winnie", 12, 3

if t == t1:
  print("yes")

# you can use unpacking and slicing on tuples but it might make the code unreadable

# named tuples - good choice for data only representations
from collections import namedtuple 
Stock = namedtuple("Stock", ["symbol", "current", "high", "low"])
stock = Stock("FB", 177.46, high=178.67, low=175.79)