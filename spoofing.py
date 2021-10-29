import csv
import os
import random
import re

import pandas as pd



filepath = "E:/University/SPRING 2021/PROJECT/mazda2006_1"
input_len = int(input('input len:'))
global csv_df
pd.set_option('max_columns', None)
pd.set_option('max_rows', None)
files = os.listdir(filepath)
files_dec = list(filter(lambda f: f.endswith('DEC.csv'), files))
head, tail = os.path.split(filepath)
filepath_byte = head + '/' +tail + ''
obdrequest = r'^.*7DF.*$'
obdrespond = r'^.*7E8.*$'

for file in files_dec:
    csv_filepath = filepath + '/' +file
    csv_data = pd.read_csv(csv_filepath)
    len_payload = csv_data.Length[0]
    len_trace = len(csv_data)
    slog_ID = file.split('_')[-2]
    if re.search(obdrespond, slog_ID) or re.search(obdrequest, slog_ID):
        print("OBD diagnostic trace file.")
    else:
        print("New input file: " + str(file))

        data = pd.read_csv(file)
        maximum_len = data.iloc[:, 7].max()
        minimum_len = data.iloc[:, 7].min()
        value_len = maximum_len = minimum_len
        print("length is " + str(value_len))

        value_ls = []
        for _ in range(input_len):
            value_list = []
            i = 8
            o = 8 + value_len
            while i < o:
                pos = i-8
                maximum = data.iloc[:,i].max()
                minimum = data.iloc[:,i].min()
                if maximum != minimum:
                    value = random.randrange(minimum, maximum)
                    print("data " + str(pos)  + " is " + str(value))
                    value_list.append(value)
                else:
                    value = maximum = minimum
                    print("data " + str(pos) + " is " + str(value))
                    value_list.append(value)

                i = i+1
            value_ls.append(value_list)

            time_interval = []
            first_column = data.iloc[1:, 1]
            last_column = data.iloc[:-1, 1]
            value = first_column.reset_index(drop=True) - last_column

            time_interval_canID = pd.DataFrame({
                'time_intervals': value
            })

            list_of_name = time_interval_canID['time_intervals'].to_list()
            round_list_of_name = [round(num, 2) for num in list_of_name]
            average = sum(round_list_of_name) / len(round_list_of_name)
            average /= 1000.0
            print(average)


        filename = str(slog_ID) + '.csv'
        f = open(filename, 'w', newline='')
        writer = csv.writer(f)
        writer.writerow(["ID", "Length", "Time_Interval", "Data0", "Data1", "Data2", "Data3", "Data4", "Data5", "Data6", "Data7"])
        for v in value_ls:
            writer.writerow([slog_ID, value_len, average] + v)
        f.close()













