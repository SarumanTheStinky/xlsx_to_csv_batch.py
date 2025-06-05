import os
import pandas as pd

directory = os.path.dirname(__file__)
files = [file for file in os.listdir(directory)]

for file in files:
    if file.endswith(".xlsx"):
        try:
            file_path = os.path.join(directory, file)
            csv_filename = os.path.splitext(file)[0] + ".csv"
            csv_path = os.path.join(directory, csv_filename)
            pd.read_excel(file_path).to_csv(csv_path, index=False, header=True)
        except Exception as e:
            print(e)
            print("Error with file:", file)
