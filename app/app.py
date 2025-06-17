import tools.venmo_tools as venmo_tools
import tools.json_tools as json_tools

import app.newMassRequest as newMassRequest
import app.defaultRequest as defaultRequest
import app.records as records

import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        #Tkinter Initialization
        tk.Tk.__init__(self)
        self.title('Colin\'s Venmo Tools')
        self.geometry("1200x650")

        #Initialize with settings
        self.settings = json_tools.load_all()
        self.remember = json_tools.load_setting('remember')

        #Login Window
        if not self.remember:
            self.withdraw()
            self.open_window(loginWindow)
        else:
            self.token = json_tools.load_setting('token')
            self.client, self.token = venmo_tools.login('', '', self.token)
            self.build()
        
        #Asking confirmation to close without logging out
        def disable_event():
            if messagebox.askokcancel('Still Logged In', 'Are you sure you want to quit? (You have not logged out)', icon='warning'):
                self.destroy()
        self.protocol("WM_DELETE_WINDOW", disable_event)

    def build(self):
        # Redact toggle (top right corner)
        self.redact_var = tk.BooleanVar(value=True)
        redact_check = tk.Checkbutton(
            self,
            text="Redact",
            variable=self.redact_var,
            command=self.refresh_all,
            background='blue',  # change this to your preferred color
            foreground='white', # optional: make text stand out
            activebackground='blue',
            activeforeground='white',
            selectcolor='black'  # checkbox checkmark background
        )
        redact_check.grid(row=0, column=2, sticky='ne', padx=8, pady=8)


        # Left Column Frame (Actions)
        left_frame = tk.Frame(self, background='green')
        tk.Label(left_frame, text='Actions:', background='green').pack()
        tk.Button(left_frame, text="New Mass Request", command=lambda: self.open_window(newMassRequest.mainWindow)).pack(fill='both')
        tk.Button(left_frame, text='Default Month Request', command=lambda: self.open_window(defaultRequest.mainWindow)).pack(fill='both')
        tk.Button(left_frame, text='Records', command=lambda: self.open_window(records.mainWindow)).pack(fill='both')
        tk.Button(left_frame, text='Logout', command=lambda: self.logout()).pack(fill='both')

        # Middle Column Frame (Transactions)
        middle_frame = tk.Frame(self, background='purple')
        tk.Label(middle_frame, text='Transactions:', background='purple').pack()
        self.transactions_box = tk.Listbox(middle_frame, height=200, width=400)
        self.transactions_box.pack()

        # Right Column Frame (Pending)
        right_frame = tk.Frame(self, background='blue')
        tk.Label(right_frame, text='Pending:', background='blue').pack()
        self.pending_box = tk.Listbox(right_frame, height=200, width=400)
        self.pending_box.pack()

        # Place column frames
        left_frame.grid(row=1, column=0, sticky='nw')
        middle_frame.grid(row=1, column=1, sticky='n')
        right_frame.grid(row=1, column=2, sticky='ne')
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)

        # Initial population
        self.refresh_all()


    def refresh_transactions(self):
        self.transactions_box.delete(0, tk.END)
        redact = self.redact_var.get()
        for entry in venmo_tools.getTransactions(redact=redact):
            self.transactions_box.insert(tk.END, entry)

    def refresh_all(self):
        redact = self.redact_var.get()

        # Transactions
        self.transactions_box.delete(0, tk.END)
        for entry in venmo_tools.getTransactions(redact=redact):
            self.transactions_box.insert(tk.END, entry)

        # Pending (for now, mock or replace with actual logic)
        self.pending_box.delete(0, tk.END)
        if redact:
            for _ in range(10):
                self.pending_box.insert(tk.END, "*****")
        else:
            for i in range(10):
                self.pending_box.insert(tk.END, f"Pending transaction {i}")


    #Opens a new Window
    def open_window(self, window_class):
        new_window = window_class(self)
    
    #Logs out and Closes Window
    def logout(self):
        venmo_tools.logout()
        json_tools.write('remember', False)
        self.quit()

#=============================Login Window===============================

class loginWindow(tk.Toplevel):
    def __init__(self, master) -> None:
        tk.Toplevel.__init__(self, master)
        self.master = master
        self.title("Login")
        self.geometry("200x210")
        self.configure(background='black')

        #Disabling Killing Window
        def disable_event():
            pass
        self.protocol("WM_DELETE_WINDOW", disable_event)
        
        #Configure Remember Status
        self.remember = tk.BooleanVar()
        self.token = json_tools.load_setting('token')
        
        usernameLabel = tk.Label(self, text='Username:', background='black')
        self.usernameEntry = tk.Entry(self)
        passwordLabel = tk.Label(self, text='Password:', background='black')
        self.passwordEntry = tk.Entry(self, show='*')
        rememberCheck = tk.Checkbutton(self, text='Remember Me', variable=self.remember, background='black')
        loginButton = tk.Button(self, text='Login', command=lambda: self.onClick())
        
        #Packing
        usernameLabel.pack()
        self.usernameEntry.pack()
        passwordLabel.pack()
        self.passwordEntry.pack()
        rememberCheck.pack()
        loginButton.pack()

    def onClick(self):
        try:
            self.master.client, self.master.token = venmo_tools.login(self.usernameEntry.get(), self.passwordEntry.get(), self.token)
            if self.remember.get():
                json_tools.write('remember', True)
            self.destroy()
            self.master.build()
            self.master.title(f"Venmo Tools: {self.master.client.user.get_my_profile().username}")
            self.master.deiconify()
        except:
            msg = 'Invalid Username or Password'
            tk.messagebox.showerror(title='Login Error', message=msg)