#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:11:49 2019

@author: sashaepelbaum
"""


#.data - where you will hold your data
#.length - that tells you the length of your data list
#.mean
#.median
#.variance
#.stand_dev
import math

class Calculator:
    def __init__(self, data):
        self.data = sorted(data) ###???? is it simply user input? do we need to print?
        self. __calc_stats__()
        #self.length = self.__calc_length__() 
        #self.mean = self.__calc_mean__()
        #self.median = self.__calc_median__()
        #self.variance = self.__calc_variance__()
        #self.stand_dev = self.__calc_stand_dev__()
    
    #def __data__(self): 
        #return sorted(self.data) #.sort()
    
    def __calc_length__(self):
        return len(self.data)
    
    def __calc_mean__(self):
        mean = sum(self.data)/len(self.data)
        return mean
    
    def __calc_median__(self):
        
        n = self.length
        if n % 2 :
            return self.data[n // 2]
        else:
            return (self.data[n // 2] + self.data[(n // 2) - 1])/2
        
    def __calc_variance__(self):
        sample_mean = self.mean
        diffs_sqrd = []
        
        for i in self.data:
            diff_sqrd = (i - sample_mean)**2
            diffs_sqrd.append(diff_sqrd)
    
        variance = sum(diffs_sqrd)/(self.length-1)
    
        return variance
        
    def __calc_stand_dev__(self):
        return math.sqrt(self.variance)
        
    def __calc_stats__(self):
        self.length = self.__calc_length__() 
        self.mean = self.__calc_mean__()
        self.median = self.__calc_median__()
        self.variance = self.__calc_variance__()
        self.stand_dev = self.__calc_stand_dev__()
 #.add_data() - which can take in a value or a list of values and extend the .data attribute
#.remove_data() accept a list of numbers and remove any of the numbers in that list from your object data   
    def add_data(self, new_data):
        self.data.extend(new_data) #add data to existing list
        return __calc_stats__()
    
    def remove_data(self, data_to_r):
        for datum in data_to_r:
            data = self.remove(element)       
        return __init__(self, data)
    
#data = [1,2,3]
#calc = Calculator(data)

#print(calc.mean)