#!/usr/bin/env python

import pickle

# declare a list
mylist = []

# assigning value to list
mylist.append('This is string')     # string
mylist.append(5)                    # integer
mylist.append(('localhost', 5000))  # tuple

# print list
print("----- This is original list: -----\n") 
print(mylist, "\n\n")

# pickle object (in this example, the object is a list)
p = pickle.dumps(mylist)

# print pickled object
print("----- This is pickled list: -----\n") 
print(p, "\n\n")

# unpickle object
u = pickle.loads(p)

# print unpickled object
print("----- This is unpickled list: -----\n") 
print(u, "\n\n")
