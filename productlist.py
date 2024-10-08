products = ["Fries", "Burger", "Spaghetti", "Chicken", "Sundae", "Mango pie"]
prices = [50, 60, 55, 99, 50, 40]

def display_products():
    print("Available products:")
    for index, product in enumerate(products):
        print(f"{index + 1}. {product} - {prices[index]} per piece") # this will print ride along of product  hindi siya mag uumpisa sa 0 kaya me+1 siya  

def get_product_price(product_name): # def meaning define  (product_name)
    if product_name in products:
        index = products.index(product_name)
        return prices[index] # mag rereturn yung product index
    return None

def main():
    total_bill = 0
    order = {}  # dito nag storeproduct quantity

    display_products() # dito tinatawag yung display ng product saan mo siya def 

    while True: # continues loop code 
        product_name = input("Enter the product name (or type 'exit' to finish): ").capitalize() # dito if naka capitilize i accept niya 

        if product_name.lower() == 'exit': # dito pag type mo lower or equals to exit  mag sstop ang loop using break
            break

        price = get_product_price(product_name) # dito kung saan mo index yung mga product_name index then mag rereturn siya sa prices using index 

        if price is not None:  # checheck if the product price is exist or hindi so mag throw po siya sa else product not found
            while True: # continues  loop 
                try: # try code of blocks 
                    quantity = int(input("Please enter how many would you like to purchase: "))
                    if quantity < 0: # if quantity is negative number or not in less than 0 will throw  non negative number or valid number
                        print("Please enter a non-negative number.")
                    else: # block lets you execute code when there is no error
                        total_bill += quantity * price
                        order[product_name] = order.get(product_name, 0) + quantity  # Update order #order.get the product the user wants to purchase) already exists as a key in the order dictionary.
                        print(f"{quantity} {product_name}(s) added to your bill. Current total: {total_bill}.")
                        break
                except ValueError: # this block handles error
                    print("Please enter a valid number.")
        else:# block lets you execute code when there is no error
            print("Product not found. Please try again.")

    print(f"Your total bill is: {total_bill}")
    print("Thank you for shopping with us!")
    print("\nTotal Purchases:")
    for product, quantity in order.items():
        print(f"{product} x {quantity} = {quantity * get_product_price(product)}")
        print(f"Your total bill is: {total_bill}")

if __name__ == "__main__":
    main()
