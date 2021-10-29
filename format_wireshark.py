import pandas as pd

df = pd.read_csv('captured_traffic.csv', dtype=str)
df[['one', 'two']] = df.Info.str.split(": ", expand=True, )
df[['ID', 'Data']] = df.two.str.split("  ", expand=True, )
df = df.join(df.pop('Data').str.split(' ', expand=True))
# delete unnecessary column
del df['Info']
del df['one']
del df['two']
del df['Source']
del df['Destination']
del df['Protocol']
df.drop(columns=df.columns[4], axis=1, inplace=True)


df = df.rename(columns={df.columns[4]: 'Data0'})
df = df.rename(columns={df.columns[5]: 'Data1'})
df = df.rename(columns={df.columns[6]: 'Data2'})
df = df.rename(columns={df.columns[7]: 'Data3'})
df = df.rename(columns={df.columns[8]: 'Data4'})
df = df.rename(columns={df.columns[9]: 'Data5'})
df = df.rename(columns={df.columns[10]: 'Data6'})
df = df.rename(columns={df.columns[11]: 'Data7'})

# generate length of each packet
for index, row in df.iterrows():
    i = 0
    count = 0
    id = str(row['ID'])
    id = id.lstrip("0x")
    row['ID'] = id
    while i < 8:
        header = 'Data'+str(i)
        if row[header] is not None:
            count += 1
        i += 1
    row['Length'] = count
df = df.drop(["No."], axis=1)
df = df.iloc[1::2]
df.to_csv('captured_traffic_p.csv')
