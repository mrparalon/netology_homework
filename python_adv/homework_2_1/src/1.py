import os
from pprint import pprint

old_environ = os.environ.copy()
new_environ = os.environ
new_environ.clear()

os.environ = old_environ
print(os.environ)

