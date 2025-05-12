# Inventory Management Program

This Python program helps manage a store's inventory efficiently. It provides functionalities to add, search, update, delete products, and calculate the total value of the inventory.

## Features
- **Add products**: Allows adding new products with their name, price, and quantity.
- **Search products**: Search for a product by its name and view its details (price and quantity).
- **Update product prices**: Change the price of an existing product.
- **Delete products**: Remove products from the inventory.
- **Calculate inventory value**: Calculate the total value of all products in stock.

## How It Works
- The program uses **functions** to handle each operation (adding, searching, updating, and deleting products).
- Products are stored in a **dictionary**, where the product name is the key, and the price and quantity are stored as a tuple.
- The **total value of the inventory** is calculated using a lambda function.

## Functions
1. **`validate_product_name`**: Validates and formats product names (max 25 characters, only letters and spaces).
2. **`validate_product_price`**: Validates the product price (positive float, max 1,000,000,000).
3. **`validate_product_quantity`**: Validates the product quantity (positive integer, max 100,000,000).
4. **`normalize`**: Normalize a string to remove accents and convert to lowercase.
5. **`add_product`**: Adds a product to the inventory if it does not already exist.
6. **`search_product`**: Searches for a product by name and displays its details.
7. **`update_product_price`**: Updates the price of an existing product.
8. **`delete_product`**: Deletes a product from the inventory.
9. **`menu`**: Displays the menu options for the user to choose from.
10. **`main`**: The main function that controls the flow of the program.

## How to Use
- The program will repeatedly ask the user to select an operation until they choose to exit.
- For each operation, the user will be prompted to enter the necessary details.
- If any input is invalid, the program will ask the user to enter the correct information.
- The program calculates and displays the total inventory value when requested.

## Requirements
- Python 3.x or higher.

## Example
You will be prompted to choose from the following options:
1. Add product
2. Search product
3. Update price
4. Delete product
5. Show total inventory value
6. View full inventory
7. Exit

## Installation
To use the program, simply clone this repository and run the `inventory_management.py` script.

```bash
git clone https://github.com/yourusername/inventory-management.git
cd inventory-management
python inventory_management.py
```
