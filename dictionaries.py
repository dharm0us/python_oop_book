# useful dict methods
# setdefault, get (with default value if key missing)
# most of the objects use dictionaries under the hood.
# namedtuples, dataclasses, dictionaries are quite similar. dicts are more dynamic in the sense that you can have variable number of attributes. namedtuples vs dataclasses => you can iterate over tuples but not dataclasses. namedtuples are immutable.

class AnObject:
  pass

# you can use an object as dict key since its ref is used for hashing, below you can see that even after modification of the object, you have the correct mapping
a = AnObject()
a.val = 13
print(a.val)
d = {}
d[a] = "new"
print(d[a])
a.val = 14
print(d[a])
# but a list can't be used as a dict key, since it doesn't implement hash method and makers didn't think it appropriate to use its ref to be hashed.

# defaultdict
# pass a function in its constructor which will be executed to set the value every time a key is not found. 
from collections import defaultdict

num_items = 0 

def tuple_counter(): 
    global num_items 
    num_items += 1 
    return (num_items, []) 
 
d = defaultdict(tuple_counter)
d = defaultdict(tuple_counter)
d['a'][1].append("hello")
d['b'][1].append('world')
print(d)
###################### Counter ######
from collections import Counter 
def letter_frequency(sentence): 
    return Counter(sentence) 
print(letter_frequency("abca"))

responses = [ 
    "vanilla", 
    "chocolate", 
    "vanilla", 
    "vanilla", 
    "caramel", 
    "strawberry", 
    "vanilla" 
] 
 
print( 
    "The children voted for {} ice cream".format( 
 Counter(responses).most_common(1)[0][0] 
    ) 
) 