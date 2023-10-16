import random
import names

# Open the file with write permission
with open('accounts.txt', 'w') as file:
    file.write(f'Holdername  |  Account balance | Account number\n')
    file.write("\n")
    

    # Generate 100 random names and balances
    for _ in range(1000):
        # Generate a random full name
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        full_name = f'{first_name} {last_name}'

        # Generate a random balance
        balance = round(random.uniform(0, 10000), 2)
        bank_account_number = random.randint(111111111111,999999999999)

        # Write the full name and balance to the file
        file.write("  \n")
        file.write(f'{full_name} {balance} {bank_account_number}\n')
        file.write("  \n")
        

print("File created with 1000 random names and balances.")
print("Yeah buddy , light weight")  # Success message

