#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2015

@author: shenzb
'''

class Node(object):
    '''
    classdocs
    '''
    #__slots__ = ('character', 'count', 'leftChild', 'rightChild')

    def __init__(self, character, count, leftChild = None, rightChild = None):
        '''
        Constructor
        '''
        self.__character = character
        self.__count     = count

    def getCharacter(self):
        return self.__character

    def getCount(self):
        return self.__count

    def plus(self, other):
        return Node(None, self.getCount() + other.getCount())

    def compare(self, other):
        if self.__count > other.__count:
            return 1
        elif self.__count < other.__count:
            return -1
        else:
            return 0
