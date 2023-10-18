import random
import names

# Open the file with write permission
with open('accounts.txt', 'w') as file:
    # Define header
    file.write('Account number | Holdername | Gender | Account balance\n')
    file.write('-' * 60 + '\n')  # Just to separate the header from the data
    
    # Generate 1000 random names, genders, and balances
    for _ in range(1000):
        # Generate a random full name
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        full_name = f'{first_name} {last_name}'
        
        # Randomly assign gender (you can improve this if needed)
        gender = random.choice(['m', 'f', 'o'])  # 'm' for male, 'f' for female, 'o' for other

        # Generate a random balance
        balance = round(random.uniform(0, 10000), 2)

        # Generate a random bank account number
        bank_account_number = random.randint(111111111111, 999999999999)

        # Write the data in the desired format
        file.write(f'{bank_account_number} | {full_name} | {gender} | {balance}\n')

print("File created with 1000 random names, genders, and balances.")
print("Yeah buddy, light weight!")  # Success message
