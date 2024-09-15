import numpy as np
import pandas as pd
import sys,os
# เพิ่มเส้นทางของโปรเจคลงใน sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.model_database import read_csv

def CheckInputInDatabase(CowId, CowOld_y, CowOld_m, CowCntUdder):
    # จัดรูปแบบข้อมูลให้เป็น list แทน set
    data_input = [CowId, CowOld_y, CowOld_m, CowCntUdder]
    
    # อ่านข้อมูลจาก CSV
    data_read = read_csv()
    
    # สร้าง DataFrame จากข้อมูลที่อ่านมา
    df = pd.DataFrame(data_read, columns=['CowId', 'CowOld_y', 'CowOld_m', 'CowCntUdder'])
    print(df.head())  # พิมพ์ข้อมูลใน DataFrame
    
    # ตรวจสอบข้อมูลใน DataFrame
    check = check_array_in_columns(df, data_input)
    print(f"Check Result: {check}")  # ดูผลลัพธ์การตรวจสอบ
    return check

def check_array_in_columns(df, array_list):
    # พิมพ์ข้อมูลที่ป้อนและข้อมูลใน DataFrame
    print(f"User Input: {array_list}")
    
    # แปลงข้อมูลใน DataFrame และข้อมูลที่ป้อนเป็น str และแทนที่ค่า NaN ด้วย ''
    df_array = df.fillna('').astype(str).to_numpy()
    array_np = np.array(array_list, dtype=str)
    
    print(f"DataFrame Array: {df_array}")
    print(f"User Input Array: {array_np}")
    
    # ตรวจสอบว่าข้อมูลที่ป้อนเข้ามาตรงกับแถวใน DataFrame หรือไม่
    mask = np.all(df_array == array_np, axis=1)
    return np.any(mask)

    
    
