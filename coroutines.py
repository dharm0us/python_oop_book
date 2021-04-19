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