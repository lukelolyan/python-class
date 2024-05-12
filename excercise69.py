
def approximate_pi(n):
    total = 3
    sign = 1
    denominator = 2
    for i in range(1, n):
        total += sign * 4 / (denominator * (denominator + 1) * (denominator + 2))
        sign *= -1
        denominator += 2
    return total

# Display 15 approximations of Pi
for i in range(1, 16):
    approx_pi = approximate_pi(i)
    print(f"Approximation {i}: {approx_pi}, Difference from Pi: {abs(math.pi - approx_pi)}")
