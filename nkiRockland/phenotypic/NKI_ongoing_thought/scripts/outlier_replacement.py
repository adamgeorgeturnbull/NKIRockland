#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:09:37 2020

@author: aturnbull1
"""

import pandas as pd
from scipy.stats import zscore

path = '/Users/aturnbull1/Desktop/NKIRockland/nkiRockland/phenotypic/NKI_ongoing_thought/data/'
file = 'thought_data_first_timepoint_plus_PENN.csv'
fileloc = path + file

first = 'PCET_PCET_ACC'
