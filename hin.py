import tkinter as tk
from tkinter.font import Font
import numpy as np
import random
from tkinter import ttk, Canvas

from playsound import playsound
import os
import gtts
from gtts import gTTS

import re
import nltk
from nltk.corpus import words

from tkinter import messagebox
a = 0
set_a = 0
with open("dataword2.txt", "r", encoding="utf-8") as file:
    data = file.read()
    data_split = data.split(" ")
    numpy_data = np.array(data_split)

    num_split = len(numpy_data)
    num_row = num_split / 3
    new_array = numpy_data.reshape(int(num_row), 3)
    random_numbers = random.sample(range(0, int(num_row)), int(num_row))

show_text = ""
count = 0
count2 = 0
check_buttom = 0




def delete_txt():
    global new_array
    global data
    
    try:

        index = int(index_input.get()) -1


        a = str(new_array[index][0])
        b = str(new_array[index][1])
        c = str(new_array[index][2])
        if index == 0:
            data = data.replace(f"{a} {b} {c} ","")
        else:
            data = data.replace(f" {a} {b} {c}" or f"{a} {b} {c} ","")

        with open("dataword2.txt", "w", encoding="utf-8") as file:
            file.write(data)
            data_split = data.split(" ")
            numpy_data = np.array(data_split)

            num_split = len(numpy_data)
            num_row = num_split / 3
            new_array = numpy_data.reshape(int(num_row), 3)

        txt_label.config(text="ลบคำศัพท์ออกแล้ว!")
    except:
        txt_label.config(text="ไม่มีคำศัพท์ลำดับที่คุณกรอกมาในไฟล์!")

def check_word(event):
    content = str(input_eng.get())
    if re.sub(r"[^\w]", "", content.lower()) not in words.words():
        input_eng.config(foreground="red")
    else:
        input_eng.config(foreground="black")


def write_txt():
    eng_word = input_eng.get()
    th_word = input_th.get()
    read_th = input_read_th.get()
    if re.sub(r"[^\w]", "", eng_word.lower()) not in words.words():
        a = messagebox.askquestion('แจ้งเตือน',"คำศัพท์ของคุณอาจจะผิดต้องการเพิ่มลงไฟล์ไหม")
        if a == "yes":
            qc_eng = all(ord(char) < 123 and ord(char) > 64 for char in eng_word)
            qc_th = all(ord(char) < 3676 and ord(char) > 3584 for char in th_word)
            qc_read_th = all(ord(char) < 3676 and ord(char) > 3584 for char in read_th)
            if qc_eng and qc_th and qc_read_th == True:
                with open("dataword2.txt", "at", encoding="utf-8") as file:
                    file.write(" " + eng_word + " " + th_word + " " + read_th)
                    txt_label.config(text="เพิ่มคำศัพท์ลงไฟล์แล้ว!")
                    input_eng.delete(0, tk.END)
                    input_th.delete(0, tk.END)
                    input_read_th.delete(0, tk.END)
            else:
                txt_label.config(text="กรุณากรอกตัวอักษรให้ถูกประเภท")
    else:
        qc_eng = all(ord(char) < 123 and ord(char) > 64 for char in eng_word)
        qc_th = all(ord(char) < 3676 and ord(char) > 3584 for char in th_word)
        qc_read_th = all(ord(char) < 3676 and ord(char) > 3584 for char in read_th)
        if qc_eng and qc_th and qc_read_th == True:
            with open("dataword2.txt", "at", encoding="utf-8") as file:
                file.write(" " + eng_word + " " + th_word + " " + read_th)
                txt_label.config(text="เพิ่มคำศัพท์ลงไฟล์แล้ว!")
                input_eng.delete(0, tk.END)
                input_th.delete(0, tk.END)
                input_read_th.delete(0, tk.END)
        else:
            txt_label.config(text="กรุณากรอกตัวอักษรให้ถูกประเภท")
    
def play_mp3():
    qc_eng = all(ord(char) < 123 and ord(char) > 64 for char in show_text)
    qc_th = all(ord(char) < 3676 and ord(char) > 3584 for char in show_text)
    try:
        if qc_th == True:
            tts = gTTS(show_text,lang='th')
            tts.save('speech.mp3')
            playsound('speech.mp3')
            os.remove('speech.mp3')
        else:
            tts = gTTS(show_text,lang='en')
            tts.save('speech.mp3')
            playsound('speech.mp3')
            os.remove('speech.mp3')
    except:
        result_label.config(text="ไม่มีอินเตอร์เน็ตใช้ไม่ได้")

def reset_word():
    global random_numbers
    global count
    global check_buttom
    global reset_buttom
    global loop_buttom
    global set_a
    loop_buttom.config(state=tk.DISABLED)
    reset_buttom.config(state=tk.DISABLED)
    loop_buttom.config(image=photo3)
    reset_buttom.config(image=photo5)
    random_numbers = random.sample(range(0, int(num_row)), int(num_row))
    start_button.config(state=tk.NORMAL)
    read_and_Type.config(state=tk.NORMAL)
    entry.config(state=tk.NORMAL)
    set_a = 0
    
    count = 0
    
def set_global_a():
    global set_a
    set_a = 1
    entry.config(state=tk.DISABLED)

def openNew_windows():
    add_txt_windows.deiconify()

def hide_windows():
    add_txt_windows.withdraw()

def closeAll():
    root.destroy() 
    add_txt_windows.destroy()
     
def set_count_to_zero():
    global count
    global set_a

    loop_buttom.config(state=tk.DISABLED)
    reset_buttom.config(state=tk.DISABLED)
    loop_buttom.config(image=photo3)
    reset_buttom.config(image=photo5)

    if set_a == 1:
        set_global_a()
        
    else:
         set_a = 0
         entry.config(state=tk.NORMAL)
    count = 0
    start_count()

def start_count():
    num_loop = int(num.get())
    global a
    if num_loop > int(num_row):
        num_loop = int(num_row)
        if a == 0:
            result_label.config(text="คุณใส่ศัพท์เกินแต่เราแก้ให้เป็นจำนวนสูงสุดแล้วนะ!")
            a = 1
    global count
    global count2
    global show_text
    global random_numbers
    global reset_buttom
    global loop_buttom
    try:

        start_button.config(state=tk.DISABLED)
        read_and_Type.config(state=tk.DISABLED)


        if count in range(int(num_loop)):
            show_text = new_array[random_numbers[count], count2]
            show_textread = new_array[random_numbers[count], 2]
            label.config(text=str(show_text))
            labelread.config(text=str(show_textread))
            count2 += 1
            

            if count2 > 1:
                count2 = 0
                count += 1
                result_label.config(text=show_word)
        else:
            label.config(text="คำศัพท์หมดแล้วว!")
            result_label.config(text=show_word)
            labelread.config(text="คำอ่าน")
            loop_buttom.config(state=tk.NORMAL)
            reset_buttom.config(state=tk.NORMAL)
            loop_buttom.config(image=photo1H)
            reset_buttom.config(image=photo2H)
            
            a = 0
           
               

    except ValueError:
        result_label.config(text="มีอะไรผิดพลาดโปรดใส่ข้อมูลให้ครบ")
        start_button.config(state=tk.NORMAL)

def clear_entry(event, name):
    name.delete(0, tk.END)

def check_number(event):
    global set_a
    try:
        if set_a == 1:
            start_count()
        else:
            user_input = entry.get()
            user_word = str(user_input)
            if user_word.lower() == show_text.lower():
                    start_count()
                    entry.delete(0, tk.END)
            else:
                result_label.config(text="ผิด! ลองอีกครั้ง")
    except ValueError:
        result_label.config(text="โปรดใส่ตัวเลขที่ถูกต้อง")


#-------------------------------------

root = tk.Tk()
root.title("ตัวอย่างโปรแกรมที่ใช้ ttk")
root.resizable(False, False)
root.minsize(width=550, height=250)
root.maxsize(width=650, height=500)
root.configure(bg='#D3F2FF')

frame = tk.Frame(root,bg='#D3F2FF')
frame.grid(row=0,column=0,padx=50,pady=10)

frame2 = tk.Frame(frame,bg='#D3F2FF')
frame2.grid(row=3, column=0, pady=10)

frame3 = tk.Frame(frame,bg='#D3F2FF')
frame3.grid(row=6, column=0, pady=10)

photo1 = tk.PhotoImage(file="next.png")
photo2 = tk.PhotoImage(file="playsong.png")
photo3 = tk.PhotoImage(file="rerun.png")
photo4 = tk.PhotoImage(file="up.png")
photo5 = tk.PhotoImage(file="random.png")
photo6 = tk.PhotoImage(file="playpro.png")
photo7 = tk.PhotoImage(file="test.png")
photo1H = tk.PhotoImage(file="rerun_h.png")
photo2H = tk.PhotoImage(file="random_h.png")

style = ttk.Style()
style.configure("TButton", font=("Kumothin", 18))


label = tk.Label(frame, text="คำศัพท์", font=("Kumothin", 30, "bold"),bg='#D3F2FF')
label.grid(row=0,column=0,pady=5)

labelread = tk.Label(frame,text="คำอ่าน",font=("Kumothin", 25, "bold"),bg='#D3F2FF')
labelread.grid(row=1,column=0,pady=5)

entry = ttk.Entry(frame, text="input words",width=40,font=("Kumothin", 18),justify='center')
entry.insert(0,"กรอกข้อความ")
entry.bind("<Button-1>", lambda event,name=entry:clear_entry(event,name))
entry.bind("<Return>", check_number)
entry.grid(row=2,column=0,pady=5)

ok_button = tk.Button(frame, image=photo1,borderwidth=0, bg='#D3F2FF',command=lambda event=None:check_number(event))
ok_button.grid(row=3,column=0,pady=5)

read_and_Type = tk.Button(frame, image=photo7,borderwidth=0, bg='#D3F2FF',command=lambda:(start_count(),show_messagebox2()))
read_and_Type.grid(row=4,column=0,padx=(5,0),sticky='w')

play_mp3_button = tk.Button(frame, image=photo2,borderwidth=0, bg='#D3F2FF',command=play_mp3)
play_mp3_button.grid(row=4,column=0,padx=(0,5),sticky='e')

loop_buttom = tk.Button(frame, image=photo3,borderwidth=0, bg='#D3F2FF',command=set_count_to_zero)
loop_buttom.grid(row=5,column=0,padx=7,pady=5,sticky='w')

add_word_button = tk.Button(frame, image=photo4,borderwidth=0, bg='#D3F2FF',command=openNew_windows)
add_word_button.grid(row=5,column=0,padx=7,pady=5,sticky='e')

show_word = "คำศัพท์ที่มีทั้งหมด = " + str(num_row)
result_label = tk.Label(frame3,text=show_word,font=("Kumothin", 20, "normal"),bg='#D3F2FF')
result_label.grid(row=1,column=0,columnspan=4,pady=(0,5))


reset_buttom = tk.Button(frame3, image=photo5,borderwidth=0, bg='#D3F2FF',command=reset_word)
reset_buttom.grid(row=2,column=0,padx=7,pady=5,)

num = ttk.Entry(frame3,width=10,font=("Kumothin", 18, "bold"))
num.insert(0,"กรอกจำนวนคำศัพท์")
num.bind("<Button-1>", lambda event,name=num:clear_entry(event,name))
num.grid(row=2,column=1,padx=7,pady=5)

loop_buttom.config(state=tk.DISABLED)
reset_buttom.config(state=tk.DISABLED)

num_show2 = 0
num_show = 0

def show_messagebox():
    global num_show2
    if num_show2 == 0:
        messagebox.showinfo("วิธีการใช้งาเบื้องต้น", "จะมีคำศัพท์และคำอ่านถูกแสดงตรงกลางหน้าจอ ผู้ใช้สามารถกดปุ่มถัดไปเพื่อให้คำสั่งศัพท์ถูกแสดงจนครบกำหนด")
        num_show2 = 1
    else:
        pass

def show_messagebox2():
    global num_show
    if num_show == 0:
        messagebox.showinfo("วิธีการใช้งาเบื้องต้น", "จะมีคำศัพท์และคำอ่านถูกแสดงตรงกลางหน้าจอ ให้ผู้ใช้กรอกตามตัวอักษรที่เห็นและกดปุ่มถัดไป หรือ Enter บนคีย์บอร์ด เพื่อไปคำศัพท์ถัดไป")
        num_show = 1
    else:
        pass

start_button = tk.Button(frame3, image=photo6,borderwidth=0, bg='#D3F2FF',command=lambda: (start_count(),set_global_a(),show_messagebox()))
start_button.grid(row=2,column=2,padx=7,pady=5) 


#-------------------------------------

add_txt_windows = tk.Tk()
add_txt_windows.title("ตัวอย่างโปรแกรมที่ใช้ ttk")
add_txt_windows.resizable(False, False)
add_txt_windows.minsize(width=550, height=250)
add_txt_windows.maxsize(width=650, height=1000)


frame = ttk.Frame(add_txt_windows)
frame.grid(row=0, column=0, padx=50, pady=10)

frame2 = ttk.Frame(add_txt_windows)
frame2.grid(row=2, column=0, padx=50, pady=10)

style = ttk.Style()
style.configure("TButton", font=("Kumothin", 18))


input_th = ttk.Entry(frame , width=35, font=("Kumothin", 18))
input_th.grid(row=1, column=0, pady=5)
input_th.insert(0,"กรอกข้อความภาษาไทย")
input_th.bind("<Button-1>", lambda event, entry=input_th: clear_entry(event, entry))


input_eng = ttk.Entry(frame, width=35, font=("Kumothin", 18))
input_eng.grid(row=2, column=0, pady=5)
input_eng.insert(0,"กรอกข้อความภาษาอังกฤษ")
input_eng.bind("<KeyRelease>", check_word)
input_eng.bind("<Button-1>", lambda event, entry=input_eng: clear_entry(event, entry))

input_read_th = ttk.Entry(frame , width=35, font=("Kumothin", 18))
input_read_th.grid(row=3, column=0, pady=5)
input_read_th.insert(0,"กรอกข้อความคำอ่านภาษาไทย")
input_read_th.bind("<Button-1>", lambda event, entry=input_read_th: clear_entry(event, entry))

oK2_button = ttk.Button(frame, text="OK", width=40 ,command=write_txt)
oK2_button.grid(row=4, column=0, pady=5)

#########

index_input = ttk.Entry(frame , width=20, font=("Kumothin", 16))
index_input.grid(row=5, column=0, pady=0 ,sticky='w')
index_input.insert(0,"กรอก")
index_input.bind("<Button-1>", lambda event, entry=index_input: clear_entry(event, entry))

delete_button = ttk.Button(frame, text="OK", width=30 ,command=delete_txt)
delete_button.grid(row=5, column=0, pady=0,sticky='e')

#########

txt_label = tk.Label(add_txt_windows, text="")
txt_label.grid(row=4, column=0, pady=5)

def on_mousewheel(event):
    mycanvas.yview_scroll(-1 * (event.delta // 120), "units")

def on_horizontal_scroll(*args):
    mycanvas.xview(*args)

def show_wordQWQ():

    for widget in myframe.winfo_children():
        if widget.grid_info()['column'] in [0, 1, 2, 3]:
            widget.destroy()

    with open("dataword2.txt", "r", encoding="utf-8") as file:
        data = file.read()
        data_split = data.split(" ")
        numpy_data = np.array(data_split)

        num_split = len(numpy_data)
        num_row = num_split / 3
        new_array = numpy_data.reshape(int(num_row), 3)
        random_numbers = random.sample(range(0, int(num_row)), int(num_row))

    labels = []
    indexlabel = ttk.Label(myframe, text="ลำดับ", font=("Kumothin", 18)).grid(row=0, column=0, padx=(20, 30))
    wordlabel = ttk.Label(myframe, text="คำศัพท์", font=("Kumothin", 18)).grid(row=0, column=1, padx=(40, 30))
    wordTHlabel = ttk.Label(myframe, text="คำแปล", font=("Kumothin", 18)).grid(row=0, column=2, padx=(0, 30))
    readlabel = ttk.Label(myframe, text="คำอ่าน", font=("Kumothin", 18)).grid(row=0, column=3, padx=(20, 25))

    for i in range(int(num_row)):
        labels.append(label)
        q = ttk.Label(myframe, text=i+1, font=("Kumothin", 18)).grid(row=i+1, column=0, padx=(20, 30))
        w = ttk.Label(myframe, text=new_array[i, 0], font=("Kumothin", 18)).grid(row=i+1, column=1, padx=(50, 30))
        e = ttk.Label(myframe, text=new_array[i, 1], font=("Kumothin", 18)).grid(row=i+1, column=2, padx=(30, 30))
        r = ttk.Label(myframe, text=new_array[i, 2], font=("Kumothin", 18)).grid(row=i+1, column=3, padx=(20, 25))

    myframe.update_idletasks()
    mycanvas.config(scrollregion=mycanvas.bbox("all"))

wrapper1 = ttk.LabelFrame(add_txt_windows)
wrapper2 = ttk.LabelFrame(add_txt_windows)

mycanvas = Canvas(wrapper1)
mycanvas.grid(row=1, column=0)
mycanvas.config(width=550, height=300)  

yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
yscrollbar.grid(row=1, column=1, sticky="ns")  
mycanvas.configure(yscrollcommand=yscrollbar.set)

xscrollbar = ttk.Scrollbar(wrapper2, orient="horizontal", command=mycanvas.xview)
xscrollbar.grid(row=0, column=0, sticky="ew")
mycanvas.configure(xscrollcommand=xscrollbar.set)

mycanvas.bind('<Enter>', lambda e: mycanvas.bind_all('<MouseWheel>', on_mousewheel))
mycanvas.bind('<Leave>', lambda e: mycanvas.unbind_all('<MouseWheel>'))

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myframe = ttk.Frame(mycanvas)
mycanvas.create_window((0, 0), window=myframe, anchor="nw")

wrapper1.grid(row=1, column=0, padx=10, pady=10)  
wrapper2.grid(row=2, column=0, padx=10, pady=10) 

s_button = ttk.Button(frame2, text="กลับหน้าเดิม", command=hide_windows ,width=10 )
s_button.grid(row=0, column=0 ,padx=(0,10))

s_w_button = ttk.Button(frame2, text="แสดงคำศัพท์ในไฟล์", command=show_wordQWQ ,width=23 ,style="TButton")
s_w_button.grid(row=0, column=1 ,padx=(0,0))

hide_windows()
add_txt_windows.protocol("WM_DELETE_WINDOW", hide_windows)
root.protocol("WM_DELETE_WINDOW", closeAll)

root.mainloop()
