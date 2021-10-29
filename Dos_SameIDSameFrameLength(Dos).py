import csv
import random

# 
times: int = 300
Length: int = 4
#
Set_id = 1075


num = random.randrange(0, 255)
Data = str('%#x' % num)[-2:]
num1 = random.randrange(0, 255)
Data1 = str('%#x' % num1)[-2:]
num2 = random.randrange(0, 255)
Data2 = str('%#x' % num2)[-2:]
num3 = random.randrange(0, 255)
Data3 = str('%#x' % num3)[-2:]
num4 = random.randrange(0, 255)
Data4 = str('%#x' % num4)[-2:]
num5 = random.randrange(0, 255)
Data5 = str('%#x' % num5)[-2:]
num6 = random.randrange(0, 255)
Data6 = str('%#x' % num6)[-2:]
num7 = random.randrange(0, 255)
Data7 = str('%#x' % num7)[-2:]

with open('Dos_SameIDSameFrameLength.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    i = 0
    while i < times:
      
        num = random.randrange(0, 255)
        data = str('%#x' % num)[-2:]
        Data = data.replace('x', ' ')

        num1 = random.randrange(0, 255)
        data1 = str('%#x' % num1)[-2:]
        Data1 = data1.replace('x', ' ')

        num2 = random.randrange(0, 255)
        data2 = str('%#x' % num2)[-2:]
        Data2 = data2.replace('x', ' ')

        num3 = random.randrange(0, 255)
        data3 = str('%#x' % num3)[-2:]
        Data3 = data3.replace('x', ' ')

        num4 = random.randrange(0, 255)
        data4 = str('%#x' % num4)[-2:]
        Data4 = data4.replace('x', ' ')

        num5 = random.randrange(0, 255)
        data5 = str('%#x' % num5)[-2:]
        Data5 = data5.replace('x', ' ')

        num6 = random.randrange(0, 255)
        data6 = str('%#x' % num6)[-2:]
        Data6 = data6.replace('x', ' ')

        num7 = random.randrange(0, 255)
        data7 = str('%#x' % num7)[-2:]
        Data7 = data7.replace('x', ' ')


        ID = str(hex(Set_id))[2:]

        if Length == 0:
            writer.writerow([Length, ID, "0"])
        if Length == 1:
            writer.writerow([Length, ID, Data])
        if Length == 2:
            writer.writerow([Length, ID, Data, Data1])
        if Length == 3:
            writer.writerow([Length, ID, Data, Data1, Data2])
        if Length == 4:
            writer.writerow([Length, ID, Data, Data1, Data2, Data3])
        if Length == 5:
            writer.writerow([Length, ID, Data, Data1, Data2, Data3, Data4])
        if Length == 6:
            writer.writerow([Length, ID, Data, Data1, Data2, Data3, Data4, Data5])
        if Length == 7:
            writer.writerow([Length, ID, Data, Data1, Data2, Data3, Data4, Data5, Data6])
        if Length == 8:
            writer.writerow([Length, ID, Data, Data1, Data2, Data3, Data4, Data5, Data6, Data7])
        i += 1