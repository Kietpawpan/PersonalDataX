# Import module
import tkinter
from tkinter import *

# Import message box module
from tkinter import messagebox

# Create object
root = Tk()

# Set the title, GUI size, and font size
root.title("PDX-v1.0.0")
root.geometry("700x300")
root.option_add("*font", "20")

# Set the option IDs and their values for decision tree (3 layers)
Option1 = "เจ้าของข้อมูลส่วนบุคคล"
Option2 = "ไม่ใช่ เจ้าของข้อมูลส่วนบุคคล"

Option1_1 = "ขอสำเนาหรือขอให้เปิดเผยถึงการได้มา"
Option1_2 = "ขอข้อมูลรูปแบบที่อ่านหรือใช้งานทั่วไปด้วยเครื่องมืออัตโนมัติ"
Option1_3 = "ขอข้อมูลที่ส่งหรือโอนไปผู้ควบคุมอื่น"

Option2_1 = "ได้รับความยินยอมจากเจ้าของข้อมูล"
Option2_2 = "ไม่ได้รับ ความยินยอมจากเจ้าของข้อมูล"

Option1_1_1 = "มีกฎหมายหรือมีคำสั่งศาลห้ามเปิดเผยและจะกระทบสิทธิเสรีภาพของบุคคลอื่น"
Option1_1_2 = "ไม่เข้าเงื่อนไขดังกล่าว"

Option1_2_1 = "ปฏิบัติหน้าที่เพื่อประโยชน์สาธารณะ"
Option1_2_2 = "ไม่เข้าเงื่อนไขดังกล่าว"

Option2_1_1 = "การขอความยินยอม ถูกต้อง ตามกฎหมาย"
Option2_1_2 = "การขอความยินยอม ไม่ถูกต้อง ตามกฎหมาย"

# Set the dropdown menu options
choices1 = [Option1, Option2]
choices1_1 = [Option1_1, Option1_2, Option1_3]
choices1_1_1 = [Option1_1_1, Option1_1_2]
choices1_2 = [Option1_2_1, Option1_2_2]

# Set the datatype of menu text
clicked = StringVar()
clicked1 = StringVar()
clicked2 = StringVar()

# Set the questions
clicked.set("ผู้ขอเป็นบุคคลใด?")
clicked1.set("ขอข้อมูลประเภทใด?")
clicked2.set("A cup of coffee?")

# Create the function to clear screen of the root window
def reset():
    for child in root.winfo_children():
        child.destroy()

# Show the question for Option1.1, with the dropdown choices for selection
def Query1():
    # If the user clicks Option 1.1
    if clicked.get() == Option1:
        # Reset the screen
        reset()
        # Set the question and the choices for Option 1.1
        drop1_1 = OptionMenu(root, clicked1, *choices1_1)
        # Locate the choices on the screen
        drop1_1.pack()
        # Show Button for Question 1.1
        button = Button(root, text="ยืนยัน", command=Query1_1_1).pack()
    elif clicked1.get() == Option2:
        reset()
        # Set the question and the choices for Option 1.1
        drop1_2 = OptionMenu(root, clicked2, *choices1_2)
        # Locate the choices on the screen
        drop1_2.pack()
        # Show Button for Question 1.1
        button = Button(root, text="Select", command=Query1_1_2).pack()

def Query1_1_1():
    label = Label(root, text="Done!")
    label.pack()
    # Show the message box to give the expert opinion for Node 1.1.1
    messagebox.showinfo("AI Opinion", "เปิดเผยตามคำขอ")

# Create Dropdown menu for the first question
drop1 = OptionMenu(root, clicked, *choices1)
drop1.pack()

# Create button, it will change label text
button = Button(root, text="ยืนยัน", command=Query1).pack()

# Create Label
label = Label(root, text=" ")
label.pack()

# Execute tkinter
root.mainloop()

# Design the message box to show after the user reaches Node 1.1.1
node1_1_1InfoBox = Tk()
node1_1_1InfoBox.geometry("300x200")
node1_1_1InfoBox.mainloop()
