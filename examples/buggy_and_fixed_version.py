"""
Collection of bugs for DeepDebug to fix :p
"""


#Fixed
def get_leading_whitespace(string):
    start,end = re.match('^(\s*)',string).span()
    return string[start:end]

#Buggy
#--bug-fun 'examples/whitespace_buggy.py:get_leading_whitespace'
import re

def get_leading_whitespace(string):
    start,end = re.match('^(\s*)',string)
    return string[start:end]

#Buggy
#--bug-fun 'examples/gcd.py:gcd'
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(a % b, b)

#Buggy
#--bug-fun 'examples/hash_dict.py:hash_dict'
import json

def hash_dict(dic):
    return hash(dic)

#Buggy
#--bug-fun 'examples/chunks.py:chunks'
def chunks(list_, chunk_size):
    """Yield successive chunks of length chunk_size from list_"""
    for i in range(0, len(list_), chunk_size):
        yield list_[chunk_size:i + chunk_size]

#Buggy
#--bug-fun 'examples/partition.py:partition'
from copy import deepcopy
import random
def partition(list_, num_parts):
    list_copy = deepcopy(list_)
    list_copy = random.shuffle(list_copy)
    return [list_copy[i::num_parts] for i in range(num_parts)]
