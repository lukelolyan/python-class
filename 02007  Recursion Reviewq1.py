def fibonacci(n):
    # Base cases
    if n <= 1:
        return n
    
    # Initialize cache dictionary
    cache = {0: 0, 1: 1}
    
    # Recursive function with memoization
    def fib_recursive(k):
        if k not in cache:
            cache[k] = fib_recursive(k-1) + fib_recursive(k-2)
        return cache[k]
    
    return fib_recursive(n)

# Example usage
n = int(input("Enter a number (n > 2): "))
if n > 2:
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
else:
    print("Please enter a number greater than 2.")
