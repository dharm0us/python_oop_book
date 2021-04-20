'''
In python, it's common to use decorator pattern on functions. Look at log_calls below. It wraps an existing function while adding additional functionality.
'''

import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print(
            "Calling {0} with {1} and {2}".format(
                func.__name__, args, kwargs
            )
        )
        return_value = func(*args, **kwargs)
        print(
            "Executed {0} in {1}ms".format(
                func.__name__, time.time() - now
            )
        )
        return return_value

    return wrapper

def test1(a, b, c):
    print("\ttest1 called")

def test2(a, b):
    print("\ttest2 called")

def test3(a, b):
    print("\ttest3 called")
    time.sleep(1)

test1 = log_calls(test1)
test2 = log_calls(test2)
test3 = log_calls(test3)

test1(1, 2, 3)
test2(4, b=5)
test3(6, 7)

# we can use the decorator directly above the function name as well to make it more readable. This essentially replaces the function with a modified filter

@log_calls
def test4():
  print("test4 called")

test4()

# similarly you can use decorators on classes which means that the class is replaced with a new class.