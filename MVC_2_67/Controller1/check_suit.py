import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Model'))
from Model.model_database import get_suit_by_id, Suit

def check_suit(suit_id):
    suit = Suit
    suit = get_suit_by_id(suit_id)
    if not suit:
        return "ไม่พบชุดนี้ในฐานข้อมูล", False 
    valid = is_valid(suit)
    if valid:
        return f"ชุด {suit.suit_id} อยู่ในสภาพดีแล้ว ความทนทาน: {suit.durability}", False #ไม่ต้องซ่อม
    else:
        return f"ชุด {suit.suit_id} ต้องการซ่อมแซม ความทนทาน: {suit.durability}", True #ต้องซ่อมชุด ความทนทานไม่ถึงเกณฑ์


    #ตรวจสอบสภาพชุด
def is_valid(suit):
    if suit.suit_type == "ชุดทรงพลัง" and suit.durability < 70:
        return False
    elif suit.suit_type == "ชุดลอบเร้น" and suit.durability < 50:
        return False
    elif suit.suit_type == "ชุดปกปิดตัวตน" and (str(suit.durability).endswith("3") or str(suit.durability).endswith("7")):
        return False
    return True