# Group members information

Member 1: Lixue Liang

Member 2: Yuet Lee Chan 

Member 3: Xinruo Zhang

Member 4: Yifei Han




# User Manual 

Generate Attack Packets 

1. To generate Dos attack packets, run ‘python3.8 Dos_SameIDSameFrameLength(Dos).py’. 
2. To generate Fuzzy attack packets, run ‘python3.8 Format_RandomLog_Generator(Fuzzy).py’. 
3. To generate Spoofing attack packets, run ‘python3.8 spoofing.py’ 

Generate Normal CAN Bus traffic on a virtual interface

1. Open a terminal, run ‘python3.8 setup.py’ to set up the SocketCAN interface and ready for sending CAN Bus traffic. Modify the filenames inside the file before use. If there is ‘0x’ before the ID in a normal traffic CSV file, run ‘python3.8 preprocess_traffic.py’ before setting up the normal traffic. 

Generate Attack CAN Bus traffic on a selected virtual interface

1. To generate the attack traffic, open a new terminal(s), run ‘python3.8 attack.py’, and follow the instructions. 

Capture traffic by Wireshark and Format the exported CSV file

1. After running setup.py, before starting any traffic, open a terminal, run ‘sudo wireshark’ to capture packets. The Wireshark must run as administrator, otherwise, the virtual interface won’t show. 
2. Export collected traffic to a CSV file from Wireshark. 
3. Run ‘python3.8 format_wireshark.py’ to format the exported CSV file. Modify the filenames inside the file before use. 
4. Run ‘python3.8 MarkType.py’ to mark the normal traffic and attack traffic. 

Traffic Visualization

1. Run ‘python3.8 MatPlot.py’ to view the plot diagram and bar diagram of the selected CAN ID. 

Data Processing and ID3 Model Training & Testing

1. Run ‘python3.8 ids_data_processing.py’ to convert ID and data fields from hexadecimal to decimal, and combine data fields into one column. 
2. Run ‘ID3_model.ipynb’ to train and test the accuracy of the model. 
