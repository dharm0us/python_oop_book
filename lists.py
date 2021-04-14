# sorting
# define _lt_ function in the class
# now a list of these objects would be sorted as per this logic when you call sort on the list.
class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        return f"{self.string}:{self.number}"
    
# similarly, implement __gt__, __eq__, __ne__, __ge__, and __le__ methods so that all of the <, >, ==, !=, >=, and <= operators also work properly. 
# Or you can get this for free by implementing __lt__ and __eq__, and then applying the @total_ordering class decorator to supply the rest:
from functools import total_ordering 
 
@total_ordering 
class WeirdSortee1: 
    def __init__(self, string, number, sort_num): 
        self.string = string 
        self.number = number 
        self.sort_num = sort_num 
 
    def __lt__(self, object): 
        if self.sort_num: 
            return self.number < object.number 
        return self.string < object.string 
 
    def __repr__(self): 
        return f"{self.string}:{self.number}"
 
    def __eq__(self, object):
        return all(( 
            self.string == object.string, 
            self.number == object.number, 
            self.sort_num == object.number 
        )) 
'''
There are a few sort key operations that are so common that the Python team has supplied them so you don't have to write them yourself. For example, it is common to sort a list of tuples by something other than the first item in the list. The operator.itemgetter method can be used as a key to do this:
'''
from operator import itemgetter
l = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]
l.sort(key=itemgetter(1)) # sort by second item in the tuple
print(l)
# itemgetter can be used with dictionaries as well
# similar methods are attrgetter/methodcaller
