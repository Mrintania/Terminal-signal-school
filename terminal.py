import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk, messagebox,Radiobutton,PhotoImage
from PIL import ImageTk, Image

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("Terminal for Radio Signal School")
root.geometry('')
root.resizable(True, True)

# # อ่าน COM Port ที่เชื่อมต่ออยู่
com_list = []
for com in serial.tools.list_ports.comports():
    com_list.append(com.device)
if not com_list:
    # แสดง message box เมื่อไม่พบ COM Port เชื่อมต่ออยู่
    messagebox.showwarning("Warning", "No COM Ports found!")

# สร้าง Dropdown สำหรับเลือก COM Port
com_label = ttk.Label(root, text="Select COM Port:")
com_label.pack(pady=10)

com_var = tk.StringVar()
com_dropdown = ttk.Combobox(root, textvariable=com_var, values=com_list, justify="center", state="readonly")
com_dropdown.current(0) # ตั้งค่าให้เลือก COM Port ตัวแรกใน list เป็นค่า default
com_dropdown.pack(pady=5)

# สร้าง Label สำหรับแสดงสถานะการเชื่อมต่อ
status_var = tk.StringVar()
status_label = ttk.Label(root, textvariable=status_var)
status_label.pack(side="bottom", pady=5)

# # สร้างฟังก์ชันเชื่อมต่อ Serial port
# def connect():
#     #ตัวอย่างการเชื่อมต่อ
#     global ser
#     ser = serial.Serial(com_var.get())
#     print("Connected")
#     # แก้ไขสถานะในส่วนของ status menu
#     status_label.config(text="Connected", foreground="green")
#     # แก้ไขปุ่ม Connect เป็น Disconnect
#     connect_button.config(text="Disconnect", command=disconnect)

# def disconnect():
#     # ตัวอย่างการยกเลิกการเชื่อมต่อ
#     global ser
#     print("Disconnected")
#     # แก้ไขสถานะในส่วนของ status menu
#     status_label.config(text="Disconnected", foreground="red")
#     # แก้ไขปุ่ม Disconnect เป็น Connect
#     connect_button.config(text="Connect", command=connect)

# # สร้างปุ่ม Connect
# connect_button = ttk.Button(root, text="Connect", command=connect)
# connect_button.pack(pady=10)

# # สร้างสถานะในส่วนของ status menu
# status_label = ttk.Label(root, text="Disconnected", foreground="red", justify="center")
# status_label.pack(side="bottom", fill="x")

# สร้าง Radio button สำหรับเลือก Baud rate
baud_frame = ttk.LabelFrame(root, text="Baud rate")
baud_frame.pack(pady=10)

baud_var = tk.StringVar()
baud_radios = [
ttk.Radiobutton(baud_frame, text=baud_rate, variable=baud_var, value=baud_rate)
for baud_rate in [9600, 19200, 38400, 57600, 115200]
]
baud_var.set(9600) # ตั้งค่าให้เลือก Baud rate 9600 เป็นค่า default
for radio in baud_radios:
    radio.pack(side="left", padx=5)

# สร้าง Data Bit สำหรับเลือก Data bit
databit_frame = ttk.LabelFrame(root, text="Data bit")
databit_frame.pack(pady=10)

databit_var = tk.StringVar()
databit_rb_8 = ttk.Radiobutton(databit_frame, text="8 bits", variable=databit_var, value="8")
databit_rb_8.pack(side="left", padx=5)

databit_rb_7 = ttk.Radiobutton(databit_frame, text="7 bits", variable=databit_var, value="7")
databit_rb_7.pack(side="left", padx=5)

databit_rb_6 = ttk.Radiobutton(databit_frame, text="6 bits", variable=databit_var, value="6")
databit_rb_6.pack(side="left", padx=5)

databit_rb_5 = ttk.Radiobutton(databit_frame, text="5 bits", variable=databit_var, value="5")
databit_rb_5.pack(side="left", padx=5)

databit_var.set("8") # ตั้งค่าให้เลือก Data bit 8 เป็นค่า default


# สร้าง Stop Bit สำหรับเลือก Stop bit
stopbit_frame = ttk.LabelFrame(root, text="Stop bit")
stopbit_frame.pack(pady=10)

stopbit_frame_inner = ttk.Frame(stopbit_frame)
stopbit_frame_inner.pack()
stopbit_var = tk.StringVar()
stopbit_1_radio = ttk.Radiobutton(stopbit_frame_inner, text="1", variable=stopbit_var, value="1")
stopbit_1_radio.pack(side="left", padx=5)
stopbit_15_radio = ttk.Radiobutton(stopbit_frame_inner, text="1.5", variable=stopbit_var, value="1.5")
stopbit_15_radio.pack(side="left", padx=5)
stopbit_2_radio = ttk.Radiobutton(stopbit_frame_inner, text="2", variable=stopbit_var, value="2")
stopbit_2_radio.pack(side="left", padx=5)

stopbit_var.set("1") # ตั้งค่าให้เลือก Stop bit 1 เป็นค่า default

# สร้าง Parity สำหรับเลือก Parity
parity_frame = ttk.LabelFrame(root, text="Parity")
parity_frame.pack(pady=10)

parity_frame_inner = ttk.Frame(parity_frame)
parity_frame_inner.pack()

parity_var = tk.StringVar()
parity_none_radio = ttk.Radiobutton(parity_frame_inner, text="None", variable=parity_var, value="None")
parity_none_radio.pack(side="left", padx=5)
parity_odd_radio = ttk.Radiobutton(parity_frame_inner, text="Odd", variable=parity_var, value="Odd")
parity_odd_radio.pack(side="left", padx=5)
parity_even_radio = ttk.Radiobutton(parity_frame_inner, text="Even", variable=parity_var, value="Even")
parity_even_radio.pack(side="left", padx=5)
parity_mark_radio = ttk.Radiobutton(parity_frame_inner, text="Mark", variable=parity_var, value="Mark")
parity_mark_radio.pack(side="left", padx=5)
parity_space_radio = ttk.Radiobutton(parity_frame_inner, text="Space", variable=parity_var, value="Space")
parity_space_radio.pack(side="left", padx=5)

parity_var.set("None") # ตั้งค่าให้เลือก Parity None เป็นค่า default

# สร้าง Handsake สำหรับเลือก Handsake



# handshake_frame = ttk.LabelFrame(root, text="Handshake")
# handshake_frame.pack(pady=10)

# handshake_frame_inner = ttk.Frame(handshake_frame)
# handshake_frame_inner.pack()

# handshake_var = tk.StringVar()
# handshake_none_radio = ttk.Radiobutton(handshake_frame_inner, text="None", variable=handshake_var, value="None")
# handshake_none_radio.pack(side="left", padx=5)
# handshake_xonxoff_radio = ttk.Radiobutton(handshake_frame_inner, text="Xon/Xoff", variable=handshake_var, value="Xon/Xoff")
# handshake_xonxoff_radio.pack(side="left", padx=5)
# handshake_rtscts_radio = ttk.Radiobutton(handshake_frame_inner, text="RTS/CTS", variable=handshake_var, value="RTS/CTS")
# handshake_rtscts_radio.pack(side="left", padx=5)
# handshake_dsrdtr_radio = ttk.Radiobutton(handshake_frame_inner, text="DSR/DTR", variable=handshake_var, value="DSR/DTR")
# handshake_dsrdtr_radio.pack(side="left", padx=5)
# # Set Handsake to None as default
# handshake_var.set("None")

# สร้าง Entry สำหรับป้อนข้อความ
input_label = ttk.Label(root, text="Enter message:")
input_label.pack(pady=10)

input_var = tk.StringVar()
input_entry = ttk.Entry(root, textvariable=input_var)
input_entry.pack(pady=5)

message_entry = ttk.Entry(root, width=50)

# สร้าง Button สำหรับส่งข้อความผ่าน Serial port
def send_message():
    try:
        databit = int(databit_var.get())
        stopbit = float(stopbit_var.get())
        baudrate = int(baud_var.get())
        parity = parity_var.get()
        message = input_var.get()
        ser = serial.Serial('COM1', baudrate, bytesize=databit, stopbits=stopbit, parity=parity, timeout=1000)
        ser.dsrdtr = True
        ser.rtscts = False
        message = message_entry.get().encode('ASCII')
        ser.write(message)
        ser.close()

    except serial.SerialException:
        messagebox.showwarning("Warning", "Cannot Send!")
        return
    ser.close() # ปิด Serial port

send_button = ttk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

# สร้าง Footer
footer_frame = ttk.Frame(root)
footer_frame.pack(side="bottom", pady=10)

# สร้าง Label สำหรับแสดงข้อความ Copyright
copyright_label = ttk.Label(
    footer_frame, 
    text="\u00A9 2023 Pornsupat Vutisuwan. All rights reserved.", 
    font=("Helvetica", 8)
)
copyright_label.pack()

root.mainloop()


# ทำฟังก์ชันสำหรับปิด Serial port ให้เมื่อปิดโปรแกรม
# มี Handshaking ด้วย
# โดย RTS จะถูกตั้งค่าเป็น 0 และ DTR จะถูกตั้งค่าเป็น 1 เมื่อกดส่ง โปแกรมจะสั่งให้ pin7 ทำงานโดยส่งเป็น 1 และ pin8 ทำงานโดยส่งเป็น 0



