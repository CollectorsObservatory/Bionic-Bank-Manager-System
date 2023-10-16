import random
import os

from BBM_G import BBM_GUI  # Ensure this import works, based on your directory structure


class BionicBankManager:
    def __init__(self):
        self.accounts_file = "accounts.txt"
        self.client_info = {}  # Key: account number, Value: {'name': name, 'gender': gender, 'balance': balance}
        self.load_accounts()

    def load_accounts(self):
        if os.path.exists(self.accounts_file):
            with open(self.accounts_file, "r") as file:
                lines = file.readlines()

            for line in lines[3::4]:  # Skip header and start from the actual data, skipping empty lines
                try:
                    data = line.strip().split()
                    holder_name = " ".join(
                        data[:-2])  # Extracting name parts, except the last two items (balance and account number)
                    balance = float(data[-2])  # The second to the last item is balance
                    account_number = int(data[-1])  # The last item is account number
                    self.client_info[account_number] = {'name': holder_name, 'gender': 'U',
                                                        'balance': balance}  # 'U' for unknown gender
                except ValueError as e:
                    print(f"Skipping invalid data: {line.strip()}, error: {e}")
                except IndexError as e:
                    print(f"Data format error in line {line.strip()}, error: {e}")

    def save_accounts(self):
        with open(self.accounts_file, "w") as file:
            for account_number, info in self.client_info.items():
                file.write(f"{account_number} | {info['name']} | {info['gender']} | {info['balance']}\n")

    def create_account(self, holder_name, gender, balance):
        account_number = random.randint(10**11, 10**12 - 1)
        self.client_info[account_number] = {'name': holder_name, 'gender': gender, 'balance': balance}
        self.save_accounts()
        return account_number

    def deposit_money(self, account_number, amount):
        if account_number in self.client_info:
            self.client_info[account_number]['balance'] += amount
            self.save_accounts()
            return True
        else:
            return False

    def withdraw_money(self, account_number, amount):
        if account_number in self.client_info and self.client_info[account_number]['balance'] >= amount:
            self.client_info[account_number]['balance'] -= amount
            self.save_accounts()
            return True
        else:
            return False

    def get_account_info(self, account_number):
        return self.client_info.get(account_number, None)


if __name__ == "__main__":
    bank_manager = BionicBankManager()
    gui = BBM_GUI(bank_manager)
    gui.mainloop()
