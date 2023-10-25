# Bionic Bank Manager

The Bionic Bank Manager is a  banking account management system that allows users to manage  accounts, conduct transactions, monitor  account details, and perform currency conversions.
The final version of this app is in BBM-final folder , all other folders are there just to monitor progress.

## Main Features

1. **Account Loading**: At startup, the system loads account information from an `accounts.txt` file.
2. **Account Creation**: Users can create a new account.
3. **Money Deposit**: Users can deposit money into their accounts.
4. **Money Withdrawal**: Users can withdraw money from their accounts.
5. **Money Transfer**: Allows for money transfers between two accounts.
6. **Account Information Retrieval**: Users can fetch details of a specific account.
7. **Currency Conversion**: Users can convert amounts between different currencies using real-time exchange rates.
8. **Account Saving**: After each transaction, account information is saved back to the `accounts.txt` file.

## Technical Details

### Classes

- **BionicBankManager**: This is the core of the system managing all account-related functionalities.

### Main Methods

- `load_accounts()`: Loads account information from the `accounts.txt` file.
- `create_account(holder_name, gender, balance)`: Creates a new account.
- `save_accounts()`: Saves account information back to the `accounts.txt` file.
- `deposit_money(account_number, amount)`: Allows for money deposits.
- `withdraw_money(account_number, amount)`: Allows for money withdrawals.
- `transfer_money(from_account, to_account, amount)`: Handles money transfers between accounts.
- `convert_currency(account_number, target_currency, amount)`: Converts the specified amount into the target currency.
- `get_account_info(account_number)`: Returns information about a specific account.

### Starting the Program

The program can be started by running the BBM.py file. A graphical user interface, `BBM_GUI`, is utilized to interact with the `BionicBankManager`.
