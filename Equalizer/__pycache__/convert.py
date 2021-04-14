import pandas as pd
read_file = pd.read_csv (r'E:\Marriam\Signal-Viewer\Data\\SampleEOG_Blinking_converted.txt')
read_file.to_csv (r'E:\Marriam\Signal-Viewer\Data\\EOG.csv', index=None)