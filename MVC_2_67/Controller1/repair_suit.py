import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Model'))
from Model.model_database import get_suit_by_id, update_suit_in_csv, Suit
import pandas as pd

#ตัวแปรที่เก็บจำนวนการซ่อมชุดแต่ละประเภท
repair_count = {
    "ชุดทรงพลัง": 0,
    "ชุดลอบเร้น": 0,
    "ชุดปกปิดตัวตน": 0
}

def repair_suit(suit_id):
    #ดึงข้อมูลชุดจากฐานข้อมูล
    suit = Suit
    suit = get_suit_by_id(suit_id)
    
    if not suit:
        return "ไม่พบชุดนี้ในฐานข้อมูล"
    
    #ซ่อมแซมชุด
    new_durability = repair(suit)

    #อัพเดตข้อมูลชุดในฐานข้อมูล
    update_suit_in_csv(suit)
    
    #เพิ่มจำนวนการซ่อมในแต่ละประเภท
    if suit.suit_type in repair_count:
        repair_count[suit.suit_type] += 1

    #แสดงผลการซ่อม
    return f"ชุด {suit.suit_id} ถูกซ่อมแซมแล้ว ความทนทานใหม่: {new_durability}\n" , repair_count
           
#ซ่อมชุด เพิ่มความทนทาน +25 แต่ค่าความทนทานจะไม่เกิน 100
def repair(suit):
        if suit.durability < 100:
            suit.durability = min(suit.durability + 25, 100)
        return suit.durability