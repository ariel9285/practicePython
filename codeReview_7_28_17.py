#!/usr/bin/python
import random

def numbers():
    total=0
    for i in range(1000):
        x = random.randint(1,1000)
        total += x
    print(total)

numbers()
