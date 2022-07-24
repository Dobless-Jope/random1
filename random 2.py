from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import smtplib
screen5 = Tk()
screen5.title('Event database')
screen5.geometry("900x540+0+0")


def exit():
    screen5.destroy()


def reset():
    name.set("")
    lf2_entry.current(0)
    budget.set("")
    lf4_entry.current(0)
    date.set("")
    location.set("")
    rt1.delete("1.0", END)


def enter():
    n = name.get()
    e = event.get()
    b = budget.get()
    m = manager.get()
    l = location.get()
    if e == 'Birthday':
        with open('Birthday.csv', 'a+', newline="") as fh:
            writer = csv.writer(fh)
            a = [n, e, b, m, l]
            writer.writerow(a)
    elif e == "Marriage":
        with open('Marriage.csv', 'a+', newline="") as m:
            writer = csv.writer(m)
            b = [n, e, b, m, l]
            writer.writerow(b)
    elif e == "Corporate Meeting":
        with open('Corporate Meeting', 'a+', newline="") as m:
            writer = csv.writer(m)
            c = [n, e, b, m, l]
            writer.writerow(c)
    elif e == "Informal Get Together":
        with open('Informal Get Together', 'a+', newline="") as m:
            writer = csv.writer(m)
            d = [n, e, b, m, l]
            writer.writerow(d)
    elif e == "Conference":
        with open('Conference', 'a+', newline="") as m:
            writer = csv.writer(m)
            f = [n, e, b, m, l]
            writer.writerow(f)
    elif e == "Seminar":
        with open('Seminar.csv', 'a+', newline="") as m:
            writer = csv.writer(m)
            g = [n, e, b, m, l]
            writer.writerow(g)
    elif e == "Award shows and competition":
        with open('Award shows and competition', 'a+', newline="") as m:
            writer = csv.writer(m)
            h = [n, e, b, m, l]
            writer.writerow(h)
    elif e == "Charity event":
        with open('Charity.csv', 'a+', newline="") as m:
            writer = csv.writer(m)
            i = [n, e, b, m, l]
            writer.writerow(i)


def overview():
    rt1.insert(END, "Name of the person:\t\t" + name.get()+"\n")
    rt1.insert(END, "Type of event:\t\t" + event.get() + "\n")
    rt1.insert(END, "Event budget:\t\t" + budget.get()+"\n")
    rt1.insert(END, "Event Manager:\t\t" + manager.get()+"\n")
    rt1.insert(END, "Date of the event:\t\t" + date.get()+"\n")
    rt1.insert(END, "Event location:\t\t" + location.get())


Label(screen5, bd=20, relief=RIDGE, text="EVENT DATABASE", font=(
    "times new roman", 50, "bold")).pack(side=TOP, fill=X)

f1 = Frame(screen5, bd=20, relief=RIDGE)
f1.place(x=0, y=130, width=900, height=300)

lf = LabelFrame(f1, bd=10, relief=RIDGE, text='Event details',
                padx=10, font=("times new roman", 12, "bold"))
lf.place(x=0, y=5, width=500, height=250)

name = StringVar()
event = StringVar()
budget = StringVar()
manager = StringVar()
date = StringVar()
location = StringVar()
rt1 = StringVar()

lf1 = Label(lf, text='Full name of the user', font=(
    "times new roman", 12, "bold"), padx=2, pady=6)
lf1.grid(row=0, column=0)

lf1_entry = Entry(lf, font=("times new roman", 12, "bold"),
                  textvariable=name, width=35)
lf1_entry.grid(row=0, column=1)

lf2 = Label(lf, text='Event to be planned', font=(
    "times new roman", 12, "bold"), padx=2, pady=6)
lf2.grid(row=1, column=0)

lf2_entry = ttk.Combobox(
    lf, font=("times new roman", 12, "bold"), state='readonly', width=33, textvariable=event)
lf2_entry["values"] = ("", "Birthday", 'Marriage', 'Corporate Meeting', 'Informal Get together',
                       'Conference', 'Seminar', 'Award shows and competition', 'Charity event',)
lf2_entry.current(0)
lf2_entry.grid(row=1, column=1)

lf3 = Label(lf, text='Budget for the event', font=(
    "times new roman", 12, "bold"), padx=2, pady=6)
lf3.grid(row=2, column=0)

lf3_entry = Entry(lf, font=("times new roman", 12, "bold"),
                  width=35, textvariable=budget)
lf3_entry.grid(row=2, column=1)

lf4 = Label(lf, text='Event manager', font=(
    "times new roman", 12, "bold"), padx=2, pady=6)
lf4.grid(row=3, column=0)

lf4_entry = ttk.Combobox(
    lf, font=("times new roman", 12, "bold"), width=33, state='readonly', textvariable=manager)
lf4_entry["values"] = ("", "Spartacus Edmundo",
                       "Maram Balder", "Husam Mirosław")
lf4_entry.current(0)
lf4_entry.grid(row=3, column=1)

lf5 = Label(lf, text='Date of the event', font=(
    "times new roman", 12, "bold"), padx=2, pady=6)
lf5.grid(row=4, column=0)

lf5_entry = Entry(lf, font=("times new roman", 12, "bold"),
                  width=35, textvariable=date)
lf5_entry.grid(row=4, column=1)

lf6 = Label(lf, text='Location of the event', font=(
    "times new roman", 12, "bold"), padx=2, pady=6)
lf6.grid(row=5, column=0)

lf6_entry = Entry(lf, font=("times new roman", 12, "bold"),
                  textvariable=location, width=35)
lf6_entry.grid(row=5, column=1)

rf = LabelFrame(f1, bd=10, relief=RIDGE, text='Details overview',
                padx=10, font=("times new roman", 12, "bold"))
rf.place(x=510, y=5, width=350, height=250)

rt1 = Text(rf, font=("times new roman", 12, "bold"),
           width=38, height=10, padx=2, pady=6)
rt1.grid(row=0, column=0)

f2 = Frame(screen5, bd=20, relief=RIDGE)
f2.place(x=0, y=435, width=900, height=100)

f2_button1 = Button(f2, text="Enter the data", font=(
    "times new roman", 12, "bold"), command=enter, width=22, height=2, padx=2, pady=6)
f2_button1.grid(row=0, column=0)

f2_button2 = f2_button1 = Button(f2, text="Delete data", font=(
    "times new roman", 12, "bold"), command=reset, width=22, height=2, padx=2, pady=6)
f2_button2.grid(row=0, column=1)

f2_button3 = f2_button1 = Button(f2, text="Data overview", font=(
    "times new roman", 12, "bold"), command=overview, width=23, height=2, padx=2, pady=6)
f2_button3.grid(row=0, column=2)

f2_button4 = Button(f2, text="Exit", font=(
    "times new roman", 12, "bold"), command=exit, width=23, height=2, padx=2, pady=6)
f2_button4.grid(row=0, column=3)

screen5.mainloop()
