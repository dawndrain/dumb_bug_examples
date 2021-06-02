from copy import deepcopy
import random
def partition(list_, num_parts):
    list_copy = deepcopy(list_)
    list_copy = random.shuffle(list_copy)
    return [list_copy[i::num_parts] for i in range(num_parts)]
