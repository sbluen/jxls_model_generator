'''
Created on Aug 15, 2015

@author: Steven
'''

import os
import csv

for filename in os.listdir("inputs"):
    if not filename.endswith(".csv"):
        continue
    java_filename = ".".join(filename.split(".")[:-1]) + ".java"