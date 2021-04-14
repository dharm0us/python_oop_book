song_library = [
    ("Phantom Of The Opera", "Sarah Brightman"),
    ("Knocking On Heaven's Door", "Guns N' Roses"),
    ("Captain Nemo", "Sarah Brightman"),
    ("Patterns In The Ivy", "Opeth"),
    ("November Rain", "Guns N' Roses"),
    ("Beautiful", "Sarah Brightman"),
    ("Mal's Song", "Vixy and Tony"),
]

artists = set() # no special syntax for creating empty set like lists and dicts
# but you can create a set like
# {"val1", "val2"}
# note that it's similar to dicts' syntax without colons
for song, artist in song_library:
    artists.add(artist)

print(artists)

# sets can store values which are hashable which is same as what can be used as keys in dicts so dicts and lists are out.

# converting sets to lists
l = list(artists)
artists1 = set([item + "1" for item in l]) # list to set
print(artists | artists1) # union of sets
print(artists.union(artists1)) # union again

# for intersection use intersection() method or logical and (&)
# symmetric_difference is the method for finding the elements which are not common in both the sets

# assymetric methods
# issubset
# issuperset
# difference (- operator)
