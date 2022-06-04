import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime as dt
from tkcalendar import Calendar, DateEntry
from tkinter.scrolledtext import *
from tkinter import messagebox
from db import Database

db = Database("tasks.db")

app = Tk()

# basic structure
app.title('TODO APPLICATION')
# size of window
app.geometry('780x450')
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
mbutton1 = Button(tab2, text='Add', width=12, bg='#03A9F4', fg='#fff')
mbutton1.grid(row=6, column=0, padx=5, pady=10)

mbutton2 = Button(tab2, text='Clear', width=12, bg='#03A9F4', fg='#fff')
mbutton2.grid(row=10, column=0, padx=5, pady=10)

mbutton3 = Button(tab2, text='Update', width=12, bg='#03A9F4', fg='#fff')
mbutton3.grid(row=6, column=1, padx=5, pady=10)

mbutton4 = Button(tab2, text='Delete', width=12, bg='#03A9F4', fg='#fff')
mbutton4.grid(row=6, column=2, padx=5, pady=10)

mbutton5 = Button(tab2, text='Completed', width=12, bg='#03A9F4', fg='#fff')
mbutton5.grid(row=10, column=1, padx=5, pady=10)

# display screen in homework page
# tab2_display = ScrolledText(tab2, height=5)
# tab2_display.grid(row=7, column=0, padx=5, pady=5, columnspan=3)
parts_list = Listbox(tab2, height=8, width=80, border=0)
parts_list.grid(row=15, column=0, columnspan=3, rowspan=6, pady=20, padx=10)
# Create scrollbar
scrollbar = Scrollbar(tab2)
scrollbar.grid(row=15, column = 3)
# Set scrollbar to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
# Bind select
#parts_list.bind('<<ListboxSelect>>', select_item)

# about Page
abt = Label(tab4, text='This application helps add tasks\n\nApplication designed by Venu\n\nCopyright \u00A9 Venu', padx = 10, pady = 10)
abt.grid(column=0, row=1)

app.mainloop()