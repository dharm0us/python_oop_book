'''
The below code creates a list of dicts from a tsv file where first line is the header line.
'''
import sys

filename = "contacts.tsv"

with open(filename) as file:
    header = file.readline().strip().split("\t")
    contacts = [
        dict(
        zip(header, line.strip().split("\t")))
        for line in file
    ]

for contact in contacts:
    print("email: {email} -- {last}, {first}".format(**contact))

'''
Creating sets using comprehension
'''
from collections import namedtuple

Book = namedtuple("Book", "author title genre")
books = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief Of Time", "fantasy"),
    Book("Le Guin", "The Dispossessed", "scifi"),
    Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
    Book("Turner", "The Thief", "fantasy"),
    Book("Phillips", "Preston Diamond", "western"),
    Book("Phillips", "Twice Upon A Time", "scifi"),
]

fantasy_authors = {b.author for b in books if b.genre == "fantasy"}
print(fantasy_authors)
'''
Create dicts
'''
fantasy_titles = {b.title: b for b in books if b.genre == "fantasy"}
print(fantasy_titles)
'''
Generator pattern
If we don't want to create a container such as list/set/dict but want to process a sequence in a memory efficient way - for e.g. process a huge file, line by line rather than getting everything in memory all at once - we can use Generator pattern.
Wrapping a for expression in () doesn't create a tuple, it creates a generator expression. For iterators we wrapped for expressions in [] or {}.
'''
inputfile = "input_log"
outputfile = "output_log"
with open(inputfile) as infile: 
    with open(outputfile, "w") as outfile: 
        warnings = (l for l in infile if 'WARNING' in l) 
        for l in warnings: 
            outfile.write(l)

# replace the word "WARNING" in the output file
with open(inputfile) as infile:
    with open(outputfile, "w") as outfile:
        warnings = (
            l.replace("\tWARNING", "") for l in infile if "WARNING" in l
        )
        for l in warnings:
            outfile.write(l)

# do the above without generators, one additional indent
with open(inputfile) as infile:
    with open(outputfile, "w") as outfile:
        for l in infile:
            if "WARNING" in l:
                outfile.write(l.replace("\tWARNING", ""))

# Let's create an OOP solution for this
class WarningFilter:
    def __init__(self, insequence):
        self.insequence = insequence

    def __iter__(self):
        return self

    def __next__(self):
        l = self.insequence.readline()
        while l and "WARNING" not in l:
            l = self.insequence.readline()
        if not l:
            raise StopIteration
        return l.replace("\tWARNING", "")

with open(inputfile) as infile:
    with open(outputfile, "w") as outfile:
        filter = WarningFilter(infile)
        for l in filter:
            outfile.write(l)

# Python does something similar to the above OOP solution, when we use yield keyword. Yield is similar to return but when the same function is called the next time, it resumes from where it left.
def warnings_filter(insequence):
    for l in insequence:
        if "WARNING" in l:
            yield l.replace("\tWARNING", "")

with open(inputfile) as infile:
    with open(outputfile, "w") as outfile:
        filter = warnings_filter(infile)
        for l in filter:
            outfile.write(l)

# so the method warning_filter returns a special type of object which is quite similar to the class we defined just above
# let's inspect it
print(warnings_filter([]))
print(dir(warnings_filter([]))) # notice that this has __iter__ and __next__ methods