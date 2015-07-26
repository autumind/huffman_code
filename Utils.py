#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2015

@author: shenzb
'''
from Node import Node

def stringToPriorityQueue(text):
    '''
    Transfer every character of a string to priority queue.
    Priority order is according to character's count of the string.
    '''
    chars = list(text)
    char_dict = dict([(c, 0) for c in chars])

    for char in chars:
        char_dict[char] = char_dict[char] + 1

    ''' Get a priority queue list. '''
    char_list = sorted(char_dict.items(), lambda x, y: cmp(x[1], y[1]))

    return char_list

def generateHuffmanTree(nodeList):
    '''
    Generate a Huffman Tree from a Priority Queue.
    '''
    nodeNew = nodeList[0].plus(nodeList[1])
    nodeNew.setLeftChild(nodeList[0])
    nodeNew.setRightChild(nodeList[1])

    nodeList.append(nodeNew)
    nodeList.pop(0)
    nodeList.pop(0)

    nodeList.sort(Node.compare)

    if len(nodeList) == 1:
        return nodeList[0]
    return generateHuffmanTree(nodeList);

def generateHuffmanCodes(huffmanTree):
    '''
    Generate Huffman codes from a Huffman Tree.
    '''
    huffmanCodes = dict[]
    leftTree = huffmanTree.getLeftChild()
    rightTree = huffmanTree.getRightChild()
    if leftTree.hasRealLeft():
        pass
    elif leftTree.hasRealRight():
        pass
    else
        return huffmanCodes
        
