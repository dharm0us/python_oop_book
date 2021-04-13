class Silly:
    def _get_silly(self):
        print("You are getting silly")
        return self._silly

    def _set_silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("Whoah, you killed silly!")
        del self._silly

    silly = property(_get_silly, _set_silly, _del_silly, "This is a silly property")
  
s = Silly()
help(Silly)
s.silly = "funny"
print(s.silly)
del s.silly
print(s.silly) #since it was deleted in the previous line, you will get AttributeError
# Deletion of a name removes the binding of that name from the local or global namespace
############################################
# Another way to do the same thing with decorators:
class Silly1: 
    @property 
    def silly(self): 
        "This is a silly property" 
        print("You are getting silly") 
        return self._silly 
 
    @silly.setter 
    def silly(self, value): 
        print("You are making silly {}".format(value)) 
        self._silly = value 
 
    @silly.deleter 
    def silly(self): 
        print("Whoah, you killed silly!") 
        del self._silly 