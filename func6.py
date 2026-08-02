"""
Write a function called discount_price that takes original price
and discount price as parameters and prints the final price after discount.

"""
def discount_price(original_price, discount):
    final_price = original_price - (original_price * discount / 100)
    print("Final price after discount:", final_price)

discount_price(100, 20)