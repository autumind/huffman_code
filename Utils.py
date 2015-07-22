#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2015

@author: shenzb.fnst
'''

def stringToPriorityQueue(text):
    '''
    Transfer every character of a string to priority queue.
    Priority order is according to character's count of the string.
    '''
    chars = list(text)
    char_dict = dict([(c, 0) for c in chars])

    for char in chars:
        char_dict[char] = char_dict[char] + 1

    ''' sort dict '''
    char_list = sorted(char_dict.items(), lambda x, y: cmp(x[1], y[1]))

    return char_list
