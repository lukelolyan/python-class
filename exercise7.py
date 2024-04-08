def sum_of_integers(n):
    return (n * (n + 1)) // 2

def main():
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    total_sum = sum_of_integers(n)
    print("The sum of all integers from 1 to", n, "is:", total_sum)

if __name__ == "__main__":
    main()