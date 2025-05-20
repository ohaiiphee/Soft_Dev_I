import sys

''' was unsure how to use sys.argv, checked https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/ '''
#function to calculate tip instead of repeating code
def calculate_tip(final_amount, chosen_currency):
   # check final_amount to calculate tip
   if final_amount < 10:
        suggested_tip = final_amount * 0.1
        final_amount = final_amount + suggested_tip
   elif final_amount < 100:
        suggested_tip = final_amount * 0.15
        final_amount = final_amount + suggested_tip
   else:
        suggested_tip = final_amount * 0.2
        final_amount = final_amount + suggested_tip
        
   print(f"Suggested tip: {suggested_tip:.2f} {chosen_currency}")
   print(f"Total: {final_amount:.2f} {chosen_currency}")
   
#function to calculate exchange rate instead of repeating code   
def exchange_currency(amount, target_currency):
   # convert final answer to a float
    amount = float(amount)

    if target_currency == "1" or target_currency == "USD":
        final_amount = amount + (amount * 0.10)
        chosen_currency = "USD"
    elif target_currency == "2" or target_currency == "GBP":
        final_amount = amount - (amount * 0.15)
        chosen_currency = "GBP"
    elif target_currency == "3" or target_currency == "JPY":
        final_amount = amount + (amount * 129.0)
        chosen_currency = "JPY"
    
    print(f"{amount:.2f} Euro equals {final_amount:.2f} {chosen_currency}")
    calculate_tip(final_amount, chosen_currency)
    
#check if enough arguments are given via CLI   
if len(sys.argv) == 3:
    amount = sys.argv[1]
    target_currency = sys.argv[2]
    
    exchange_currency(amount, target_currency)    
    
# if not enough arguments, proceed with inputs    
else:
    # ask the user for the amount in euros
    amount = str(input("Please enter the amount in Euros: "))

    # if user tries to insert letters/symbols as the amount, ask for a new input
    while not amount.isnumeric():
        amount = input("Invalid input, please enter the amount in Euros: ")

    # convert final answer to a float
    amount = float(amount)

    # ask for the target currency
    print("Choose the target currency: ")
    print("1. USD")
    print("2. GBP")
    print("3. JPY")
    target_currency = input("What is your choice (1/2/3 or name of currency): ")

    #if user inputs something that isn't one of the options, ask them to input again until they do so :)
    while target_currency != "1" and target_currency != "2" and target_currency != "3" and target_currency != "USD" and target_currency != "GBP" and target_currency != "JPY":
        print("Invalid choice, please enter one of the options available: ")
        print("1. USD")
        print("2. GBP")
        print("3. JPY")
        target_currency = input("What is your choice (1/2/3 or name of currency): ")

    exchange_currency(amount, target_currency)  