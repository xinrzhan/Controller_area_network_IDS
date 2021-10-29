# This file compare between normal traffic and traffic with attack
# Normal will be marked 0, attack will be marked 1
import pandas as pd
import numpy as np

combine_df = pd.read_csv('demo_df.csv', dtype=str)
attack_df = pd.read_csv('spoof_only_p.csv', dtype=str)

combine_df['Attack'] = '0'
count = 0

#'''
for index, row in combine_df.iterrows():

    for index2, row2 in attack_df.iterrows():
        if str(row['ID']) == str(row2['ID']) \
                and str(row['Data0']) == str(row2['Data0']) \
                and str(row['Data1']) == str(row2['Data1']) \
                and str(row['Data2']) == str(row2['Data2']) \
                and str(row['Data3']) == str(row2['Data3']) \
                and str(row['Data4']) == str(row2['Data4']) \
                and str(row['Data5']) == str(row2['Data5']) \
                and str(row['Data6']) == str(row2['Data6']) \
                and str(row['Data7']) == str(row2['Data7']):
            row['Attack'] = '1'
            print(count, " " , row['ID'])
            attack_df.drop(index2, inplace=True)
            count += 1
    print(row[0])
'''


for index, row in combine_df.iterrows():

    if str(row['ID']) == str('4d2'):
        row['Attack'] = '1'
        print(count, " ", row['ID'])
        count += 1
    print(row[0])
'''
combine_df.to_csv('demo_dfs.csv')
