# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:46:02 2019

@author: c_mob
"""

import re

def histogram(s):
    d = dict()
    for sentence in s:
        words = sentence.split()
        for word in words:            
            w = word.lower()               # make lowercase
            w = re.sub(r'\W+', '', w)     # remove all the punctuation with a regular expression substituion
            for c in w:
                if c not in d:
                    d[c] = 1
                else:
                    d[c] += 1
    return d

if __name__ == '__main__':    
    filehandle = open('emma.txt',encoding='utf-8')
    all_lines = filehandle.readlines()
    d = histogram(all_lines)
    for c in d:
        print (c,d[c])
        