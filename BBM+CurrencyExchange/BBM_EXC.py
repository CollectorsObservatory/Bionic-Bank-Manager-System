# start of program
# the idea is to replace forex bureaus
# it's like an interaction between a human and a machine

# if the clients inputs a country , we tell him the country's currency
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


def converter_buy_1(currency):
    """ takes a given currency as an input
     the point here is to give a better rate than our competition
     so we take their rate and remove 3% as a discount
     then the function returns the new rate that will be
     used later on in the body of the code"""
    rate_buy = currencies_rates_buy.get(currency)
    bonus_buy = rate_buy - ((rate_buy * 3) / 100)
    new_rate_buy = bonus_buy
    return new_rate_buy


def converter_sell_1(currency):
    rate_sell = currencies_rates_sell.get(currency)
    bonus_sell = rate_sell - ((rate_sell * 3) / 100)
    new_sell_rate = bonus_sell
    return new_sell_rate


print("Welcome to Forex system 2.0")
print("These rates are last updated on April 30th 2023")
# Source of rates is ICE canada
# point of this program is to be more competitive
# i made an endless loop to keep testing without annoyance , it has no direct functionality
while True:
    currency_input = str(input("Enter country name: "))
    country = currency_input.lower()  # to accept all inputs from the user
    if country in currency_iso_codes.keys():  # loops through the keys to check for the currency name
        iso_code = currency_iso_codes.get(country)
        print(f"The currency of {country} is {iso_code}")
        print(f"Our buy rate is {converter_buy_1(country)}")
        print(f"Our sell rate is {converter_sell_1(country)}")
        print(" ")  # just to leave space between the two displayed rates
        print(f"Average Buy rate in our competition  is {currencies_rates_buy.get(country)}")
        print(f"Average Sell rate in our competition  is {currencies_rates_sell.get(country)}")
        print("With us you are saving almost 15 cents on the dollar !")
        print(" ")
        list_of_names = ["brahim", "eleonore", "fares", "chaima", "tayeb", "raja", "amin"]
        input_name = str(input("enter your name: "))
        list_of_names += [input_name]
        final_list_of_names = set(list_of_names)
        if input_name in list_of_names:
            print(f"Hello {input_name}, welcome back")
        elif input_name not in list_of_names:
            print(f"Hello {input_name}, i will assist you today")

        # after knowing the country , currency now the user should choose wether to buy or sell
        question_buy_or_sell = str(
            input(f"Do you want to buy or sell the currency of {currency_input}(B or S and press ⏎): "))
        if question_buy_or_sell == "B" or question_buy_or_sell == "b":  # two conditions to accept all user inputs
            amount = float(input("Please Enter the amount: "))
            available_balances = current_balances.get(country)
            maximum = available_balances * 0.01  # we only sell 1 % of current balance per client
            print(f"You can buy a maximum of {maximum} for {iso_code} per transaction")
            while amount > maximum:  # if the client exceeds the maximum , he has the chance to enter another one
                print("sorry we do not have that in stock")
                print("please try anouther amount")
                amount = float(input("Please Enter the amount: "))
            while amount <= 0:  # the client can only sell us anything greater than 0
                print("You can not buy nothing now, right? ;)")
                print("please try anouther amount")
                amount = float(input("Please Enter the amount: "))
            if amount <= maximum:
                new_amount = amount * converter_buy_1(country)
                print(f"Buying from us {amount} is going to cost you", " %.2f" % new_amount,
                      "in canadian dollars !")
                print(" ")
                print("And by the way , we take no comission fees as the entire system is automatic ;)")
                print("Our competition take between 2 and 5 dollars commission , we don't ;}")
            user_input_2 = str(input(f"Do you want to buy {amount} of {iso_code}? (Yes or no): "))
            available_balances -= amount  # to update the balance
            another_transaction = str(input("Do you want to do another transaction? "))
            if another_transaction == "fazaab13":  # admin option only
                available_balances -= amount  # to update the balance of the currency
                print(available_balances, current_balances)
            if another_transaction == "yes" or another_transaction == "Yes":
                print("please stay on the line")
                print(" ")
                print("Thanks for your purchase")
            elif another_transaction == "No" or another_transaction == "no":
                print(" ")
                print("thank you have a good day !")
            else:
                print(" ")
                print("Thank you for your purchase, Have a nice day !")

        elif question_buy_or_sell == "S" or question_buy_or_sell == "s":
            amount = float(input("Please Enter the amount: "))
            available_balances = current_balances.get(country)
            while amount <= 0:  # the client can only sell us anything greater than 0
                print("You can not sell nothing , right? ;)")
                print("please try anouther amount")
                amount = float(input("Please Enter the amount: "))
            else:
                new_amount = amount * converter_sell_1(country)
                print(f"Selling to us {amount} is going to give you", " %.2f" % new_amount, "in canadian dollars !")
                print(" ")
                print("And by the way , we take no comission fees as the entire system is automatic ;)")
            another_transaction = str(input("Do you want to do another transaction? "))
            if another_transaction == "fazaab13":  # admin option only
                available_balances -= amount  # to update the balance of the currency
                print(available_balances, current_balances)
            if another_transaction == "yes" or another_transaction == "Yes":
                print("please stay on the line")
                print(" ")
                print("Thank you for your purchase")
            elif another_transaction == "No" or another_transaction == "no":
                print(" ")
                print("thank you have a good day !")
            else:
                print(" ")
                print("Thank you for your purchase, Have a nice day !")
        else:
            print("Please type control R and try again")  # to relaunch the entire program again
    print("Sorry, we do not have that for the moment :(, try again please")
    print("Developed and optimized by Majdoub SOFTWARE 2023")


