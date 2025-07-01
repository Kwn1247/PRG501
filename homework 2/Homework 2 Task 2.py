# Homework 2
# @Author  : Haixiang Yu

# Tuple to store SPY stock prices for the past 5 days
SPY_prices = (572.41, 588.75, 588.43, 590.71, 594.26)

def show_price_for_day():
    try:
        day = int(input("Enter the day number (1-5): "))
        if 1 <= day <= 5:
            price = SPY_prices[day - 1]
            print(f"The SPY price on Day {day} was ${price}")
        else:
            print("Invalid day. Please enter a number between 1 and 5.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    print("Welcome to the SPY Tracker!")
    print("We have prices for the last 5 days.")

    while True:
        show_price_for_day()
        again = input("Would you like to check another day? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the SPY Price Tracker.")
            break

if __name__ == "__main__":
    main()
