def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    If the discount is 20% or higher, the discount is applied.
    Otherwise, the original price is returned.
    
    :param price: Original price of the item
    :param discount_percent: Discount percentage
    :return: Final price after discount
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price  # No discount applied

if __name__ == "__main__":
    # Prompt user for input
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(price, discount_percent)
    
    # Print the result
    print(f"The final price after applying the discount is: ${final_price:.2f}")

