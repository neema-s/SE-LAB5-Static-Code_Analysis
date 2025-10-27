"""
inventory_system.py
This module manages a simple inventory system allowing adding,
removing, saving, and loading of stock data.
It demonstrates file handling, static analysis, and code improvement practices.
"""
import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item and its quantity to the inventory.
    Args:
        item (str): Name of the item.
        qty (int): Quantity to add.
        logs (list): List to store operation logs.
    """
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        print(f"Invalid input types: item={item}, qty={qty}")
        return
    if not item:
        print("Item name cannot be empty")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove a given quantity of an item from the inventory.
    Args:
        item (str): Name of the item.
        qty (int): Quantity to remove.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except (KeyError, ValueError, FileNotFoundError) as e:
        print(f"Error removing item {item}: {e}")


def get_qty(item):
    """
    Retrieve the current quantity of a specified item.
    Args:
        item (str): Name of the item.
    Returns:
        int: Quantity available for the given item.
    """
    return stock_data[item]


def load_data(filename="inventory.json"):
    """
    Load inventory data from a JSON file.
    Args:
        filename (str): Name of the file to read inventory data from.
    Returns:
        dict: Inventory data loaded from the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        inventory = json.load(file)
    return inventory


def save_data(file="inventory.json"):
    """
    Save current inventory data to a JSON file.
    Args:
        file (str): File name to write inventory data into.
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data():
    """
    Print all items and their quantities from the inventory.
    """
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_lowitems(threshold=5):
    """
    Identify items with quantity below a given threshold.
    Args:
        threshold (int): Minimum quantity threshold.
    Returns:
        list: Items below the specified threshold.
    """
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """
    Main function to demonstrate the inventory system workflow.
    """
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_lowitems())
    save_data()
    load_data()
    print_data()
    print("eval used")
    # eval("print('eval used')")  # dangerous


if __name__ == "__main__":
    main()
