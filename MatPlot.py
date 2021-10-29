import string
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Set_ID: string = "90"  # Set your Wanted ID here


class FrameStream:
    def __init__(self):
        self.timeStream = []
        self.bytesStream = []  # array of [8]
        self.constTimestamps = []  # array of [8](start, end) tuples


frames = dict()

data = pd.read_csv("captured_traffic_p.csv")
data = data[data['ID'].str.fullmatch(Set_ID)]
data['ID'] = data['ID'].astype(str)
for index, row in data.iterrows():
    length = int(row['Length'])
    i = 0
    # print(row['ID']) #80
    data.at[index, "Time"] = row["Time"] * 1000 + 200
    while i < length:
        header = "Data" + str(i)
        d = int(row[header], 16)
        data.at[index, header] = d
        i += 1
data.to_csv("Test.csv", index=False)
data = pd.read_csv('Test.csv')

for index, row in data.iterrows():
    id = Set_ID
    try:
        time = int(row['Time'])
    except ValueError:
        print('time incorrect row time:', row['Time'])
        continue
    try:
        i = 0
        bytes = []
        while i < length:
            header = "Data" + str(i)
            d = int(row[header])
            bytes.append(d)
            i += 1
    except ValueError:
        print('byte incorrect row time:', row[header])
        continue
    if not id in frames:
        frames[id] = FrameStream()
    frame = frames[id]
    if len(frame.bytesStream) == 0:
        frame.bytesStream = [[x] for x in bytes]
    else:
        if len(bytes) != len(frame.bytesStream):
            continue
        for b, byte in enumerate(bytes):
            frame.bytesStream[b].append(byte)
    frame.timeStream.append(time)
    assert len(frame.timeStream) == len(frame.bytesStream[0])

for (_, frame) in frames.items():
    for byteStream in frame.bytesStream:
        frame.constTimestamps.append(list())
        print("set bytestream", len(set(byteStream)))
        if len(set(byteStream)) > 10: #noises
            continue  # skip bytes with real numeric data
        timeStart = 0
        for i, b2 in enumerate(zip(byteStream[:-1], byteStream[1:])):
            print(b2[0], b2[1])
            if (b2[0] != b2[1]) or (i == len(byteStream) - 2):
                if timeStart < (i - 10):
                    frame.constTimestamps[-1].append([timeStart, i])
                timeStart = i + 1

# print("const timestamp", frame.constTimestamps)
fig, axs = plt.subplots(2, 1, sharex='all')
#values = list(frames.values())
#plt.xlim(values[0].timeStream[0], values[0].timeStream[-1])

# Create plot diagram
bytesCount = len(frames[id].bytesStream)
x = data.loc[:, "Time"]
i = 0
while i < length:
    header = "Data" + str(i)
    y_axis = "y" + str(i)
    y_axis = data.loc[:, header]
    axs[0].plot(x, y_axis, label=header)
    i += 1

Table_title = data.loc[1, "ID"]

axs[0].set_title(Table_title, size=10)
axs[0].legend()
axs[0].set_xlabel(u'Time (Second)', size=10)
axs[0].set_ylabel(u'Data', size=10)
#axs[0].set_xticks(np.arange(min(x), max(x), 0.2))

# Create bar diagram
axs[1].set_title(Set_ID + ' constant values intervals')
axs[1].yaxis.set_visible(False)
frame = frames[id]
print(frame.constTimestamps)
for b, byteTimestamps in enumerate(frame.constTimestamps):
    if len(byteTimestamps) == 0:
        continue
    axs[1].text(x=1,
                y=b,
                s='b' + str(b),
                va='center',
                color='black',
                fontsize='x-small')
    prevTimeStart = frame.timeStream[byteTimestamps[0][0]]
    for i, timestamp in enumerate(byteTimestamps):
        timeStart = frame.timeStream[timestamp[0]]
        timeEnd = frame.timeStream[timestamp[1]]
        axs[1].barh(y=b,
                    width=timeEnd - timeStart,
                    left=prevTimeStart,
                    color=('yellow' if i % 2 == 0 else 'lime'))
        prevTimeStart = timeEnd
        byteValue = frame.bytesStream[b][timestamp[0]]
        axs[1].text((timeStart + timeEnd) / 2,
                    b,
                    str(byteValue),
                    ha='center',
                    va='center',
                    color='black',
                    fontsize='x-small')
axs[1].legend(fontsize='x-small')

plt.show()
