import csv
import pandas as pd
import random

def write_csv(data):
    file_path = 'database.csv'
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"write to {'file_path'} success")
    except Exception as e:
        print(f"errer to write : {e}")


def read_csv():
    file_path = 'database.csv'
    data = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data
    except Exception as e:
        print(f"error to read: {e}")
        return []

def update_csv(cow_id,x):
    df = pd.read_csv()
    file_path = 'database.csv'
  
    if cow_id in df['CowID'].values:
        df.loc[df['CowID'] == cow_id, 'UdderCount'] = df.loc[df['CowID'] == cow_id, 'UdderCount'].apply(x)
    
    df.to_csv(file_path, index=False)

