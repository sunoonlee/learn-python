#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random

def get_random_string(n):
    "args: n - int, length of string to generate"
    string = ""
    for i in range(n):
        string += chr(random.randrange(33, 127)) # from '!' to '~'
    return string

if __name__ == '__main__':
    for i in range(200):
        print(get_random_string(16))