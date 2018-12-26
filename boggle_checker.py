#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 23:51:48 2018

@author: santhoshreddyventeru
"""

from boggle_dices import Boggle_Dice
from inpu_t import Input

words = list()
def Word_checker():
        with open('words.txt', 'r') as file_:
            for x in file_:
                words = file_.read().splitlines()
        words = [wor_d.upper() for wor_d in words]
                         

def word_check(strin_g):
    if strin_g in words:
        return True
    return False
    
def trace_word_grid(word_trace, grid_trace, i, j, strin_g):
    grid_trace[i][j] = True
    strin_g = strin_g + word_trace[i][j]
    print(str(strin_g))
    if word_check(strin_g.upper()):
        print(strin_g.upper())
    
    for row in range(i-1, i+2):
        if row >= len(word_trace):
            break
        for col in range(j-1, j+2):
            if col >= len(word_trace[0]):
                break
            if row>=0 and col>=0:
                if grid_trace[row][col] == False:
                    trace_word_grid(word_trace, grid_trace, row, col, strin_g)
    strin_g = strin_g[:-1]
    grid_trace[i][j] = False
    return

def trace_word(input_word, input_grid):
    for row in range(0, len(input_grid)):
        for col in range(0, len(input_grid)):
            if trace_wordgrid(input_word, row, col, input_grid):
                return True
    return False

def trace_wordgrid(word_trace, row, col, grid_trace):
    """
    This function is the important function that checks the adjacency of the letters recursively.
    
    """
    if word_trace == '':
        return True
    elif row<0 or row>=4 or col<0 or col>=4 or word_trace[:1] != grid_trace[row][col]:
        return False
    else:
        exist = grid_trace[row][col]
        grid_trace[row][col] = ''
        remaining = word_trace[1:len(word_trace)]
        result = trace_wordgrid(remaining, row-1, col-1, grid_trace) or trace_wordgrid(remaining, row-1, col, grid_trace)   or trace_wordgrid(remaining, row-1, col+1, grid_trace) or trace_wordgrid(remaining, row, col-1, grid_trace)  or trace_wordgrid(remaining, row, col+1, grid_trace)  or trace_wordgrid(remaining, row+1, col-1, grid_trace) or trace_wordgrid(remaining, row+1, col, grid_trace)   or trace_wordgrid(remaining, row+1, col+1, grid_trace) 
            
        grid_trace[row][col] = exist
        return result
    
    
class Boggle_checker:

    def display(self):
        self.sixteendices = Boggle_Dice()
        self.sixteendices.display_dices()
        print('Start typing your words!(press enter after each word and enter "X" when done)' )  

    def _input(self):
        self.player_input = Input()
        while True:
            input_word = input()
            if str(input_word).upper() == 'X':
                break
            else:
                self.player_input.add_to_input(input_word)

    def scor_e(self):
        points = 0
        matri_x = self.dices.letterboard()
        player_in = self.player_input.getlist()
        #length_word = len(player_in)
        for j in range(0, len(player_in)):
            if trace_word(player_in[j], matri_x):
                    if len(player_in[j])<3:
                        print('The word ', player_in[j], 'is short.')
                        pass
                    if len(player_in[j]) == 3 or len(player_in[j]) == 4:
                        print('The word ', player_in[j], 'is worth 1 point')
                        points += 1
                    if len(player_in[j]) == 5:
                        print('The word ', player_in[j], 'is worth 2 point')
                        points += 2
                    if len(player_in[j]) == 6:
                        print('The word ', player_in[j], 'is worth 3 point')
                        points += 3
                    if len(player_in[j]) == 7:
                        print('The word ', player_in[j], 'is worth 5 point')
                        points += 5
                    if len(player_in[j]) >= 8:
                        print('The word ', player_in[j], 'is worth 11 point')
                        points += 11
    
            else:
                print('The word ', player_in[j], 
                      'is not present in the grid.')
        self.score = points
        print('Your total score is ', points, 'points')
                
    
    def setSixteenDices(self, _dices):
        self.dices = _dices
    
    def setInputProcessor(self, input_processor):
        self.player_input = input_processor
    
    def getScore(self):
        return self.score