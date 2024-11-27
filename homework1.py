def linear_search(shelf, target_book):
    for index, book in enumerate(shelf):
        if book == target_book:
            return index  # Return the position of the book
    return -1  # Return -1 if the book is not found

# Example usage:
shelf = ["Book A", "Book B", "Book C", "Book D", "Book E"]
target_book = "Book C"

position = linear_search(shelf, target_book)

if position != -1:
    print(f"The book '{target_book}' is found at position {position}.")
else:
    print(f"The book '{target_book}' is not on the shelf.")
