import sys
sys.path.append("/home/runner/pythonoop/supplychain/")
from ecommerce.db import Database as db1
d = db1()
print(d)

# OR but then you have to run it like
# python -m ecommerce.product from the "supplychain" directory
# whereas the above import can be run from current directory as well, like:
# python product.py
from .db import Database as db2
d = db2()
print(d)