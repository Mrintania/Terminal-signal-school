from PIL import Image, ImageTk
import tkinter as tk

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("Terminal for Radio")
root.geometry('')
root.resizable(True, True)

# สร้าง label และภาพ logo
imgage = Image.open("../Terminal for radio/Images/siglogo.png")

tkimage = ImageTk.PhotoImage(imgage)
lable = tk.Label(root, image=tkimage)
lable.pack()  
root.mainloop()  