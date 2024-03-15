import os
from tkinter import *
import customtkinter
from pathlib import Path
import pandas as pd
import glob as g

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.minsize(900, 600)
# root.resizable(width=False, height=False)
root.title("نرم افزار معادل")

uname = str(os.getcwd()).replace("\\", "/")
username = os.getlogin()

try:
    directory = "people"
    parent_dir = f"{uname}"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory)
except:
    pass

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure((0, 1), weight=1)
# _____________________________________________________________________________________________________
label1 = customtkinter.CTkLabel(master=root, text="ریاضی", font=("B Nazanin Bold", 19))
label1.place(x=65, y=50)

entry1 = customtkinter.CTkEntry(master=root, placeholder_text="نمره مستمر ریاضی", corner_radius=10,
                                font=("B Nazanin", 20))
entry1.place(x=200, y=40)

entry1_2 = customtkinter.CTkEntry(master=root, placeholder_text="نمره پایانی ریاضی", corner_radius=10,
                                  font=("B Nazanin", 20))
entry1_2.place(x=350, y=40)
# _____________________________________________________________________________________________________
label2 = customtkinter.CTkLabel(master=root, text="فارسی", font=("B Nazanin Bold", 19))
label2.place(x=60, y=80)

entry2 = customtkinter.CTkEntry(master=root, placeholder_text="نمره مستمر فارسی", corner_radius=10,
                                font=("B Nazanin", 20))
entry2.place(x=200, y=77)

entry2_2 = customtkinter.CTkEntry(master=root, placeholder_text="نمره پایانی فارسی", corner_radius=10,
                                  font=("B Nazanin", 20))
entry2_2.place(x=350, y=77)
# _____________________________________________________________________________________________________
label3 = customtkinter.CTkLabel(master=root, text="علوم", font=("B Nazanin Bold", 19))
label3.place(x=65, y=114)

entry3 = customtkinter.CTkEntry(master=root, placeholder_text="نمره مستمر علوم", corner_radius=10,
                                font=("B Nazanin", 20))
entry3.place(x=200, y=114)

entry3_2 = customtkinter.CTkEntry(master=root, placeholder_text="نمره پایانی علوم", corner_radius=10,
                                  font=("B Nazanin", 20))
entry3_2.place(x=350, y=114)
# _____________________________________________________________________________________________________
entry_name = customtkinter.CTkEntry(master=root, placeholder_text="نام و نام خانوادگی", corner_radius=10,
                                    font=("B Nazanin", 20))
entry_name.place(x=720, y=60)
# _____________________________________________________________________________________________________
final = customtkinter.CTkLabel(master=root, text="", font=("", 20), fg_color="#eee")
final.place(x=200, y=180)
# _____________________________________________________________________________________________________
my_listbox = Listbox(root)
my_listbox.place(x=500, y=20, width=210, height=555)
# _____________________________________________________________________________________________________

directory = 'people'
files = Path(directory).glob('*')

for file in files:
    x = str(file).replace("people\\", "").replace(".py", "")
    my_listbox.insert(END, x)


def select():
    entry1.delete(0, END)
    entry1_2.delete(0, END)
    entry2.delete(0, END)
    entry2_2.delete(0, END)
    entry3.delete(0, END)
    entry3_2.delete(0, END)
    entry_name.delete(0, END)
    if my_listbox.get(my_listbox.curselection()):
        # noinspection PyGlobalUndefined
        global itm
        itm = my_listbox.get(my_listbox.curselection())
        print(itm)
        entry_name.insert(END, itm)
    try:
        # file_read = open(f"people/{entry_name.get()}.py", "r")
        # noinspection PyUnboundLocalVariable
        file_read = open(f"{os.getcwd()}/people/{itm}.py", "r")

        line_numbers = [0, 1, 2, 3, 4, 5]
        # noinspection PyGlobalUndefined
        global lines
        lines = []
        for i, line1 in enumerate(file_read):
            if i in line_numbers:
                lines.append(line1.strip())
            elif i > 6:
                break

        print(lines)
        entry1.insert(END, lines[0])
        entry1_2.insert(END, lines[1])
        entry2.insert(END, lines[2])
        entry2_2.insert(END, lines[3])
        entry3.insert(END, lines[4])
        entry3_2.insert(END, lines[5])

        file_read.close()
    except:
        # customtkinter.CTkLabel(root, text="کنید وارد را بالا موارد از یکی باید شما !", text_color="#fe6262").place(
        #     x=490, y=200)
        pass

def add_item():
    file_name = open(f"{uname}/people/{entry_name.get()}.py", "w")

    rm_ = float(entry1.get())
    rp_ = float(entry1_2.get())
    fm_ = float(entry2.get())
    fp_ = float(entry2_2.get())
    om_ = float(entry3.get())
    op_ = float(entry3_2.get())

    file_name.write(f"{rm_}\n{rp_}\n{fm_}\n{fp_}\n{om_}\n{op_}")

    file_name.close()
    refresh_btn()


def remove_btn():
    label = entry_name.get()
    idx = my_listbox.get(0, END).index(label)
    my_listbox.delete(idx)
    os.remove(f"{os.getcwd()}/people/{entry_name.get()}.py")
    entry_name.delete(0, END)



def report_btn():
    people = Path(r'people')
    people_list = []
    for file in people.iterdir():
        people_list.append(file.name.replace(".py", ""))

    nomre_1 = []
    files = g.glob("./people/*.py")
    for file in files:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                nomre_1.append(lines)
    del nomre_1[1::2]

    nomre_11 = nomre_1[0][0].replace("\\n", "")
    nomre_12 = nomre_1[0][1].replace("\\n", "")
    nomre_13 = nomre_1[0][2].replace("\\n", "")
    nomre_14 = nomre_1[0][3].replace("\\n", "")
    nomre_15 = nomre_1[0][4].replace("\\n", "")
    nomre_16 = nomre_1[0][5].replace("\\n", "")

    moadel = float(nomre_11) / 6 + float(nomre_12) / 6 + float(nomre_13) / 6 + float(nomre_14) / 6 + float(
        nomre_15) / 6 + float(
        nomre_16) / 6
    data = {
        "نام": people_list,
        "ریاضی مستمر": nomre_1[0][0],
        "ریاضی پایانی": nomre_1[0][1],
        "فارسی مستمر": nomre_1[0][2],
        "فارسی پایانی": nomre_1[0][3],
        "علوم مستمر": nomre_1[0][4],
        "علوم پایانی": nomre_1[0][5],
        "معدل": moadel
    }
    df = pd.DataFrame(data)
    df.to_excel('Report.xlsx', index=False)

    def done_btn():
        repo_root.destroy()

    # Label(root, text="! فایل اکسل گزارش نمرات شما در فایل های برنامه با موفقیت ثبت شد", font=("B Nazanin", 27), fg="#03A678").place(y= 252,x=70)
    repo_root = customtkinter.CTk()
    repo_root.minsize(450, 225)
    repo_root.resizable(False, False)
    repo_root.title("گزارش")
    repo_s = Label(repo_root, text="! فایل اکسل گزارش نمرات شما در فایل های برنامه با موفقیت ثبت شد", font=("B Nazanin",15), fg="#03A678")
    repo_s.place(relx=0.5, rely=0.3, anchor="center")
    customtkinter.CTkButton(master=repo_root, text="تایید", command=done_btn, font=("B Nazanin Bold", 18)).place(relx=0.5, rely=0.7, anchor="center")
    repo_root.mainloop()

def refresh_btn():
    my_listbox.delete(0, END)
    directory2 = 'people'
    files2 = Path(directory2).glob('*')
    for h in files2:
        b = str(h).replace("people\\", "").replace(".py", "")
        my_listbox.insert(END, b)


my_btn = customtkinter.CTkButton(root, text="انتخاب", command=select, font=("B Nazanin Bold", 18))
my_btn.place(x=720, y=20)

my_btn = customtkinter.CTkButton(root, text="افزودن", command=add_item, font=("B Nazanin Bold", 18))
my_btn.place(x=720, y=100)

remove = customtkinter.CTkButton(master=root, text="حذف مورد", command=remove_btn, font=("B Nazanin Bold", 18))
remove.place(x=720, y=140)

refresh = customtkinter.CTkButton(master=root, text="تازه سازی", command=refresh_btn, font=("B Nazanin Bold", 18))
# refresh.place(x=720, y=180)

report = customtkinter.CTkButton(master=root, text="گزارش", command=report_btn, font=("B Nazanin Bold", 18))
# report.place(x=720, y=220)
report.place(x=720, y=180)


def button_event():
    rmo = float(entry1.get())
    rpa = float(entry1_2.get())
    fmo = float(entry2.get())
    fpa = float(entry2_2.get())
    omo = float(entry3.get())
    opa = float(entry3_2.get())
    r = rmo + rpa
    r = r / 2
    farsi = fmo + fpa
    farsi = farsi / 2
    o = omo + opa
    o = o / 2
    all = r + farsi + o
    all = all / 3
    all = round(all, 2)
    final.configure(text=all)


button = customtkinter.CTkButton(master=root, text="محاسبه معدل", command=button_event, font=("B Nazanin Bold", 18))
button.place(x=20, y=180)

root.mainloop()
