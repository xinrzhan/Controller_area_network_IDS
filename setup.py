import os
import can
import pandas as pd


def import_normal_data(file, bus):
    df = pd.read_csv(file)
    try:
        for index, row in df.iterrows():
            # string of ID
            '''id = row['ID']
            if id[0] == '0':
                id = id.lstrip("0")
            id = '0x'+ id'''
            id = row['ID']
            arbitration_id = int(id, base=16)
            length = int(row['Length'])
            i = 0
            j = 9
            csv_data = []
            while i < length:
                d = int(str(row[j]), base=16)
                csv_data.append(d)
                j += 1
                i += 1
            data = csv_data
            msg = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=False)
            bus.send(msg)
            print(str(arbitration_id) + " " + str(data))
            print("Message sent on {}".format(bus.channel_info))
    except can.CanError:
        print("Message NOT sent")


if __name__ == "__main__":
    os.system("sudo modprobe vcan")
    os.system("sudo ip link add dev vcan0 type vcan")
    os.system("sudo ip link set vcan0 up")
    print("Setting up vcan0 ")
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    print("channel = vcan0 | bustype = socketcan ")
    #file = input("Import Normal Traffic CSV File: ")
    file = 'normal.csv'
    a = input("Press any key to start")
    import_normal_data(file, bus)
