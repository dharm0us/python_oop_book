a = "hello" 
b = 'world'
c = '''a multiple 
line string''' 
d = """More 
multiple""" 
e = ("Three " "Strings " 
        "Together") 
l = [a,b,c,d,e]
for index,item in enumerate(l):
  print(str(index) + ". " + item)

  # string formatting
orders = [("burger", 2, 5), ("fries", 3.5, 1), ("cola", 1.75, 3)]

print("PRODUCT QUANTITY PRICE SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print(
        f"{product:10s}{quantity: ^9d} "
        f"${price: <8.2f}${subtotal: >7.2f}"
    )
# each formatting string has this order from left to right
# padding character,alignment,size,type
# default padding char for integers/floats is 0 but we specified space
# ^ => center alignment, < => left alignment, > => right

# Unicode
characters = b'\x63\x6c\x69\x63\x68\xe9' 
# characters is now a bytes object
print(characters) # they will be treated as ASCII characters so last char won't be printed correctly
print(characters.decode("latin-1")) # output of decode() is a Unicode string which was output by decode by decoding bytes using "latin-1" encoding
# if we had used Cyrillic iso8859-5 encoding, we'd have ended up with the 'clichщ' string since last byte maps to a different char in that encoding
print(characters.decode("iso8859-5"))

# reverse of the above operation, convert string to bytes using a certain encoding
characters = "cliché" 
print(characters.encode("UTF-8")) 
print(characters.encode("latin-1")) 
print(characters.encode("CP437")) 
# this one will throw an error - ascii codec can't encode a character print(characters.encode("ascii"))
# or you can use the second parameter - errors in a way that you get some output. By default it's strict but you can make it replace/ignore etc.