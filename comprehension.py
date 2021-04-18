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