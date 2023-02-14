import csv
from datetime import datetime
PRODUCT_NUM_INDEX = 0
PRODUCT_QUANTITY_INDEX = 1

def main():
    try:
        products_dict = read_dictionary("receipt project/products.csv", PRODUCT_NUM_INDEX)
        with open("receipt project/request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)

            items = 0
            total = 0

            print("-------Receipt-------")
            for a in reader:
                key = a [0]
                item_price = float(products_dict[key] [2])
                quantity = int(a [1])
                name = products_dict[key] [1]
                price = quantity * item_price
                total =  total + price
                items = items + quantity
                print(f"{name}: {quantity} @ ${item_price}")


            tax = total * .06
            total_plus_tax = total + tax
            current_date_and_time = datetime.now()
            day_of_week  = current_date_and_time.weekday()
                
            print("---------------------")
            print(f"Number of Items: {items} ")
            print(f"Subtotal: {round(total, 2)}")
            print(f"Sales Tax: {round(tax, 2)}")
            print(f"Total: {round(total_plus_tax, 2)}")
            if day_of_week == 4 or 5 or 6:
                discount = total * .10
                total = total - discount
                total_plus_tax = total + tax
                print("---------------------")
                print("Applied Discount!")
                print(f"You Saved {round(discount, 2)}!")
            print("---------------------")
            print("Thank you for shopping with us!")
            print(f"{current_date_and_time:%c}")
    
    except (FileNotFoundError, PermissionError) as err:
        print(err)
    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file")
        print(type(key_err).__name__, key_err, sep=": ")

            



def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, "rt") as products_file:
        reader = csv.reader(products_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    
    return dictionary

if __name__ == "__main__":
    main()