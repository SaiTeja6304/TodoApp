import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime as dt
from tkcalendar import Calendar, DateEntry
from tkinter.scrolledtext import *
from tkinter import messagebox
from db import Database
import csv

db = Database("tasks.db")

def view():
    # for row in db.fetch():
    #     tree.insert("",tk.END,values=row)
    hw.delete(0, END)
    for row in db.fetch():
        hw.insert(END, row)

def clear_text():
    entry_tname.delete('0', END)
    entry_des.delete('0', END)
    entry_sub.delete('0', END)
    entry_date.delete('0', END)
    entry_subject.delete('0', END)

def add_details():
    name = str(entry_tname.get())
    des = str(entry_des.get())
    mob = str(entry_sub.get())
    dd = str(entry_date.get())
    sub = str(entry_subject.get())
    if name == '' or des == '' or mob == '' or dd == '' or sub == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
    else:
        db.add(name, des, mob, dd, sub)
        result = '\nTask:{}, \nDescription:{}, \nMethod of Submission:{}, \nDue Date:{}, \nSubject:{}'
        #tab2_display.insert(tk.END,result)
        messagebox.showinfo(title='TODO APPLICATION', message='Task successfully created')
    clear_text()
    view()

def export_as_csv():
    filename = str(entry_filename.get())
    myfilename = filename + '.csv'
    with open(myfilename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['No','Task','Description','Method of submission','Due Date','Subject'])
        writer.writerows(db.fetch())
        messagebox.showinfo(title='TODO APPLICATION', message='"Exported As {}'.format(myfilename))

def select_item(event):
    try:
        global selected_item
        index = hw.curselection()[0]
        selected_item = hw.get(index)

        entry_tname.delete(0, END)
        entry_tname.insert(END, selected_item[1])
        entry_des.delete(0, END)
        entry_des.insert(END, selected_item[2])
        entry_sub.delete(0, END)
        entry_sub.insert(END, selected_item[3])
        entry_date.delete(0, END)
        entry_date.insert(END, selected_item[4])
        entry_subject.delete(0, END)
        entry_subject.insert(END, selected_item[5])
    except IndexError:
        pass

def remove_task():
    db.remove(selected_item[0])
    clear_text()
    messagebox.showinfo(title='TODO APPLICATION', message='Task successfully deleted')
    view()

def update_task():
    db.update(selected_item[0], entry_tname.get(), entry_des.get(), entry_sub.get(), entry_date.get(), entry_subject.get())
    clear_text()
    messagebox.showinfo(title='TODO APPLICATION', message='Task successfully updated')
    view()

def completed_task():
    db.remove(selected_item[0])
    clear_text()
    messagebox.showinfo(title='TODO APPLICATION', message='Task marked complete')
    view()

app = Tk()

# basic structure
app.title('TODO APPLICATION')
# size of window
app.geometry('1150x550')
# background color
app.configure(background='red')

# for tabs on left
style = ttk.Style(app)
style.configure("leftab.TNotebook", tabposition = 'wn')

tab_control = ttk.Notebook(app, style='leftab.TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

# Add tabs to Notebook
tab_control.add(tab1, text=f'{"Home":^20s}')
tab_control.add(tab2, text=f'{"Homework":^20s}')
tab_control.add(tab3, text=f'{"Export":^20s}')
tab_control.add(tab4, text=f'{"About":^20s}')

tab_control.pack(expand=1, fill="both")

# Headings on each tab
label1 = Label(tab1, text='Welcome', font="none 15 bold", pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, text='Homework Tasks', font="none 15 bold", pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text='Export', font="none 15 bold", pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab4, text='About This App', font="none 15 bold", pady=5)
label4.grid(column=0, row=0)

# Home Page
# display current date
date = dt.datetime.now()
dlabel = Label(tab1, text=f"{date:%A, %B %d, %Y}", font="Calibri, 10", padx = 10, pady = 10)
dlabel.grid(column=0, row=1)

# Homework Page
# Defining variable, taking user input, creating input box
ml1 = Label(tab2, text='Task Name:', padx=5, pady=5)
ml1.grid(column=0, row=1)
tname = StringVar()
entry_tname = Entry(tab2, textvariable=tname, width=50)
entry_tname.grid(column=1, row=1)

ml2 = Label(tab2, text='Description:', padx=5, pady=5)
ml2.grid(column=0, row=2)
des = StringVar()
entry_des = Entry(tab2, textvariable=des, width=50)
entry_des.grid(column=1, row=2)

ml3 = Label(tab2, text='Method of Submission:', padx=5, pady=5)
ml3.grid(column=0, row=3)
sub = StringVar()
entry_sub = Entry(tab2, textvariable=sub, width=50)
entry_sub.grid(column=1, row=3)
# creating calendar
ml4 = Label(tab2, text='Due Date:', padx=5, pady=5)
ml4.grid(column=0, row=4)
date = StringVar()
entry_date = DateEntry(tab2, textvariable=date, width=30, background='darkblue', foreground='white', borderwidth=2, year=2022)
entry_date.grid(column=1, row=4, padx=10, pady=10)

ml5 = Label(tab2, text='Subject:', padx=5, pady=5)
ml5.grid(column=0, row=5)
subject = StringVar()
entry_subject = Entry(tab2, textvariable=subject, width=50)
entry_subject.grid(column=1, row=5)

# buttons creation
mbutton1 = Button(tab2, text='Add', width=12, bg='#03A9F4', fg='#fff', command=add_details)
mbutton1.grid(row=6, column=0, padx=5, pady=10)

mbutton2 = Button(tab2, text='Clear', width=12, bg='#03A9F4', fg='#fff', command=clear_text)
mbutton2.grid(row=10, column=0, padx=5, pady=10)

mbutton3 = Button(tab2, text='Update', width=12, bg='#03A9F4', fg='#fff', command=update_task)
mbutton3.grid(row=6, column=1, padx=5, pady=10)

mbutton4 = Button(tab2, text='Delete', width=12, bg='#03A9F4', fg='#fff', command=remove_task)
mbutton4.grid(row=6, column=2, padx=5, pady=10)

mbutton5 = Button(tab2, text='Completed', width=12, bg='#03A9F4', fg='#fff')
mbutton5.grid(row=10, column=1, padx=5, pady=10)

# display screen in homework page
# tab2_display = ScrolledText(tab2, height=5)
# tab2_display.grid(row=7, column=0, padx=5, pady=5, columnspan=3)
hw = Listbox(tab2, height=8, width=80, border=0)
hw.grid(row=15, column=0, columnspan=3, rowspan=6, pady=20, padx=10)
#Create scrollbar
scrollbar = Scrollbar(tab2)
scrollbar.grid(row=15, column = 3)
#Set scrollbar to listbox
hw.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=hw.yview)
#Bind select
hw.bind('<<ListboxSelect>>', select_item)
# tree = ttk.Treeview(tab2, column=('column1', 'column2', 'column3', 'column4', 'column5', 'column6'), show='headings')
# tree.heading('#1', text='No')
# tree.heading('#2', text='Task')
# tree.heading('#3', text='Description')
# tree.heading('#4', text='Method of submission')
# tree.heading('#5', text='Due date')
# tree.heading('#6', text='Subject')
# tree.grid(row=7, column=0, columnspan=200, padx=0, pady=5)

# about Page
abt = Label(tab4, text='This application helps add tasks\n\nApplication designed by Venu\n\nCopyright \u00A9 Venu', padx = 10, pady = 10)
abt.grid(column=0, row=1)

# export page
label_export1 = Label(tab3, text='File Name:',padx=5,pady=5)
label_export1.grid(column=0,row=2)
filename_raw_entry = StringVar()
entry_filename = Entry(tab3, textvariable=filename_raw_entry, width=30)
entry_filename.grid(row=2,column=1)

b1 = Button(tab3, text='Export to CSV', width=12, bg='#03A9F4', fg='#fff',command=export_as_csv)
b1.grid(row=3, column=1, padx=10, pady=10)


view()

app.mainloop()