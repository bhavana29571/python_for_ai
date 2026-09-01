import os

print("Current working directory:", os.getcwd())# get current working directory

#check if data file exists in the current working directory

data_path="data/sales.csv"
if os.path.exists(data_path):
    print(f"Found {data_path}")
else:
    print(f"Cannot find {data_path}")
    print("Please make sure you are running from the sales-analysis folder.")
