import tkinter as tk
from tkinter import messagebox, simpledialog, font, filedialog
from ttkthemes import ThemedTk
import webbrowser
import datetime
from PIL import Image, ImageTk

class BBM_GUI(tk.Tk):

    def __init__(self, bank_manager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bank_manager = bank_manager
        self.title("Bionic BankManager")
        self.geometry("1600x1200")
        self.configure(bg="white")
        self.title_font = font.Font(family="Arial", size=18, weight="bold")
        self.button_font = font.Font(family="Arial", size=12, weight="bold")
        self.initialize_ui()



    def initialize_ui(self):
        # Split the current date and time
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        # Display the current date on the upper left
        date_label = tk.Label(self, text=current_date, font=("Courier", 12, "bold"), bg="white", fg="black")
        date_label.place(relx=0.01, rely=0.01, anchor=tk.NW)

        # Display the current time just below the date
        time_label = tk.Label(self, text=current_time, font=("Courier", 12, "bold"), bg="white", fg="black")
        time_label.place(relx=0.01, rely=0.04, anchor=tk.NW)

        # Display Location, Employer Name, and Employer ID on the upper right
        location_label = tk.Label(self, text="Location: Canada", font=("Courier", 12, "bold"), bg="white", fg="black")
        location_label.place(relx=0.99, rely=0.01, anchor=tk.NE)

        employer_name_label = tk.Label(self, text="Employer Name: Server Admin", font=("Courier", 12, "bold"), bg="white", fg="black")
        employer_name_label.place(relx=0.99, rely=0.04, anchor=tk.NE)

        employer_id_label = tk.Label(self, text="Employer ID: 0", font=("Courier", 12, "bold"), bg="white", fg="black")
        employer_id_label.place(relx=0.99, rely=0.07, anchor=tk.NE)

        # Adjust the title font and display it
        self.title_font = font.Font(font=("Courier", 18, "bold"), size=18, weight="bold")

        menu_label = tk.Label(self, text="★ Welcome to Bionic BankManager ★", font=self.title_font, bg="white", fg="blue")
        menu_label.pack(pady=20)

        button_frame = tk.Frame(self, bg="white")
        button_frame.place(relx=0.5, rely=0.4, anchor='center')  # Place frame in the center of the screen

        button_style = {"font": self.button_font, "bg": "#D3D3D3", "fg": "#333333", "padx": 20, "pady": 10}
        btn_create_account = tk.Button(button_frame, text="Create Account", command=self.create_account, **button_style)
        btn_create_account.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W + tk.E)

        # ... [Rest of the button definitions and the rest of the code]


        btn_create_account = tk.Button(button_frame, text="Create Account", command=self.create_account, **button_style)
        btn_create_account.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W + tk.E)

        btn_deposit_money = tk.Button(button_frame, text="Deposit Money", command=self.deposit_money, **button_style)
        btn_deposit_money.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W + tk.E)

        btn_withdraw_money = tk.Button(button_frame, text="Withdraw Money", command=self.withdraw_money, **button_style)
        btn_withdraw_money.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W + tk.E)

        btn_view_info1 = tk.Button(button_frame, text="Account ID Info", command=self.view_info, **button_style)
        btn_view_info1.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W + tk.E)

        btn_transfer_money = tk.Button(button_frame, text="Transfer Money", command=self.transfer_money, **button_style)
        btn_transfer_money.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W + tk.E)

        btn_view_info2 = tk.Button(button_frame, text="HolderName Info", command=self.view_info_by_name, **button_style)
        btn_view_info2.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W + tk.E)

        btn_view_all_accounts = tk.Button(button_frame, text="View All Accounts", command=self.view_all_accounts, **button_style)
        btn_view_all_accounts.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W + tk.E)

        btn_exit = tk.Button(button_frame, text="Exit", command=self.destroy, **button_style)
        btn_exit.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W + tk.E)

        buttons = [btn_create_account, btn_deposit_money, btn_withdraw_money, btn_view_info1, btn_transfer_money, btn_view_info2, btn_exit, btn_view_all_accounts]
        for button in buttons:
            button.bind("<Enter>", self.on_enter)
            button.bind("<Leave>", self.on_leave)

        # Load and place the image
        image_path = "logo.png"  # Replace with the path to your image
        original_image = Image.open(image_path)
        resized_image = original_image.resize((250, 250))
        img = ImageTk.PhotoImage(resized_image)
        img_label = tk.Label(self, image=img, bg="white")
        img_label.image = img
        img_label.place(relx=0.5, rely=0.8, anchor='center')

        # Event binding for the image to open a link when clicked
        img_label.bind("<Button-1>", self.open_link)

        # Event binding for the image to open a link when clicked
        img_label.bind("<Button-1>", self.open_link)

        # Add footer
        footer_label_text = "⚡ -Developed by CollectorsObservatory using AI- ⚡"
        footer_label = tk.Label(self, text=footer_label_text, font=("Arial", 14, "bold"), bg="white", fg="#333333")
        footer_label.pack(side=tk.BOTTOM, pady=5)

        # Binding the hover and click events for the footer
        footer_label.bind("<Enter>", self.footer_on_enter)
        footer_label.bind("<Leave>", self.footer_on_leave)
        footer_label.bind("<Button-1>", self.open_link)

    # ... [Rest of your methods, like on_enter, on_leave, create_account, etc.]


        
    def on_enter(self, e):
        e.widget['background'] = 'blue'  # Blue color
        e.widget['fg'] = 'blue'  # White text for contrast

    def on_leave(self, e):
        e.widget['background'] = '#D3D3D3'  # LightGray color
        e.widget['fg'] = '#333333'  # Dark gray text

    # ... [Your other methods like create_account, deposit_money, etc.]

    def footer_on_enter(self, e):
        e.widget['fg'] = '#8a2be2'  # Purple color for hover

    def footer_on_leave(self, e):
        e.widget['fg'] = '#333333'  # Original color

    def open_link(self, event):
        webbrowser.open("https://github.com/CollectorsObservatory")


    def create_account(self):
        holder_name = simpledialog.askstring("Input", "Enter your full name:")
        gender = simpledialog.askstring("Input", "Enter your gender (M/F):")
        balance = simpledialog.askfloat("Input", "Enter your initial deposit in $:")

        if holder_name and gender and balance:
            account_number = self.bank_manager.create_account(holder_name, gender, balance)
            messagebox.showinfo("Success", f"Account created! Your account number is {account_number}.")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def deposit_money(self):
        account_number = simpledialog.askinteger("Input", "Enter your account number:")
        amount = simpledialog.askfloat("Input", "Enter the amount to deposit in $:")

        if account_number and amount:
            if self.bank_manager.deposit_money(account_number, amount):
                messagebox.showinfo("Success", f"${amount} $ has been deposited to your account.")
            else:
                messagebox.showwarning("Error", "Account not found or invalid amount!")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def withdraw_money(self):
        account_number = simpledialog.askinteger("Input", "Enter your account number:")
        amount = simpledialog.askfloat("Input", "Enter the amount to withdraw $:")

        if account_number and amount:
            if self.bank_manager.withdraw_money(account_number, amount):
                messagebox.showinfo("Success", f"${amount} $ has been withdrawn from your account.")
            else:
                messagebox.showwarning("Error", "Insufficient funds or account not found!")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def view_info(self):
        account_number = simpledialog.askinteger("Input", "Enter your account number:")

        if account_number:
            info = self.bank_manager.get_account_info(account_number)
            if info:
                messagebox.showinfo("Account Info", f"Name: {info['name']}\nBalance: ${info['balance']}")
            else:
                messagebox.showwarning("Error", "Account not found!")
        else:
            messagebox.showwarning("Input Error", "Account number is required!")
    def view_info_by_name(self):
        holder_name = simpledialog.askstring("Input", "Enter the holder's full name:")

        if holder_name:
          info = self.bank_manager.get_account_info_by_name(holder_name)
        if info:
            messagebox.showinfo("Account Info", f"Holder's Name: {info['name']}\nGender: {info['gender']}\nAccount Number: {info['account_number']}\nBalance: ${info['balance']}")
        else:
            messagebox.showwarning("Error", "Account not found!")
    def transfer_money(self):
        from_account = simpledialog.askinteger("Input", "Enter your account number (from):")
        to_account = simpledialog.askinteger("Input", "Enter the recipient's account number (to):")
        amount = simpledialog.askfloat("Input", "Enter the amount to transfer:")

        if from_account and to_account and amount:
            # Check if both accounts exist
            if from_account in self.bank_manager.client_info and to_account in self.bank_manager.client_info:
                # Check if 'from_account' has enough balance
                if self.bank_manager.client_info[from_account]['balance'] >= amount:
                    # Deduct from 'from_account' and add to 'to_account'
                    self.bank_manager.client_info[from_account]['balance'] -= amount
                    self.bank_manager.client_info[to_account]['balance'] += amount
                    self.bank_manager.save_accounts()
                    messagebox.showinfo("Success", f"Transferred ${amount} from account {from_account} to {to_account}.")
                else:
                    messagebox.showwarning("Error", "Insufficient funds!")
            else:
                messagebox.showwarning("Error", "One or both account numbers are invalid!")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")
    def view_all_accounts(self):
        """Method to display data from accounts.txt"""
        with open("accounts.txt", "r") as file:
            accounts_data = file.read()
        # Display the data in a top-level window (or any other way you want)
        view_accounts_window = tk.Toplevel(self)
        view_accounts_window.title("All Accounts")
        view_accounts_window.geometry("600x400")

        text_area = tk.Text(view_accounts_window, wrap=tk.WORD)
        text_area.insert(tk.END, accounts_data)
        text_area.pack(expand=True, fill=tk.BOTH)

        close_button = tk.Button(view_accounts_window, text="Close", command=view_accounts_window.destroy)
        close_button.pack(pady=10)
    def footer_on_enter(self, e):
            e.widget['fg'] = '#8a2be2'  # Purple color for hover
    

    def footer_on_leave(self, e):
      e.widget['fg'] = '#333333'  # Original color


    def open_link(self, event):
        webbrowser.open("https://github.com/CollectorsObservatory") 

# Instantiate and run the main loop
if __name__ == "__main__":
    app = BBM_GUI(None)  # Pass in the bank manager instance here
    app.mainloop()
    
    