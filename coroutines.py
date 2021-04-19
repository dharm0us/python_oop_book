def tally():
  score = 0
  print("h1")
  while True:
    print("h2")
    increment = yield score
    print("h3")
    score += increment
    print("h4")

team1 = tally()
print(next(team1)) # this reaches line 6, returns current value of score and waits for next value to arrive
print(team1.send(3)) # this makes the value of increment 3, adds it to score, returns score on line 6 and waits for next send
print(team1.send(3)) # same as above

# so the difference between coroutine and generator is that coroutine consumes and generates a value whereas generator only generates.

'''
Serial matcher, see the log file EXAMPLE_LOG.log you will see what we are trying to do
'''
import re

def match_regex(filename, regex):
    with open(filename) as file:
        lines = file.readlines()
    for line in reversed(lines):
        match = re.match(regex, line)
        if match:
            regex_sent_via_send = yield match.groups()[0]
            regex = regex_sent_via_send

def get_serials(filename):
    ERROR_RE = "XFS ERROR (\[sd[a-z]\])"
    matcher = match_regex(filename, ERROR_RE)
    device = next(matcher)
    while True:
        try:
            bus = matcher.send(
                "(sd \S+) {}.*".format(re.escape(device))
            )
            serial = matcher.send("{} \(SERIAL=([^)]*)\)".format(bus))
            yield serial
            device = matcher.send(ERROR_RE)
        except StopIteration:
            matcher.close()
            return

for serial_number in get_serials("EXAMPLE_LOG.log"):
    print(serial_number)

'''
Normal generators signal their exit from inside by raising StopIteration. If we chain multiple generators together (for example, by iterating over one generator from inside another), the StopIteration exception will be propagated outward. Eventually, it will hit a for loop that will see the exception and know that it's time to exit the loop.

Even though they use a similar syntax, coroutines don't normally follow the iteration mechanism. Instead of pulling data through one until an exception is encountered, data is usually pushed into it (using send). The entity doing the pushing is normally the one in charge of telling the coroutine when it's finished. It does this by calling the close() method on the coroutine in question.

When called, the close() method will raise a GeneratorExit exception at the point the coroutine was waiting for a value to be sent in. It is normally good policy for coroutines to wrap their yield statements in a try...finally block so that any cleanup tasks (such as closing associated files or sockets) can be performed.
'''

'''
The relationship between coroutines/generators/functions.

We've seen coroutines in action, so now let's go back to that discussion of how they are related to generators. In Python, as is so often the case, the distinction is quite blurry. In fact, all coroutines are generator objects, and authors often use the two terms interchangeably. Sometimes, they describe coroutines as a subset of generators (only generators that return values from yield are considered coroutines). This is technically true in Python, as we've seen in the previous sections.

However, in the greater sphere of theoretical computer science, coroutines are considered the more general principles, and generators are a specific type of coroutine. Further, normal functions are yet another distinct subset of coroutines.

A coroutine is a routine that can have data passed in at one or more points and get it out at one or more points. In Python, the point where data is passed in and out is the yield statement.

A function, or subroutine, is the simplest type of coroutine. You can pass data in at one point, and get data out at one other point when the function returns. While a function can have multiple return statements, only one of them can be called for any given invocation of the function.

Finally, a generator is a type of coroutine that can have data passed in at one point, but can pass data out at multiple points. In Python, the data would be passed out at a yield statement, but you can't pass data back in. If you called send, the data would be silently discarded.

So, in theory, generators are types of coroutines, functions are types of coroutines, and there are coroutines that are neither functions nor generators. That's simple enough, eh? So, why does it feel more complicated in Python?

In Python, generators and coroutines are both constructed using a syntax that looks like we are constructing a function. But the resulting object is not a function at all; it's a totally different kind of object. Functions are, of course, also objects. But they have a different interface; functions are callable and return values, generators have data pulled out using next(), and coroutines have data pushed in using send.
'''