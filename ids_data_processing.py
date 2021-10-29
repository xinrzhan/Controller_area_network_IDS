import pandas as pd


df = pd.read_csv('demo_dfs.csv', dtype=str)
cols = [0,1,2,3,4]
df.drop(df.columns[cols],axis=1,inplace=True)
# Convert ID to Decimal
count = 0
for index, row in df.iterrows():
    id = str(row['ID'])
    row['ID'] = int(id, 16)
    i = 0
    while i < 8:
        header = 'Data' + str(i)
        try:
            row[header] = int(str(row[header]),16)
        except:
            pass
        i += 1
    count += 1
    print(count)

df['DataField'] = ''

for index, row in df.iterrows():
    i = 0
    count = 0
    data = []
    while i < 8:
        header = 'Data' + str(i)
        try:
            data.append(row[header])
        except:
            pass
        i += 1
    row['DataField'] = ''.join(map(str,data))
    row['DataField'] = row['DataField'].replace("a", "")
    row['DataField'] = row['DataField'].replace("n", "")
    count += 1

del df['Data0']
del df['Data1']
del df['Data2']
del df['Data3']
del df['Data4']
del df['Data5']
del df['Data6']
del df['Data7']

df.to_csv('final_demo.csv')
