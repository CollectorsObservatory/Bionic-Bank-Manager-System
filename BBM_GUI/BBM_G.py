import tkinter as tk
from tkinter import messagebox, simpledialog


class BBM_GUI(tk.Tk):

    def __init__(self, bank_manager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bank_manager = bank_manager
        self.title("Bionic BankManager")
        self.geometry("600x400")
        self.initialize_ui()

    def initialize_ui(self):
        menu_label = tk.Label(self, text="Welcome to Bionic BankManager", font=('Arial', 16))
        menu_label.pack(pady=20)

        btn_create_account = tk.Button(self, text="Create Account", command=self.create_account)
        btn_create_account.pack()

        btn_deposit_money = tk.Button(self, text="Deposit Money", command=self.deposit_money)
        btn_deposit_money.pack()

        btn_withdraw_money = tk.Button(self, text="Withdraw Money", command=self.withdraw_money)
        btn_withdraw_money.pack()

        btn_view_info = tk.Button(self, text="View Account Info", command=self.view_info)
        btn_view_info.pack()

        btn_exit = tk.Button(self, text="Exit", command=self.destroy)
        btn_exit.pack()

    def create_account(self):
        holder_name = simpledialog.askstring("Input", "Enter your full name:")
        gender = simpledialog.askstring("Input", "Enter your gender (M/F/O):")
        balance = simpledialog.askfloat("Input", "Enter your initial deposit:")

        if holder_name and gender and balance:
            account_number = self.bank_manager.create_account(holder_name, gender, balance)
            messagebox.showinfo("Success", f"Account created! Your account number is {account_number}.")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def deposit_money(self):
        account_number = simpledialog.askinteger("Input", "Enter your account number:")
        amount = simpledialog.askfloat("Input", "Enter the amount to deposit:")

        if account_number and amount:
            if self.bank_manager.deposit_money(account_number, amount):
                messagebox.showinfo("Success", f"${amount} has been deposited to your account.")
            else:
                messagebox.showwarning("Error", "Account not found or invalid amount!")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def withdraw_money(self):
        account_number = simpledialog.askinteger("Input", "Enter your account number:")
        amount = simpledialog.askfloat("Input", "Enter the amount to withdraw:")

        if account_number and amount:
            if self.bank_manager.withdraw_money(account_number, amount):
                messagebox.showinfo("Success", f"${amount} has been withdrawn from your account.")
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
