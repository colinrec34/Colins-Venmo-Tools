import tkinter as tk
from tkinter import messagebox
import tools.venmo_tools as venmo_tools

class mainWindow(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)

        #Window Settings
        self.title("Default Monthly Request")
        self.geometry('250x100')
        self.configure(bg='blue')

        #Send Request Button
        tk.Button(self, text="Send Request", command=lambda: self.onClick()).pack(side="bottom")

        #Month Name Entry
        tk.Label(self, text='Enter Message Prefix (Month):', background='blue').pack()
        self.monthEntry = tk.Entry(self)
        self.monthEntry.pack()
        #Include Button
        self.include = tk.BooleanVar(value=True)
        tk.Checkbutton(self, text='Include Yourself?', variable=self.include, background='blue').pack()

    def onClick(self) -> None:
        try:
            monthMessage = str(self.monthEntry.get())
            if len(monthMessage) == 0:
                raise ValueError
        except:
            msg = 'Please enter a message prefix'
            tk.messagebox.showerror(title='Invalid', message=msg)
            return
        
        msg = f'You are requesting the roommates for the month of \"{monthMessage}\"'
        if tk.messagebox.askokcancel(title='Confirm', message=msg):
            venmo_tools.monthlyRequest(str(self.monthEntry.get()), include=self.include.get())
            self.destroy()

    def open_window(self, window_class):
        #Opens a new window
        new_window = window_class(self)