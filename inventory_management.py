import re
import unicodedata

inventory:dict = {}

def validate_product_name(product_name:str = "") -> str:
    """
    Validate and format a product name according to specific rules.

    - Max 25 characters
    - Letters and spaces only (supports Spanish characters)
    - Single spaces only

    Args:
        product_name (str, optional): Initial product name to validate. Defaults to "".

    Returns:
        str: The validated and capitalized product name.
    """
    condition:bool = True
    while condition:
        product_name = " ".join(input("\n📝 Enter the product name: ").split())
        if len(product_name) > 25:
            print("\033[91m❌ The product name must not exceed 25 characters.\033[0m")
        elif not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", product_name):
            print("\033[93m⚠️ Only letters and spaces are allowed (including accents like á, é, ñ).\033[0m")
        else:
            condition = False
    return product_name


def validate_product_price(product_price:float = 0.0) -> float:
    """
    Validate and format a product price according to specific rules.

    - Must be a positive number (greater than 0)
    - Must be a valid float number
    - Cannot exceed 1,000,000,000
    - Rounds to 2 decimal places

    Args:
        product_price (float, optional): Initial price to validate. Defaults to 0.0.

    Returns:
        float: The validated price rounded to 2 decimal places.
    """
    condition:bool = True
    while condition:
        try:
            product_price = round(float(input("\n💰 Enter the product price: ")), 2)
            if 0 < product_price <= 1_000_000_000:
                condition = False
            elif product_price > 1_000_000_000:
                print("\033[91m❌ Price exceeds the maximum allowed ($1,000,000,000).\033[0m")
            else:
                print("\033[91m❌ Invalid price. The value must be greater than zero.\033[0m")
        except ValueError:
            print("\033[93m⚠️ Invalid input. Please enter a valid number (e.g., 19.99).\033[0m")
    return product_price


def validate_product_quantity(product_quantity:int = 0) -> int:
    """
    Validate and format a product quantity according to specific rules.

    - Must be a positive integer (greater than 0)
    - No decimals allowed
    - Maximum allowed quantity is 100,000,000

    Args:
        product_quantity (int, optional): Initial quantity to validate. Defaults to 0.

    Returns:
        int: The validated quantity.
    """
    condition:bool = True
    while condition:
        try:
            product_quantity = int(input("\n📦 Enter the available product quantity: "))
            if 0 < product_quantity <= 100_000_000:
                condition = False
            elif product_quantity > 100_000_000:
                print("\033[91m❌ Quantity exceeds the maximum allowed (100,000,000).\033[0m")
            else:
                print("\033[91m❌ Quantity must be greater than zero.\033[0m")
        except ValueError:
            print("\033[93m⚠️ Invalid input. Please enter a whole number (e.g., 15).\033[0m")
    return product_quantity


def normalize(text: str) -> str:
    """
    Function to normalize a string to remove accents and convert to lowercase.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    ).lower()


def add_product(product_name:str = "", product_price:float = 0.0, product_quantity:int = 0) -> None:
    """
    Add one or multiple products to the inventory.

    - Allows adding products and continuing in a loop.
    - Stores product name, price, and quantity.

    Args:
        product_name (str, optional): Name of the product. Defaults to "".
        product_price (float, optional): Price of the product. Defaults to 0.0.
        product_quantity (int, optional): Quantity of the product. Defaults to 0.

    Returns:
        None: This function modifies the inventory directly and doesn't return a value.
    """
    condition:bool = True
    while condition:

        # Check if the product already exists
        if normalize(product_name) in inventory.keys():
            print("\033[93m⚠️ The product already exists.\033[0m")
        else:
            inventory[normalize(product_name)] = (product_price, product_quantity)
            print(f"\033[92m\n➕ The Product '{product_name.capitalize()}': ('Price': ${product_price}, 'Quantity': {product_quantity} unit(s)) added successfully!\033[0m")

        # Ask if the user wants to add another product
        print(f"""\033[93m\n➕ Add another product? 
(Press 'y' to add more / any other key to return to menu): \033[0m""", end = "")

        if input().strip().lower() != "y":
            condition = False
        else:
            # Validate new product information
            product_name:str = validate_product_name()
            if normalize(product_name) not in inventory.keys():
                product_price:float = validate_product_price()
                product_quantity:int = validate_product_quantity()
            else:
                continue


def search_product(product_name:str = "") -> tuple[float, int]:
    """
    Search for a product in the inventory and display its information.

    - Displays product name, price, and quantity if found.
    - Allows repeated searches.

    Args:
        product_name (str, optional): Name of the product to search. Defaults to "".

    Returns:
        tuple[float, int]: Price and quantity of the last searched product.
    """
    product_price:float = 0.0
    product_quantity:int = 0
    condition:bool = True
    while condition:

        # Check if the product exists in the inventory
        if normalize(product_name) in inventory.keys():
            product_price, product_quantity = inventory[normalize(product_name)]
            print(f"\033[32m🔍 Product found!\033[0m")
            print(f"""\033[92m-------------------------
🛒 Name: {product_name.capitalize()}
💰 Price: ${product_price}
📦 Quantity available: {product_quantity}\033[0m""")
        else:
            print(f"\033[91m❌ The product '{product_name}' is not in the inventory.\033[0m")

        # Ask if the user wants to search for another product
        print(f"""\033[93m\n🔍 Search for another product? 
(Press 'y' to continue / any other key to return to menu): \033[0m""", end = "")

        if input().lower() != "y":
            condition = False
        else:
            # Validate a new product name
            product_name:str = validate_product_name()

    return product_price, product_quantity


def update_product_price(product_name:str = "", new_product_price:float = 0.0) -> None:
    """
    Update the price of one or multiple products in the inventory.

    - Verifies if the product exists
    - Updates only the price, keeping the quantity unchanged
    - Displays confirmation and allows multiple updates

    Args:
        product_name (str, optional): Name of the product to update. Defaults to "".
        new_product_price (float, optional): New price for the product. Defaults to 0.0.

    Returns:
        None: This function modifies the inventory directly and doesn't return a value.
    """
    condition:bool = True
    while condition:

        # Check if the product exists in the inventory
        if normalize(product_name) in inventory.keys():
            old_product_price:float = inventory[normalize(product_name)][0]
            product_quantity:int = inventory[normalize(product_name)][1]
            inventory[normalize(product_name)] = (new_product_price, product_quantity)
            print(f"\033[32m💲 Product price updated!\033[0m")
            print(f"""\033[92m-------------------------
🛒 Name: {product_name.capitalize()}
💸 Old price: ${old_product_price}
💰 New price: ${new_product_price}
📦 Quantity available: {product_quantity}\033[0m""")
        else:
            print(f"\033[91m\n❌ The product '{product_name}' is not in the inventory.\033[0m")

        # Ask if the user wants to update another product's price
        print(f"""\033[93m\n💲 Update another product's price? 
(Press 'y' to continue / any other key to return to menu): \033[0m""", end = "")

        if input().lower() != "y":
            condition = False
        else:
            # Validate new product information
            product_name:str = validate_product_name()
            if normalize(product_name) in inventory.keys():
                new_product_price:float = validate_product_price()
            else:
                continue


def delete_product(product_name:str = "") -> None:
    """
    Delete one or multiple products from the inventory.

    - Verifies product existence
    - Deletes product and confirms the action
    - Allows multiple deletions in a loop

    Args:
        product_name (str, optional): Name of the product to delete. Defaults to "".

    Returns:
        None: This function modifies the inventory directly and doesn't return a value.
    """
    condition:bool = True
    while condition:

        # Check if the product exists in the inventory
        if normalize(product_name) in inventory.keys():
            print("\033[93m\n👉 Do you really want to permanently delete this product? (y/n): \033[0m", end = "")
            if input().lower() == "y":
                del inventory[normalize(product_name)]
                print(f"\033[92m🗑️ The product '{product_name.capitalize()}' has been permanently deleted from the inventory.\033[0m")
            else:
                print(f"\033[34m👉 The product '{product_name.capitalize()}' was not deleted.")
        else:
            print(f"\033[91m❌ The product '{product_name.capitalize()}' is not in the inventory.\033[0m")

        # Ask if the user wants to delete another product
        print(f"""\033[93m\n🗑️ Delete another product? 
(Press 'y' to continue / any other key to return to menu): \033[0m""", end = "")

        if input().lower() != "y":
            condition = False
        else:
            # Validate a new product name
            product_name:str = validate_product_name()


def menu() -> str:
    """
    Display the main menu of the inventory management system and get user input.

    Returns:
        str: The user's selected option as a string (from "1" to "7").
    """
    print("\033[96m\n---------- 📊 Inventory Management Menu ----------\033[0m")
    print("""
1.➕ Add product
2.🔍 Search product
3.💲 Update product price
4.🗑️ Delete product
5.🧮 Calculate total inventory value
6.📦 View full inventory
7.🚪 Exit
    """)
    option:str = input("👉 Enter the number of the action you want to perform: ")
    return option


def main() -> None:
    """
    Main function to run the inventory management program.

    The program continues running until the user selects the exit option (7).
    """
    condition:bool = True
    while condition:
        option:str = menu()

        if option == "1":
            print("\033[96m\n➕ -------------------- ADD PRODUCT --------------------\033[0m")
            product_name:str = validate_product_name()
            product_price:float = 0.0
            product_quantity:int = 0
            if normalize(product_name) not in inventory.keys():
                product_price:float = validate_product_price()
                product_quantity:int = validate_product_quantity()
            add_product(product_name, product_price, product_quantity)

        elif option == "2":
            print("\033[96m\n🔍 ----------------- SEARCH PRODUCT ------------------\033[0m")
            product_name:str = validate_product_name()
            search_product(product_name)

        elif option == "3":
            print("\033[96m\n💲 ------------------ UPDATE PRICE -------------------\033[0m")
            product_name:str = validate_product_name()
            new_product_price:float = 0.0
            if normalize(product_name) in inventory.keys():
                new_product_price:float = validate_product_price()
                update_product_price(product_name, new_product_price)
            else:
                update_product_price(product_name, new_product_price)

        elif option == "4":
            print("\033[96m\n🗑️ ------------------ DELETE PRODUCT ------------------\033[0m")
            product_name:str = validate_product_name()
            delete_product(product_name)

        elif option == "5":
            print("\033[96m\n🧮 -------- CALCULATE TOTAL INVENTORY VALUE --------\033[0m")
            total_value:float = sum(map(lambda x: x[0] * x[1], inventory.values()))
            print(f"\033[92m\n💰 Total inventory value: ${total_value:.2f}\033[0m")

        elif option == "6":
            print("\033[96m\n📦 ------------------- VIEW INVENTORY ------------------\033[0m")
            if inventory:
                print(f"\033[93m\n{'📋 Product Name':<25}  {'💵 Price':<14}  {'📦 Quantity':<12}\033[0m")
                print("-" * 65)
                for product, details in inventory.items():
                    price, quantity = details
                    print(f"\033[92m{product.capitalize():<25}  $ {price:<15}  {quantity:<15}")
            else:
                print("\033[93m\n⚠️ The inventory is empty.\033[0m")

        elif option == "7":
            condition = False
            print("\033[92m\n👋 Thank you for using the inventory management program. Goodbye!\033[0m")
        else:
            print("\033[91m\n❌ Invalid option. Please enter a number between 1 and 7.\033[0m")


if __name__ == "__main__":
    main()