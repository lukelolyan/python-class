import math
import decimal
num5 = 0.25
num6 = 0.10

num3 = input(" what is the number of your less that 1L bottles?")
num4 = input("what is the number of your bottle that are more than 1L")

truenum1 = float(num4) * num5
truenum2 = float(num3) * num6
last = truenum1+truenum2

print("the amount of cash you will get is $", last)