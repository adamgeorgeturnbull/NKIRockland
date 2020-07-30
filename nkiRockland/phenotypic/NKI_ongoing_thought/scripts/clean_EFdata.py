# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pandas as pd
from scipy.stats import zscore
import numpy as np

path = '/Users/adamturnbull/GitHub/NKIRockland/nkiRockland/phenotypic/assessment_data/'
file = '8100_Penn_CNP_(12-18-13)_20200624.csv'
fileloc = path + file

df = pd.read_csv(fileloc)
df = df.iloc[1:]
df['Visit'] = df['Visit'].replace(['V1', 'V2'], 'VA')
df = df.drop_duplicates(subset='Anonymized ID', keep='first')
