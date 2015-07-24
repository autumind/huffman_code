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
        self.__character  = character
        self.__count      = count
        self.__leftChild  = leftChild
        self.__rightChild = rightChild

    def getCharacter(self):
        return self.__character

    def getCount(self):
        return self.__count

    def getLeftChild(self):
        return self.__leftChild

    def getRightChild(self):
        return self.__rightChild

    def setLeftChild(self, leftChild):
        self.__leftChild = leftChild

    def setRightChild(self, rightChild):
        self.__rightChild = rightChild

    def plus(self, other):
        return Node(None, self.getCount() + other.getCount())

    def compare(self, other):
        if self.__count > other.__count:
            return 1
        elif self.__count < other.__count:
            return -1
        else:
            return 0

    def hasRealLeft(self):
        if (self.getLeftChild().getCharacter() == None):
            return False
        else:
            return True

    def hasRealRight(self):
        if (self.getRightChild().getCharacter() == None):
            return False
        else:
            return True
