def calculate_savings(initial_amount, years, interest_rate):
    """
    Calculate the savings amount after a given number of years
    """
    for year in range(1, years + 1):
        initial_amount *= (1 + interest_rate / 100)
        print(f"After {year} year(s), the savings amount is: ${initial_amount:.2f}")

def main():
    # Input the initial amount deposited into the account
    initial_amount = float(input("Enter the initial amount deposited into the account: "))

    # Define interest rate
    interest_rate = 4  # 4 percent interest per year

    # Compute and display the savings amount after 1, 2, and 3 years
    calculate_savings(initial_amount, 3, interest_rate)

if __name__ == "__main__":
    main()
