#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 23:32:22 2018

@author: santhoshreddyventeru
"""
import random
class Boggle_Dice:
    
    def __init__(self):
        self.dic_es = { 1  : ['A', 'E', 'A', 'N', 'E', 'G'],  2  : ['A', 'H', 'S', 'P', 'C', 'O'],
                       3  : ['A', 'S', 'P', 'F', 'F', 'K'],  4  : ['O', 'B', 'J', 'O', 'A', 'B'],
                       5  : ['I', 'O', 'T', 'M', 'U', 'C'],  6  : ['R', 'Y', 'V', 'D', 'E', 'L'],
                       7  : ['L', 'R', 'E', 'I', 'X', 'D'],  8  : ['E', 'I', 'U', 'N', 'E', 'S'],
                       9  : ['W', 'N', 'G', 'E', 'E', 'H'],  10 : ['L', 'N', 'H', 'N', 'R', 'Z'],
                       11 : ['T', 'S', 'T', 'I', 'Y', 'D'],  12 : ['O', 'W', 'T', 'O', 'A', 'T'],
                       13 : ['E', 'R', 'T', 'T', 'Y', 'L'],  14 : ['T', 'O', 'E', 'S', 'S', 'I'],
                       15 : ['T', 'E', 'R', 'W', 'H', 'V'],  16 : ['N', 'U', 'I', 'H', 'M', 'Qu'],}
        self.board = [[]]
        self.dice_s()
        
    def dice_s(self):
        important = []
        for val in self.dic_es.keys():
            value = self.dic_es[val][random.randint(0, 5)]
            print('[', value, ']', sep = " ", 
                 end = "" if (val%4) != 0 else '\n')
            important.append(value)
            if val%4 == 0:
                self.board.append(important)
                important = []
        self.board = self.board[1:]
    
    def letterboard(self):
        return self.board
    
    
    
    
    
    