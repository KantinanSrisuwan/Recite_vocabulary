import tkinter as tk
from tkinter import font
import numpy as np
import random

from playsound import playsound
import os
import gtts
from gtts import gTTS

with open("dataword.txt", "r", encoding="utf-8") as file:
    data = file.read()
    data_split = data.split(" ")
    numpy_data = np.array(data_split)

    num_split = len(numpy_data)
    num_row = num_split / 2
    new_array = numpy_data.reshape(int(num_row), 2)
    random_numbers = random.sample(range(0, int(num_row)), int(num_row))

show_text = ""
count = 0
count2 = 0

def write_txt():
    eng_word = input_eng.get()
    th_word = input_th.get()
    qc_eng = all(ord(char) < 123 and ord(char) > 64 for char in eng_word)
    qc_th = all(ord(char) < 3676 and ord(char) > 3584 for char in th_word)
    print(qc_eng,qc_th)
    if qc_eng and qc_th == True:
        with open("dataword.txt", "at", encoding="utf-8") as file:
            file.write(" " + eng_word + " " + th_word)
            txt_label.config(text="เพิ่มคำศัพท์ลงไฟล์แล้ว!")
            input_eng.delete(0, tk.END)
            input_th.delete(0, tk.END)
    else:
        txt_label.config(text="กรุณากรอกตัวอักษรให้ถูกประเภท")
    
def play_mp3():
    tts = gTTS(show_text,lang='en')
    tts.save('speech.mp3')
    playsound('speech.mp3')
    os.remove('speech.mp3')


def openNew_windows():
    add_txt_windows.deiconify()

def hide_windows():
    add_txt_windows.withdraw()

def closeAll():
    root.destroy() 
    add_txt_windows.destroy()
     

def start_count():
    global count
    global count2
    global show_text
    global random_numbers
    try:
        num_loop = int(num.get())
        if num_loop > int(num_row):
            num_loop = int(num_row)

        start_button.config(state=tk.DISABLED)

        if count in range(int(num_loop)):
            show_text = new_array[random_numbers[count], count2]
            label.config(text=str(show_text))
            count2 += 1

            if count2 > 1:
                count2 = 0
                count += 1
        else:
            random_numbers = random.sample(range(0, int(num_row)), int(num_row))
            start_button.config(state=tk.NORMAL)
            label.config(text="คำศัพท์หมดแล้วว!")
            count = 0

    except ValueError:
        result_label.config(text="มีอะไรผิดพลาดโปรดใส่ข้อมูลให้ครบ")
        start_button.config(state=tk.NORMAL)

def clear_entry(event, name):
    name.delete(0, tk.END)

def check_number(event):
    user_input = entry.get()
    try:
        user_word = str(user_input)
        if user_word == show_text:
            start_count()
            entry.delete(0, tk.END)
            result_label.config(text="")
        else:
            result_label.config(text="ผิด! ลองอีกครั้ง")
    except ValueError:
        result_label.config(text="โปรดใส่ตัวเลขที่ถูกต้อง")

    
root = tk.Tk()
custom_font = font.Font(family="Arial", size=16)
root.option_add("*Font", custom_font)
root.title("โปรแกรมท่องศัพท์")

label = tk.Label(root, text="กรุณากดปุ่มเริ่ม")
label.pack()

start_button = tk.Button(root, text="Start", command=start_count)
start_button.pack()

play_mp3_button = tk.Button(root, text="play", command=play_mp3)
play_mp3_button.pack()

num = tk.Entry(root,justify='center')
num.insert(0,"กรอกจำนวนคำศัพท์")
num.bind("<Button-1>", lambda event,name=num:clear_entry(event,name))
num.pack()

entry = tk.Entry(root,justify='center')
entry.insert(0,"กรอกข้อความ")
entry.bind("<Button-1>", lambda event,name=entry:clear_entry(event,name))
entry.bind("<Return>", check_number)
entry.pack()

show_word = "คำศัพท์ที่มีทั้งหมด = " + str(num_row)
result_label = tk.Label(root, text=show_word)
result_label.pack(pady=20)

ok_button = tk.Button(root, text="OK", command=lambda event=None:check_number(event))
ok_button.pack()

add_word_button = tk.Button(root, text="เขียนศัพท์เพิ่ม", command=openNew_windows)
add_word_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

add_txt_windows = tk.Tk()
add_txt_windows.title("เพิ่มข้อมูล")
add_txt_windows.geometry("500x300")
add_txt_windows.option_add("*Font", custom_font)

input_eng = tk.Entry(add_txt_windows,justify='center')
input_eng.insert(0,"กรอกข้อความภาษาอังกฤษ")
input_eng.bind("<Button-1>", lambda event, entry=input_eng: clear_entry(event, entry))
input_eng.pack()

input_th = tk.Entry(add_txt_windows,justify='center')
input_th.insert(0,"กรอกข้อความภาษาไทย")
input_th.bind("<Button-1>", lambda event, entry=input_th: clear_entry(event, entry))
input_th.pack()

txt_label = tk.Label(add_txt_windows, text="")
txt_label.pack()

add_button = tk.Button(add_txt_windows, text="OK", command=write_txt)
add_button.pack()

hide_windows()
add_txt_windows.protocol("WM_DELETE_WINDOW", hide_windows)
root.protocol("WM_DELETE_WINDOW", closeAll)

root.mainloop()
