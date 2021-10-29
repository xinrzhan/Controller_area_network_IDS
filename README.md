# Group members information

Member 1: Lixue Liang

Member 2: Yuet Lee Chan 

Member 3: Xinruo Zhang

Member 4: Yifei Han

User Manual 

Generate Attack Packets 
To generate Dos attack packets, run ‘python3.8 Dos_SameIDSameFrameLength(Dos).py’. 
To generate Fuzzy attack packets, run ‘python3.8 Format_RandomLog_Generator(Fuzzy).py’. 
To generate Spoofing attack packets, run ‘python3.8 spoofing.py’ 

Generate Normal CAN Bus traffic on a virtual interface
Open a terminal, run ‘python3.8 setup.py’ to set up the SocketCAN interface and ready for sending CAN Bus traffic. Modify the filenames inside the file before use. If there is ‘0x’ before the ID in a normal traffic CSV file, run ‘python3.8 preprocess_traffic.py’ before setting up the normal traffic. 

Generate Attack CAN Bus traffic on a selected virtual interface
To generate the attack traffic, open a new terminal(s), run ‘python3.8 attack.py’, and follow the instructions. 

Capture traffic by Wireshark and Format the exported CSV file
After running setup.py, before starting any traffic, open a terminal, run ‘sudo wireshark’ to capture packets. The Wireshark must run as administrator, otherwise, the virtual interface won’t show. 
Export collected traffic to a CSV file from Wireshark. 
Run ‘python3.8 format_wireshark.py’ to format the exported CSV file. Modify the filenames inside the file before use. 
Run ‘python3.8 MarkType.py’ to mark the normal traffic and attack traffic. 

Check outliers
After generating each dataset that includes normal and attack labels, run ‘outlier.R’ to detect whether each packet has outliers.
The core idea of detection is outliers (data point), which is significantly different from other data. 
There are too many methods to check the outliers, but we use Rosner’s Test that is used to detect several outliers at once. 
Rosner’s Test is based on Boxplot, it can identify potential outliers by displaying five common locations
Finally, outliers are marked as 1, and normal data are marked as 0.

Traffic Visualization
Run ‘python3.8 MatPlot.py’ to view the plot diagram and bar diagram of the selected CAN ID. 

Data Processing and ID3 Model Training & Testing
Run ‘python3.8 ids_data_processing.py’ to convert ID and data fields from hexadecimal to decimal, and combine data fields into one column. 
Run ‘ID3_model.ipynb’ to train and test the accuracy of the model. 
