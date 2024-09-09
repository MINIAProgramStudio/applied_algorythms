from Set import Set
from random import random

def random_set(length, multiply_by, offset):
    set = Set()
    for i in range(length):
        set.insert(random()*multiply_by + offset)
    return set


while True:
    print(str(random_set(int(input("length>>>")), 1000, -500)))