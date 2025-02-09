import pandas as pd
import csv
csv_file = 'superhero_suits.csv' #ฐานข้อมูล

#สร้างคลาสเพื่อทำเป็น object
class Suit:
    def __init__(self, suit_id, suit_type, durability):
        self.suit_id = suit_id
        self.suit_type = suit_type
        self.durability = durability

#ดึงข้อมูลชุดจากฐานข้อมูล
def get_suit_by_id(suit_id):
    df = pd.read_csv(csv_file)
    suit_row = df[df['รหัสชุด'] == int(suit_id)]
    
    if suit_row.empty:
        return None  #ไม่พบชุดในฐานข้อมูล

    suit_id = str(suit_row.iloc[0]['รหัสชุด'])
    suit_type = suit_row.iloc[0]['ประเภทของชุด']
    durability = suit_row.iloc[0]['ระดับความทนทาน']
    
    return Suit(suit_id, suit_type, durability) #ส่งไปเป็น object

#อัพเดตข้อมูลชุดในฐานข้อมูล
def update_suit_in_csv(suit):
    df = pd.read_csv('superhero_suits.csv')
    df.loc[df['รหัสชุด'] == int(suit.suit_id), 'ระดับความทนทาน'] = suit.durability
    df.to_csv(csv_file, index=False)
