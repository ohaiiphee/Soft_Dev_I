import random

def main():
    name = "Sofia Martins Rua"
    print(name)

    # call and print function only once
    print(generate_lotto_numbers(6,45)) # austrian lottery

def generate_lotto_numbers(count, max):
    lotto_numbers = [] # empty list to start

    # keep searching for numbers until we have needed amount (5-6 numbers depending on the lottery)
    while len(lotto_numbers) < count:
        number_to_add = random.randint(1, max) # generate random number to add to lotto_numbers
        # only add number if it isn't already on the list --> no repeat numbers!
        if number_to_add not in lotto_numbers:
            lotto_numbers.append(number_to_add)

    # sort numbers and return
    lotto_numbers.sort()
    return lotto_numbers

main()