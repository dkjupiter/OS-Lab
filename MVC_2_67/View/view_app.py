import sys
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication

# เพิ่มเส้นทางไปยังโฟลเดอร์ Controller
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Controller1'))

#นำเข้าฟังก์ชั่น check_suit และ repair_suit จากไฟล์ในโฟลเดอร์ Controller
#ใช้ Controller1 เพราะ Controller อันเดิมพัง ไม่สามารถลบได้ภายในเวลา
from Controller1.check_suit import check_suit
from Controller1.repair_suit import repair_suit

#UIหน้าจอ
def valid_suit_ui():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("ตรวจสอบความทนทานของชุด")
    window.setGeometry(100, 100, 400, 300)

    layout = QVBoxLayout()

    #ใส่รหัสชุดที่จะตรวจสอบ
    label = QLabel("ป้อนรหัสชุด:")
    layout.addWidget(label)

    entry = QLineEdit(window)
    layout.addWidget(entry)

    #ปุ่มตรวจความทนทาน เพื่อจะดูว่ามีความทนทานเท่าไหร่
    check_button = QPushButton("ตรวจสอบ", window)
    layout.addWidget(check_button)

    #ปุ่มที่คลิกเพื่อซ่อมแซมชุด
    repair_button = QPushButton("ซ่อมแซมชุด", window)
    repair_button.setVisible(False)
    layout.addWidget(repair_button)

    #แสดงจำนวนครั้งการซ่อมชุดแต่ละประเภท
    repair_summary_label = QLabel("จำนวนชุดที่ซ่อมแซมในแต่ละประเภท:")
    layout.addWidget(repair_summary_label)

    #ไว้อัพเดตจำนวนการซ่อมุด
    def update_repair_summary(repair_count):
        repair_summary = "\n".join([f"{key}: {value}" for key, value in repair_count.items()])
        repair_summary_label.setText(f"จำนวนชุดที่ซ่อมแซมในแต่ละประเภท:\n{repair_summary}")

    #ไว้ตรวจสอบว่ามีชุดนั้นในฐานข้อมูลไหม
    def handle_check():
        """ ฟังก์ชั่นที่ใช้ตรวจสอบชุด """
        suit_id = entry.text()
        result, repair_needed = check_suit(suit_id)  #เรียกใช้ฟังก์ชั่น check_suit ของ controller
        QMessageBox.information(window, "ผลลัพธ์", result)
        if repair_needed:
            repair_button.setVisible(True)
        else:
            repair_button.setVisible(False)

    #คลิกปุ่มซ่อมชุด ไปเพิ่มความทนทานของชุด 
    def handle_repair():
        suit_id = entry.text()
        result, repair_count = repair_suit(suit_id)  # เรียกใช้ฟังก์ชั่น repair_suit ของ controller 
        QMessageBox.information(window, "การซ่อมแซม", result)
        repair_button.setVisible(False)
        
        # อัพเดตจำนวนการซ่อมชุด
        update_repair_summary(repair_count)

    check_button.clicked.connect(handle_check)
    repair_button.clicked.connect(handle_repair)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())
