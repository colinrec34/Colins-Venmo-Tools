import tkinter as tk
from tkinter import messagebox
import tools.venmo_tools as venmo_tools

class mainWindow(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        #Window Settings
        self.title("New Mass Request")
        self.geometry('600x300')

        #Top Level Widgets
        tk.Button(self, text="Send Request", command=lambda: self.onClick()).pack(side="bottom")

        #Left Column Frame
        left_frame = tk.Frame(self, background='blue')
        #Total Amount Entry
        tk.Label(left_frame, text='Enter Total Amount:', background='blue').pack()
        self.totalEntry = tk.Entry(left_frame)
        self.totalEntry.pack()
        #Note Entry
        tk.Label(left_frame, text='Enter Note:', background='blue').pack()
        self.noteEntry = tk.Entry(left_frame)
        self.noteEntry.pack()
        #Include Button
        self.include = tk.BooleanVar()
        tk.Checkbutton(left_frame, text='Include Yourself?', variable=self.include, background='blue').pack()

        left_frame.pack(side='left', fill='y')

        #Right Listbox
        #Defining Elements of Listbox
        usernames = tk.Variable(value=venmo_tools.get_username_list())
        self.list_box = tk.Listbox(self, height=300, width=150, listvariable=usernames, yscrollcommand=True, selectmode=tk.MULTIPLE)
        self.list_box.bind("<<ListboxSelect>>", lambda event: self.itemSelect())
        self.list_box.pack(side='right')
    
    def onClick(self) -> None:
        try:
            totalAmount = float(self.totalEntry.get())
            if totalAmount == float(0):
                raise ValueError
        except:
            msg = 'Please enter a non-zero amount'
            tk.messagebox.showerror(title='Invalid Amount', message=msg)
            return
        try:
            list_boxLength = len(self.list_box.curselection())
        except:
            msg = 'Please enter a message'
            tk.messagebox.showerror(title='Invalid Message', message=msg)
            return

        if self.include.get():
            list_boxLength += 1

        msg = f'You are requesting ${totalAmount/(list_boxLength):.2f} from \n {self.selected_string}'
        if tk.messagebox.askokcancel(title='Confirm', message=msg):
            venmo_tools.requestEqualSplit(float(self.totalEntry.get()), self.noteEntry.get(), usernameList=self.selected_users, include=self.include.get())

    def itemSelect(self) -> None:
        selected_indices = self.list_box.curselection()
        # get selected items
        self.selected_users = [self.list_box.get(i) for i in selected_indices]
        self.selected_string = ",".join(self.selected_users)
        #tk.messagebox.askquestion(title='Information', message=msg)

    def open_window(self, window_class):
        #Opens a new window
        new_window = window_class(self)