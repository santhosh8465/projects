#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 22:59:42 2018

@author: santhoshreddyventeru
"""

import sys
class Input:
    def __init__(self, ):
        self.lis = list()
        #self.input = string()
        #self.input = dictionary()
        
    def add_to_input(self, in_val):
        try:
            self.lis.append(str(in_val).upper())
        except TypeError:
            print("error")
            sys.exit(1)
            
            
    def getlist(self):  
        print(self.lis)
        #print(self.Input)
        return self.lis
        #print(x)    
    def setlist(self, input_list):
        self.lis = input_list
        
        
    def set_input_list(self, input_list):
        self.__input_list = input_list

