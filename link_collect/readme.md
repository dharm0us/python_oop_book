A simple program to collect all the links from a website.
It will output a dictionary, key is a page url, value is all the pages pointed to from that page.

$ docker run -p8000:8000 -it python:3.8 bash
$ python -m http.server &
$ python link_collection.py http://localhost:8000/

Output:

http://localhost:8000: {'http://localhost:8000/contact.html', 'http://localhost:8000/esme.html', 'http://localhost:8000/blog.html', 'http://www.archlinux.org', 'http://localhost:8000/hobbies.html'}
http://localhost:8000/contact.html: set()
http://localhost:8000/esme.html: set()
http://localhost:8000/blog.html: set()
http://www.archlinux.org: set()
http://localhost:8000/hobbies.html: set()
