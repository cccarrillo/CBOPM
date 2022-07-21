# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 10:44:59 2022

@author: Xadmin
"""
import pandas as pd
import math
import os

## trying to make an oyster grown from day 0 to day 365.
shell_length= 1.5
sex= 1
dry_biomass= 25
wet_biomass= 40
age = 1
        
class Oyster:
    #list all oyster attributes 
    
    def __init__(self):
        self.sex = 1
        self.age = 5
        self.shell_length = 13
        self.dry_biomass = 25
        self.wet_biomass = 30
        self.fecundity = 3
        self.environmental_effects = 0.52
        self.rde = 0.6
        self.k = 0.5
        print(vars(self))


##Initializing variables

    def growth(self):
        dry_biomass = ((9.6318e-06)*self.shell_length**2.743)
        wet_biomass = (dry_biomass*5.6667) + dry_biomass
        
        
        self.shell_length = self.shell_length + 0.01
        print('new shell length: {}'.format(self.shell_length))
        
        print('dry biomass: {}'.format(dry_biomass))
        print('wet biomass: {}'.format(wet_biomass))
        
        
        
        return self.shell_length
    
    def reproduce(self):
        fecundity_age = self.rde *  self.k
        fecundity_adjusted = self.environmental_effects * fecundity_age
        total_fecundity = self.fecundity * fecundity_adjusted 
        
        print('fecundity age: {}'.format(fecundity_age))
        print('fecundity adjusted: {}'.format(fecundity_adjusted))
        print('total fecundity: {}'.format(total_fecundity))





test = Oyster()
print(test.growth())
print(test.reproduce())

    
    
