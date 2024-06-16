def reduce_fraction(numerator, denominator):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    greatest_common_divisor = gcd(numerator, denominator)
    reduced_numerator = numerator // greatest_common_divisor
    reduced_denominator = denominator // greatest_common_divisor

    return reduced_numerator, reduced_denominator


if __name__ == "__main__":
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    reduced_numerator, reduced_denominator = reduce_fraction(numerator, denominator)

    print(f"The reduced fraction is: {reduced_numerator}/{reduced_denominator}")
