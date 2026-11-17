
"""
DevSecOps Lab
A simple Python application for security analysis.
"""


def calculate_total(price, quantity):
    """Calculate the total price."""
    return price * quantity


def main():
    price = 25
    quantity = 4

    total = calculate_total(price, quantity)

    print(f"Total price: ${total}")


if __name__ == "__main__":
    main()
