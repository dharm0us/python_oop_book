# placing __init__.py inside a folder tells python that this folder is a package.
# we can use some imports here which could be used by all modules inside this package
# for e.g.
# from .database import db
# then other modules can do
# from ecommerce import db
# check supply.py for example