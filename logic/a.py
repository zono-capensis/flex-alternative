import sys
import os.path
sys.path.insert(0, os.path.abspath('../data'))

from  structures import Stack

a = Stack()
a.push([1,2,3])
print(str(a))