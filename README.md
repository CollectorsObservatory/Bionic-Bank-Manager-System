# Bionic Bank Manager🏛

The Bionic Bank Manager is a  banking account management system that allows users to manage  accounts, conduct transactions, monitor  account details, and perform currency conversions.
The final version of this app is in BBM-final folder , all other folders are there just to monitor progress.
The web version is supposed to link up to a dist or app version of this code that is still under development.
<img width="993" alt="Screenshot 2023-10-25 at 5 38 29 PM" src="https://github.com/CollectorsObservatory/Bionic-Bank-Manager-System/assets/126903635/dd574698-26bc-4094-bbbc-b932dd4fade2">


## Main Features🚀

1. **Account Loading**: At startup, the system loads account information from an `accounts.txt` file.
2. **Account Creation**: Users can create a new account.
3. **Money Deposit**: Users can deposit money into their accounts.
4. **Money Withdrawal**: Users can withdraw money from their accounts.
5. **Money Transfer**: Allows for money transfers between two accounts.
6. **Account Information Retrieval**: Users can fetch details of a specific account.
7. **Currency Conversion**: Users can convert amounts between different currencies using static rates ( for optimization )
8. **Account Saving**: After each transaction, account information is saved back to the `accounts.txt` file.
9. **Calculator App**: Included in the currency conversion program.
10. **Function plotting app**: Included in the currency conversion program.

## Technical Details🚀

### Classes

- **BionicBankManager**: This is the core of the system managing all account-related functionalities.
- **ForexExchangeGUI**: Manages the exchange function with static rates ( for optimization )
- **BBM_GUI**: The class that manages the graphical part of the program generations buttons and styles etc.
<img width="965" alt="Screenshot 2023-10-25 at 5 39 52 PM" src="https://github.com/CollectorsObservatory/Bionic-Bank-Manager-System/assets/126903635/e4f8b4e4-704c-46d2-ba7d-1f53eb6eb167">
### Main Methods🚀

- `load_accounts()`: Loads all account information from the `accounts.txt` file.
- `create_account(holder_name, gender, balance)`: Creates a new account taking name gender and initial deposit.
- `save_accounts()`: Saves account information back to the `accounts.txt` file(automatically).
- `deposit_money(account_number, amount)`: Allows for money deposits using account number.
- `withdraw_money(account_number, amount)`: Allows for money withdrawals using account number.
- `transfer_money(from_account, to_account, amount)`: Handles money transfers between accounts using account number.
- `convert_currency(account_number, target_currency, amount)`: Converts the specified amount into the target currency.
- `get_account_info(account_number)`: Returns information about a specific account.

### Starting the Program

The program can be started by running the BBM.py file. A graphical user interface, `BBM_GUI`, is utilized to interact with the `BionicBankManager`.
