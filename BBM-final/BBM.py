import random
import os
from BBM_G import BBM_GUI  

class BionicBankManager:
    def __init__(self):
        self.accounts_file = "accounts.txt"
        self.client_info = {}  
        self.load_accounts()

    def load_accounts(self):
        if os.path.exists(self.accounts_file):
            with open(self.accounts_file, "r") as file:
                lines = file.readlines()

            for line in lines[2:]:
                try:
                    data = line.strip().split('|')
                    account_number = int(data[0].strip())
                    holder_name = data[1].strip()
                    gender = data[2].strip()
                    balance = float(data[3].strip())
                    self.client_info[account_number] = {'name': holder_name, 'gender': gender, 'balance': balance}
                except (ValueError, IndexError) as e:
                    print(f"Skipping invalid data: {line.strip()}, error: {e}")

    def create_account(self, holder_name, gender, balance):
        account_number = random.randint(10**11, 10**12 - 1)
        self.client_info[account_number] = {'name': holder_name, 'gender': gender, 'balance': balance}
        with open(self.accounts_file, "a") as file:
            file.write(f"{account_number} | {holder_name} | {gender} | {balance}\n")
        return account_number

    def save_accounts(self):
        with open(self.accounts_file, "w") as file:
            file.write('Account number | Holdername | Gender | Account balance\n')
            file.write('-' * 60 + '\n')
            for account_number, info in self.client_info.items():
                file.write(f"{account_number} | {info['name']} | {info['gender']} | {info['balance']}\n")

    def deposit_money(self, account_number, amount):
        if account_number in self.client_info:
            self.client_info[account_number]['balance'] += amount
            self.save_accounts()
            return True
        return False

    def withdraw_money(self, account_number, amount):
        if account_number in self.client_info and self.client_info[account_number]['balance'] >= amount:
            self.client_info[account_number]['balance'] -= amount
            self.save_accounts()
            return True
        return False

    def transfer_money(self, from_account, to_account, amount):
        if from_account in self.client_info and to_account in self.client_info:
            if self.client_info[from_account]['balance'] >= amount:
                self.client_info[from_account]['balance'] -= amount
                self.client_info[to_account]['balance'] += amount
                self.save_accounts()
                return True
            else:
                return False
        return False

    def get_account_info(self, account_number):
        return self.client_info.get(account_number, None)

    def get_account_info_by_name(self, holder_name):
        for account_number, info in self.client_info.items():
            if info['name'] == holder_name:
                return {'account_number': account_number, **self.client_info.get(account_number)}
        return None

if __name__ == "__main__":
    bank_manager = BionicBankManager()
    gui = BBM_GUI(bank_manager)
    gui.mainloop()