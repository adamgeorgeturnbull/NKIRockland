#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:09:37 2020

@author: aturnbull1
"""

import pandas as pd
import numpy as np

path = '/Users/aturnbull1/Desktop/NKIRockland/nkiRockland/phenotypic/NKI_ongoing_thought/data/'
file = 'thought_data_plus_PENN_comp.csv'
fileloc = path + file

first = 'PCET_PCET_ACC'
df = pd.read_csv(fileloc)
x = df.columns.get_loc(first)
PENN_cols = df.columns[x:]
PENN = df[PENN_cols]
PENN = PENN.replace(r'^\s*$', np.NaN, regex=True)
PENN = PENN.astype(str).astype(float)
PENN = PENN.dropna()
med = PENN.median()
Q1 = PENN.quantile(0.25)
Q3 = PENN.quantile(0.75)
IQR = Q3-Q1
outliers = (PENN - med).abs() > 3*IQR
n_outliers = outliers.sum()
PENN[outliers] = np.nan
PENN.fillna(med, inplace=True)
df[PENN_cols] = PENN

n_outliers.to_csv(path+'outlier_counts.csv')
df.to_csv(path+'PENN_clean_data_no_outliers.csv')