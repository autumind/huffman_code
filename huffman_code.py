#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2015

@author: shenzb
'''
from Node import Node 
import Utils

if __name__ == '__main__':

    char_list = Utils.stringToPriorityQueue("hello, world!")
    #print(char_list);

    ''' Initialize PriorityQueue '''
    nodeList = []
    for ch, cnt in char_list:
        #print(ch, cnt)
        node = Node(ch, cnt)
        nodeList.append(node)

    '''
    Get a Huffman tree.
    '''
    huffmanTree = Utils.generateHuffmanTree(nodeList)

    '''
    Get Huffman codes.
    '''
    huffmanCode = Utils.generateHuffmanCodes(huffmanTree)
