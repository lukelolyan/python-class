def is_sorted(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(num) for num in user_input.split()]
    
    if is_sorted(numbers):
        print("The list is sorted.")
    else:
        print("The list is not sorted.")
