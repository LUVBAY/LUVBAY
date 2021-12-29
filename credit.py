def main():
    card_number = input("Enter credit card number: ")
    print_card_value(card_number)



def print_card_value(card_number):
    if check_for_sum(card_number) == False:
        print("INVALID")

    elif check_for_amex(card_number) == True:

        print("AMEX")
    elif check_for_master(card_number) == True:
        print("MASTERCARD")

    elif check_for_visa(card_number) == True:
        print("VISA")

    else:
        print("INVALID")


def check_for_amex(card_number):
    if len(card_number) == 15 and card_number[:2] in ["34", "37"]:
        return True

    else:
        return False


def check_for_master(card_number):
    if len(card_number) == 16 and card_number[:2] in ["51", "52", "53", "54", "55"]:
        return True
    else:
        return False


def check_for_visa(card_number):
    if len(card_number) in [13, 16] and card_number[0] == "4":
        return True
    else:
        return False



def check_for_sum(card_number):
    product_of_two_sequence = 0
    not_product_of_two_sequence = 0

    product_of_two_digit_array = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
    for i in range(len(card_number)):
        new_number = int(card_number[len(card_number) - 1 - i])

        if i % 2 == 0:
            not_product_of_two_sequence = not_product_of_two_sequence + new_number
        else:
            product_of_two_sequence = product_of_two_digit_array[new_number]


    sum_of_total = not_product_of_two_sequence + product_of_two_sequence
    return ((sum_of_total % 10) == 0)



main()
