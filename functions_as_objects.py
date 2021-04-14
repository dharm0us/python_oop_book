################### using functions as attributes/monkey patching
# replacing method of an object or a class
class A: 
    def print(self): 
        print("my class is A") 
 
def fake_print(): 
    print("my class is not A") 
 
a = A() 
a.print() 
a.print = fake_print 
a.print() 

def my_function():
    print("The Function Was Called")

my_function.description = "A silly function"

def second_function():
    print("The second was called")

second_function.description = "A sillier function."

def another_function(function):
    print("The description:", end=" ")
    print(function.description)
    print("The name:", end=" ")
    print(function.__name__)
    print("The class:", end=" ")
    print(function.__class__)
    print("Now I'll call the function passed in")
    function()

another_function(my_function)
another_function(second_function)
################## Event driven timer
import datetime
import time

class TimedEvent:
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        return self.endtime <= datetime.datetime.now()

class Timer:
    def __init__(self):
        self.events = []

    def call_after(self, delay, callback):
        end_time = datetime.datetime.now() + datetime.timedelta(
            seconds=delay
        )

        self.events.append(TimedEvent(end_time, callback))

    def run(self):
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)

def format_time(message, *args):
    now = datetime.datetime.now()
    print(f"{now:%I:%M:%S}: {message}")

def one(timer):
    format_time("Called One")

def two(timer):
    format_time("Called Two")

def three(timer):
    format_time("Called Three")

class Repeater:
    def __init__(self):
        self.count = 0

    def repeater(self, timer):
        format_time(f"repeat {self.count}")
        self.count += 1
        timer.call_after(5, self.repeater)

timer = Timer()
timer.call_after(1, one)
timer.call_after(2, one)
timer.call_after(2, two)
timer.call_after(4, two)
timer.call_after(3, three)
timer.call_after(6, three)
repeater = Repeater()
timer.call_after(5, repeater.repeater) # a method can be used as callback too, just like a function
format_time("Starting")
timer.run()