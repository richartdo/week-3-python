
# Create a function named calculate_discount(price, discount_percent)
def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        deducted_discount = price * (discount_percent / 100)
        final_price = price - deducted_discount
        return final_price
    else:
        return price

# prompt the user to enter the original price of an item and the discount percentage
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# calculating the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price after applying the discount, or if no discount was applied, print the original price
if discount_percent >= 20:
    print(f"The final price when {discount_percent}% is included is ${final_price}")
else:
    print(f"Final price without any discount included: ${price}")