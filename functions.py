# 1. Create a function named calculate_discount, that calculates the final discount after applying discount.
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount 
        return final_price
    else:
        return price

# 2. Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
try:
    # Get input from user
    price = float(input("Enter original price of an item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(price, discount_percent)

    # Print the results
    if discount_percent >= 20:
        print(f"The final price is discounted: ${final_price:.2f}")
    else:
        print(f"No discount price remains the same: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numbers, like 10 or 10.5!")
