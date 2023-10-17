import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
import datetime
from PIL import Image, ImageTk

currency_iso_codes = {"united states": "United states Dollar",
                      "japan": "Japanese Yen",
                      "spain": "Euro",
                      "france": "Euro",
                      "europe": "Euro",
                      "germany": "Euro",
                      "italy": "Euro",
                      "mexico": "Mex peso",
                      "Cuba": "Cuban convertible peso",
                      "united kingdom": "Great Britain Pound",
                      "costa rica": "Costa Rica colon",
                      "dominican republic": "DOM peso",
                      "australia": "Australian dollar",
                      "new zealand": "NZ dollar",
                      "switzerland": "swiss franc",
                      "tunisia": "Tunisian Dinar",
                      "morocco": "Moroccan Dirham",
                      "china": "Chinese Yuan",
                      "vietnam": "Vietnam Dong"}

# Define available currencies and their ISO codes
available_currencies = list(currency_iso_codes.keys())
# Define buy and sell rates for each currency
currencies_rates_buy = {"united states": 1.416316,
                        "mexico": 0.080344,
                        "japan": 0.013,
                        "france": 1.518346,
                        "spain": 1.518346,
                        "germany": 1.518346,
                        "italy": 1.518346,
                        "europe": 1.518346,
                        "united kingdom": 1.726182,
                        "costa rica": 0.0023,
                        "dominican republic": 0.023,
                        "australia": 1.039646,
                        "new zealand": 1.101636,
                        "switzerland": 1.525777,
                        "tunisia": 0.479655,
                        "morocco": 0.154211,
                        "china": 0.211689,
                        "vietnam": 0.000068}

currencies_rates_sell = {"united states": 1.333812,
                         "mexico": 0.070118,
                         "japan": 0.012,
                         "spain":  1.427788,
                         "france": 1.427788,
                         "germany": 1.427788,
                         "italy": 1.427788,
                         "europe": 1.427788,
                         "united kingdom": 1.597548,
                         "costa rica": 0.0021,
                         "dominican republic": 0.021,
                         "australia": 0.872762,
                         "new zealand": 1.801696,
                         "switzerland": 1.414677,
                         "tunisia": 0.376634,
                         "morocco": 0.120716,
                         "china": 0.178395,
                         "vietnam": 0.000049}

# Define current balances for each currency for updates and to limit amounts
current_balances = {"united states": 50000,
                    "japan": 9000000,
                    "spain": 9000000,
                    "france": 678007,
                    "germany": 678007,
                    "italy": 678007,
                    "europe": 678007,
                    "united kingdom": 7789,
                    "costa rica": 9000000000,
                    "dominican republic": 7000000,
                    "australia": 3500,
                    "new zealand": 50000,
                    "switzerland": 36000,
                    "tunisia": 12500000,
                    "morocco": 8000000000000000000000,
                    "vietnam": 18800000000,
                    "china": 9000,
                    "mexico": 400000}


class ForexExchangeGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Forex Exchange Program")
        self.geometry("800x600")
        self.configure(bg="white")
        self.title_font = ("Arial", 18, "bold")
        self.button_font = ("Arial", 12, "bold")
        self.initialize_ui()

    def initialize_ui(self):
        self.title("Forex Exchange Program")
        self.geometry("800x600")
        self.configure(bg="white")

        title_label = tk.Label(self, text="★ Forex Exchange Program ★", font=self.title_font, bg="white", fg="blue")
        title_label.pack(pady=20)

        frame = tk.Frame(self, bg="white")
        frame.pack(pady=20)

        country_label = tk.Label(frame, text="Enter country name:", font=self.button_font, bg="white", fg="black")
        country_label.grid(row=0, column=0, padx=10, pady=10)

        self.country_entry = tk.Entry(frame, font=self.button_font)
        self.country_entry.grid(row=0, column=1, padx=10, pady=10)

        amount_label = tk.Label(frame, text="Enter amount:", font=self.button_font, bg="white", fg="black")
        amount_label.grid(row=1, column=0, padx=10, pady=10)

        self.amount_entry = tk.Entry(frame, font=self.button_font)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        buy_sell_label = tk.Label(frame, text="Buy (B) or Sell (S):", font=self.button_font, bg="white", fg="black")
        buy_sell_label.grid(row=2, column=0, padx=10, pady=10)

        self.buy_sell_var = tk.StringVar(value="B")
        buy_radiobutton = tk.Radiobutton(frame, text="Buy", variable=self.buy_sell_var, value="B", font=self.button_font, bg="white")
        sell_radiobutton = tk.Radiobutton(frame, text="Sell", variable=self.buy_sell_var, value="S", font=self.button_font, bg="white")
        buy_radiobutton.grid(row=2, column=1, padx=10, pady=10)
        sell_radiobutton.grid(row=2, column=2, padx=10, pady=10)

        convert_button = tk.Button(frame, text="Convert", command=self.confirm_transaction, font=self.button_font, bg="#D3D3D3", fg="black", padx=20, pady=10)
        convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 14), bg="white", fg="black")
        self.result_label.pack(pady=20)
        footer_label_text = "⚡ -Developed by CollectorsObservatory using AI- ⚡"
        footer_label = tk.Label(self, text=footer_label_text, font=("Arial", 14, "bold"), bg="white", fg="#333333")
        footer_label.pack(side=tk.BOTTOM, pady=5)

    def confirm_transaction(self):
        user_input = self.country_entry.get().lower()
        detected_country = self.detect_country(user_input)
        if detected_country:
            country = detected_country
        else:
            country = user_input

        amount = self.amount_entry.get()
        buy_or_sell = self.buy_sell_var.get()

        if country in currency_iso_codes:
            exchange_rate = currencies_rates_buy[country] if buy_or_sell == "B" else currencies_rates_sell[country]
            try:
                amount = float(amount)
                converted_amount = amount * exchange_rate
                iso_code = currency_iso_codes[country]

                confirmation_message = f"You entered {amount} {iso_code} for {buy_or_sell}. Conversion result: {converted_amount:.2f} CAD\n\nDo you want to confirm this transaction?"
                confirmation_result = messagebox.askyesno("Confirmation", confirmation_message)

                if confirmation_result:
                    transaction_message = "Transaction done."
                else:
                    transaction_message = "Transaction canceled."

                self.result_label.config(text=transaction_message)
            except ValueError:
                self.result_label.config(text="Invalid amount. Please enter a valid number.")
        else:
            self.result_label.config(text="Country not found in the database.")

    def detect_country(self, input_text):
        for country in available_currencies:
            if country.startswith(input_text):
                return country

if __name__ == "__main__":
    app = ForexExchangeGUI()
    app.mainloop()

 
