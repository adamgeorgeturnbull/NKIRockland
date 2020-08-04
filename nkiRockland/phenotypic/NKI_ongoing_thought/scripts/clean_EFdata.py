# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from scipy.stats import zscore

path = '/Users/aturnbull1/Desktop/NKIRockland/nkiRockland/phenotypic/assessment_data/'
file = '8100_Penn_CNP_(12-18-13)_20200624.csv'
fileloc = path + file

EF = ['PCET_PCET_ACC','PCET_PCETRTCR','SPCPTNL_SCPT_TP','SPCPTNL_SCPT_TPRT','SLNB2_SLNB_MCR','SLNB2_SLNB_MRTC']
EM = ['KCPW_KIWRD_TOT','KCPW_KIWRD_RTC','CPF_IFAC_TOT','CPF_IFAC_RTC','SHORTVOLT_SVT','SHORTVOLT_SVTCRT']
CC = ['KSPVRTC_K_SPVRT_C_CR','KSPVRTC_K_SPVRT_C_RTCR']
SC = ['ER40D_ER40_CR','ER40D_ER40_CRT','MEDF36_MEDF36_NS_CR','MEDF36_MEDF36_NS_RTCR']
allscores = EF + EM + CC + SC
columns = ['Anonymized ID', 'Subject Type', 'Sub Study Label', 'Visit'] + allscores

df = pd.read_csv(fileloc)
df = df.iloc[1:]
df['Visit'] = df['Visit'].replace(['V1', 'V2'], 'VA')
df = df.drop_duplicates(subset='Anonymized ID', keep='first')
df = df[columns]
df = df.dropna()
numeric_cols = df.columns[4:]
df[numeric_cols] = df[numeric_cols].astype(str).astype(float)
zdf = df[numeric_cols].apply(zscore)
zdf.columns = [str(col) + '_z' for col in zdf.columns]
zdf[zdf.columns[1::2]] = zdf[zdf.columns[1::2]]*-1
effdf = zdf.groupby(list(zdf.columns.str[:4]),axis=1).sum()
effdf.columns = [str(col) + '_eff' for col in effdf.columns]
zeffdf = effdf.apply(zscore)
zeffdf.columns = [str(col) + '_z' for col in zeffdf.columns]

final = pd.concat([df,zdf,effdf,zeffdf], axis=1)
final.to_csv(path + 'PENN_data_clean.csv')