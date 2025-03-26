def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price: The original price of the item.
        discount_percent: The discount percentage.

    Returns:
        The final price after discount, or the original price if no discount is applied.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
while True:
    try:
        price = float(input("Enter the original price of the item: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numerical price.")

while True:
    try:
        discount_percent = float(input("Enter the discount percentage: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numerical percentage.")


# Calculate and print the final price
final_price = calculate_discount(price, discount_percent)
print(f"Final price: ${final_price:.2f}")  # Format to 2 decimal places