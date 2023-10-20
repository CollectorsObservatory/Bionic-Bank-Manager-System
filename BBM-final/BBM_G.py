import tkinter as tk
from tkinter import messagebox, simpledialog, font, filedialog
from ttkthemes import ThemedTk
import webbrowser
import datetime
from PIL import Image, ImageTk
from ICE import currency_iso_codes,available_currencies,currencies_rates_buy,currencies_rates_sell
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg






class BBM_GUI(tk.Tk):

    def __init__(self, bank_manager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bank_manager = bank_manager
        self.title("Bionic Banking Software")
        self.geometry("1000x800")
        self.configure(bg="white")
        self.title_font = font.Font(family="Sans Serif", size=18, weight="bold")
        self.button_font = font.Font(family="Sans Serif", size=12, weight="bold")
        self.initialize_ui()
    



    def initialize_ui(self):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        # Display the current date on the upper left
        date_label = tk.Label(self, text=current_date, font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        date_label.place(relx=0.01, rely=0.01, anchor=tk.NW)

        # Display the current time just below the date
        time_label = tk.Label(self, text=current_time, font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        time_label.place(relx=0.01, rely=0.04, anchor=tk.NW)

        # Display Location, Employer Name, and Employer ID on the upper right
        location_label = tk.Label(self, text="Location: Canada", font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        location_label.place(relx=0.99, rely=0.01, anchor=tk.NE)

        employer_name_label = tk.Label(self, text="Employer Name: Server Admin", font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        employer_name_label.place(relx=0.99, rely=0.04, anchor=tk.NE)

        employer_id_label = tk.Label(self, text="Employer ID: 0", font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        employer_id_label.place(relx=0.99, rely=0.07, anchor=tk.NE)

        # Adjust the title font and display it
        self.title_font = font.Font(font=("Sans Serif", 23, "bold"), size=20, weight="bold")

        menu_label = tk.Label(self, text="🌐 Logged in:  Bionic Banking Software 🌐", font=self.title_font, bg="white", fg="black")
        menu_label.pack(pady=15)

        button_frame = tk.Frame(self, bg="white")
        button_frame.place(relx=0.5, rely=0.4, anchor='center')  

        button_style = {"font": self.button_font, "bg": "#D3D3D3", "fg": "#333333", "padx": 20, "pady": 10}
        btn_create_account = tk.Button(button_frame, text="Create Account", command=self.create_account, **button_style)
        btn_create_account.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W + tk.E)

      


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
        
        btn_currency_exchange = tk.Button(button_frame, text="Currency Exchange", command=self.currency_exchange, **button_style)
        btn_currency_exchange.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W + tk.E)
        buttons = [btn_create_account, btn_deposit_money, btn_withdraw_money, btn_view_info1, btn_transfer_money, btn_view_info2, btn_exit, btn_view_all_accounts, btn_currency_exchange]
        for button in buttons:
            button.bind("<Enter>", self.on_enter)
            button.bind("<Leave>", self.on_leave)

      
        image_path = "fin1.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((256, 256), Image.LANCZOS)  
        img = ImageTk.PhotoImage(resized_image)
        img_label = tk.Label(self, image=img, bg='white')
        img_label.image = img
        img_label.place(relx=0.5, rely=0.75, anchor='center')


       
        img_label.bind("<Button-1>", self.open_link)

      
        img_label.bind("<Button-1>", self.open_link)

        # Add footer
        footer_label_text = "⚡ -By CollectorsObservatory under Collosus Software- ⚡"
        footer_label = tk.Label(self, text=footer_label_text, font=("Sans serif", 15, "bold"), bg="white", fg="#333333")
        footer_label.pack(side=tk.BOTTOM, pady=5)

        
        footer_label.bind("<Enter>", self.footer_on_enter)
        footer_label.bind("<Leave>", self.footer_on_leave)
        footer_label.bind("<Button-1>", self.open_link)

    


        
    def on_enter(self, e):
        e.widget['background'] = 'blue'  # Blue color
        e.widget['fg'] = 'blue'  # White text for contrast

    def on_leave(self, e):
        e.widget['background'] = '#D3D3D3'  # LightGray color
        e.widget['fg'] = '#333333'  # Dark gray text

    

    def footer_on_enter(self, e):
        e.widget['fg'] = '#8a2be2'  

    def footer_on_leave(self, e):
        e.widget['fg'] = '#333333'  

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
            messagebox.showwarning("Error", "All fields are required!")

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
            messagebox.showwarning("Error", "All fields are required!")
    def view_all_accounts(self):
        """Method to display data from accounts.txt"""
        with open("accounts.txt", "r") as file:
            accounts_data = file.read()

        view_accounts_window = tk.Toplevel(self)
        view_accounts_window.title("All Accounts")
        view_accounts_window.geometry("600x600")

        text_area = tk.Text(view_accounts_window, wrap=tk.WORD)
        text_area.insert(tk.END, accounts_data)
        text_area.pack(expand=True, fill=tk.BOTH)

        close_button = tk.Button(view_accounts_window, text="Close", command=view_accounts_window.destroy)
        close_button.pack(pady=10)
    def currency_exchange(self):
         exchange_window = tk.Toplevel(self)
       
         exchange_window.title("Bionic Currency Exchange")
         exchange_window.geometry("1000x800")
         exchange_window.configure(bg="white")

         title_label = tk.Label(exchange_window, text="★ Bionic Currency Exchange ★", font=self.title_font, bg="white", fg="blue")
         title_label.pack(pady=20)

         frame = tk.Frame(exchange_window, bg="white")
         frame.pack(pady=20)

         country_label = tk.Label(frame, text="Enter country name:", font=self.button_font, bg="white", fg="black")
         country_label.grid(row=0, column=0, padx=10, pady=10)

         country_entry = tk.Entry(frame, font=self.button_font)
         country_entry.grid(row=0, column=1, padx=10, pady=10)

         amount_label = tk.Label(frame, text="Enter amount:", font=self.button_font, bg="white", fg="black")
         amount_label.grid(row=1, column=0, padx=10, pady=10)
         self.result_label = tk.Label(exchange_window, text="", font=("Arial", 14), bg="white", fg="black")
         self.result_label.pack(pady=20)

         amount_entry = tk.Entry(frame, font=self.button_font)
         amount_entry.grid(row=1, column=1, padx=10, pady=10)
         

         buy_sell_label = tk.Label(frame, text="Buy (B) or Sell (S):", font=self.button_font, bg="white", fg="black")
         buy_sell_label.grid(row=2, column=0, padx=10, pady=10)

         buy_sell_var = tk.StringVar(value="B")
         buy_radiobutton = tk.Radiobutton(frame, text="Buy", variable=buy_sell_var, value="B", font=self.button_font, bg="white")
         sell_radiobutton = tk.Radiobutton(frame, text="Sell", variable=buy_sell_var, value="S", font=self.button_font, bg="white")
         buy_radiobutton.grid(row=2, column=1, padx=10, pady=10)
         sell_radiobutton.grid(row=2, column=2, padx=10, pady=10)

         convert_button = tk.Button(frame, text="Convert", command=lambda: self.confirm_transaction(
         exchange_window, country_entry.get(), amount_entry.get(), buy_sell_var.get()), font=self.button_font, bg="#D3D3D3", fg="black", padx=20, pady=10)
         convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

         result_label = tk.Label(exchange_window, text="", font=("Arial", 14), bg="white", fg="black")
         result_label.pack(pady=20)
         calc_button = tk.Button(frame, text="Calculator", 
                            command=self.launch_calculator, 
                            font=self.button_font, 
                            bg="#D3D3D3", 
                            fg="black", 
                            padx=20, 
                            pady=10)
         calc_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
         plot_button = tk.Button(frame, text="Plot Functions", 
                                command=self.plot_function, 
                                font=self.button_font, 
                                bg="#D3D3D3", 
                                fg="black", 
                                padx=20, 
                                pady=10)
         plot_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
         

         
         
    def confirm_transaction(self, exchange_window, country, amount, buy_or_sell):
        user_input = country.lower()
        detected_country = self.detect_country(user_input)

        # If a country is detected, use it as the ISO code; otherwise, use the input as-is
        if detected_country:
            country = detected_country
        else:
            country = user_input

        # Check if the entered country is valid (in currency_iso_codes)
        if country in currency_iso_codes:
            exchange_rate = currencies_rates_buy.get(country) if buy_or_sell == "B" else currencies_rates_sell.get(country)
            if exchange_rate:
                try:
                    amount = float(amount)
                    converted_amount = amount * exchange_rate
                    iso_code = currency_iso_codes[country]

                    confirmation_message = f"You entered {amount} {iso_code} for {buy_or_sell}. " \
                                          f"Conversion result: {converted_amount:.2f} CAD\n\n" \
                                          f"Do you want to confirm this transaction?"

                    confirmation_result = messagebox.askyesno("Confirmation", confirmation_message)

                    if confirmation_result:
                        transaction_message = f"Transaction done. {amount} {iso_code} converted to {converted_amount:.2f} CAD.\n THANK YOU !"
                    else:
                        transaction_message = "Transaction canceled."

                    self.result_label.config(text=transaction_message)
                except ValueError:
                    self.result_label.config(text="Invalid amount. Please enter a valid number.")
            else:
                self.result_label.config(text="Exchange rate not found for the given country.")
        else:
            self.result_label.config(text="Country not found in the database.")

    def detect_country(self, input_text):
        for country in available_currencies:
            if country.startswith(input_text):
                return country
        return None
    def launch_calculator(self):
        calculator_window = tk.Toplevel(self)
        calculator_window.title("Bionic Calculator")

        expression_entry = tk.Entry(calculator_window, width=35, borderwidth=5)
        expression_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        def button_click(number):
            current = expression_entry.get()
            expression_entry.delete(0, tk.END)
            expression_entry.insert(0, str(current) + str(number))

        def button_clear():
            expression_entry.delete(0, tk.END)

        def button_equal():
            expression = expression_entry.get()
            try:
                expression_entry.delete(0, tk.END)
                expression_entry.insert(0, str(eval(expression)))
            except:
                expression_entry.delete(0, tk.END)
                expression_entry.insert(0, "Error")


        buttons = []
        for i in range(9, -1, -1):
            button = tk.Button(calculator_window, text=str(i), padx=40, pady=20, command=lambda i=i: button_click(i))
            buttons.append(button)

        equal_button = tk.Button(calculator_window, text="=", padx=40, pady=20, command=button_equal)
        clear_button = tk.Button(calculator_window, text="Clear", padx=30, pady=20, command=button_clear)

    
        row_vals = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        col_vals = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        for i, button in enumerate(buttons[:9]):
            button.grid(row=row_vals[i], column=col_vals[i])

        buttons[9].grid(row=4, column=1)
        clear_button.grid(row=4, column=0)
        equal_button.grid(row=4, column=2)
    def plot_function(self):
        plot_window = tk.Toplevel(self)
        plot_window.title("Plot Function")
        plot_window.configure(bg="white")

        label = tk.Label(plot_window, text="Enter a function of x to plot (use 'x' as the variable):", bg="white")
        label.pack(padx=10, pady=5)

        entry = tk.Entry(plot_window)
        entry.pack(padx=10, pady=5)

        plot_button = tk.Button(plot_window, text="Plot", command=lambda: self.create_plot(entry.get()))
        plot_button.pack(padx=10, pady=5)

    def create_plot(self, func_str):
        try:
            
            func_str = func_str.replace('^', '**')
            x = np.linspace(-10, 10, 400)
            y = eval(func_str)

          
            plot_result_window = tk.Toplevel(self)
            plot_result_window.title("Function Plot")
            plot_result_window.configure(bg="white")

         
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.set(xlabel='x', ylabel='y', title='y = ' + func_str)

            
            canvas = FigureCanvasTkAgg(fig, master=plot_result_window)  
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        except Exception as e:
            tk.messagebox.showerror("Error", "Invalid function format or syntax error in the function.")



def footer_on_enter(self, e):
    e.widget['fg'] = '#8a2be2'  # Purple color for hover

def footer_on_leave(self, e):
    e.widget['fg'] = '#333333'  # Original color

def open_link(self, event):
    webbrowser.open("https://github.com/CollectorsObservatory") 




    
