def capitalize_string(input_string):
    words = input_string.split()
    for i in range(len(words)):
        if i == 0 or (i > 0 and (words[i-1][-1] in ['.', '!', '?'])):
            words[i] = words[i].capitalize()
        elif words[i] == 'i' and i > 0 and i < len(words) - 1 and words[i-1] == ' ' and words[i+1] == ' ':
            words[i] = 'I'
    return ' '.join(words)

# Main program
user_input = input("Enter a string: ")
capitalized_string = capitalize_string(user_input)
print("Capitalized String:", capitalized_string)
