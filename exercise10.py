

def main():
    a, b = map(int, input("Enter two integers (a and b): ").split())

    print("Sum of", a, "and", b, "is:", a + b)
    print("Difference when", b, "is subtracted from", a, "is:", a - b)
    print("Product of", a, "and", b, "is:", a * b)
    print("Quotient when", a, "is divided by", b, "is:", a / b)
    print("Remainder when", a, "is divided by", b, "is:", a % b)
    print("Result of log10", a, "is:", math.log10(a))
    print("Value of", a, "raised to the power of", b, "is:", a ** b)

if __name__ == "__main__":
    main()
