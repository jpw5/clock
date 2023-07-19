import time
import sys
import customtkinter as ctk
import tkinter as yk
from tkinter import ttk, messagebox
from time import strftime


def time():
    string = strftime('%H:%M:%S')
    lbl.configure(text=string)
    lbl.after(1000, time)

    if string == '09:34:00 AM':
        exit()


def refresh():
    time()


# creating tkinter window
root = ctk.CTk()
root.title('Clock')
root.geometry('400x200')
root.resizable(False, False)
ctk.set_appearance_mode('dark')

lbl = ctk.CTkLabel(root, font=('Arial', 60, 'bold', 'italic'))
lbl.pack(anchor='center', pady=50)
# button = ctk.CTkButton(root, text='Refresh', command=refresh)
# button.pack()
time()

root.mainloop()
