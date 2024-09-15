import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox, QLineEdit

# เพิ่มเส้นทางของโปรเจคลงใน sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Controller.inputChevk import inputCheck
from Controller.CheckInputInDatabase import CheckInputInDatabase
from Controller.CheckType import checktype
from Controller.itCow import totalkmilk

def show_message(title, text, buttons=None, default_button=None):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    if buttons:
        for button_text in buttons:
            button = msg.addButton(button_text, QMessageBox.AcceptRole)
            if button_text == default_button:
                button.setDefault(True)
    msg.exec_()
    return msg

def on_button_click():
    Cowid = input_CowId.text()
    Cowold_y = input_cowold_y.text()
    Cowold_m = input_cowold_m.text()
    Cowudder = input_cowudder.text()
    
    isValid = inputCheck(Cowid, Cowold_y, Cowold_m, Cowudder)
    if isValid:
        checkindbs = CheckInputInDatabase(Cowid, Cowold_y, Cowold_m, Cowudder)
        if checkindbs:
            check = checktype(Cowold_y, Cowold_m, Cowudder)
            if check:
                milk = totalkmilk(Cowid, Cowold_y, Cowold_m, Cowudder)
                show_message("ปริมาณนมรวม", f"ปริมาณนมรวม: {milk} ลิตร.")
            else:
                msg = show_message("เป็นแกะหรือไม่", "ดูเหมือนว่าจะเป็นแกะ ต้องการขับไล่แกะออกไปไหม?", ["ขับไล่แกะ"], "ขับไล่แกะ")
                if msg.clickedButton().text() == "ขับไล่แกะ":
                    click_sheep()
        else:
            show_message("คำเตือน", "กรุณากรอกข้อมูลให้ถูกต้อง!")
    else:
        show_message("ข้อมูลไม่ถูกต้อง", "กรุณากรอกข้อมูลให้ถูกต้อง!")

def click_sheep():
    show_message("เสร็จสิ้น", "การขับไล่แกะเสร็จสมบูรณ์.")

def window():
    global input_CowId, input_cowold_y, input_cowold_m, input_cowudder
    
    app = QApplication(sys.argv)
    main_window = QWidget()
    main_window.setWindowTitle("โปรแกรมจัดการนมวัว")
    main_window.setGeometry(100, 100, 300, 200)

    CowIdlabel = QLabel("กรุณากรอก ID ของวัว:", main_window)
    CowOld_yearlabel = QLabel("กรุณากรอกอายุวัว (ปี):", main_window)
    CowOld_monthlabel = QLabel("กรุณากรอกอายุวัว (เดือน):", main_window)
    CowCountUdderLabel = QLabel("กรุณากรอกจำนวนเต้านมวัว:", main_window)
    
    input_CowId = QLineEdit()
    input_cowold_y = QLineEdit()
    input_cowold_m = QLineEdit()
    input_cowudder = QLineEdit()
    
    button = QPushButton("ตรวจสอบ", main_window)
    button.clicked.connect(on_button_click)

    layout = QVBoxLayout()
    layout.addWidget(CowIdlabel)
    layout.addWidget(input_CowId)
    
    layout.addWidget(CowOld_yearlabel)
    layout.addWidget(input_cowold_y)
    
    layout.addWidget(CowOld_monthlabel)
    layout.addWidget(input_cowold_m)
    
    layout.addWidget(CowCountUdderLabel)
    layout.addWidget(input_cowudder)
    
    layout.addWidget(button)
    main_window.setLayout(layout)
    
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
