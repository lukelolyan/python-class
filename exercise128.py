def reverseLookup(dictionary, value):
    keys = []
    for key, val in dictionary.items():
        if val == value:
            keys.append(key)
    return keys

if __name__ == "__main__":
  #proof of work
    sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}


    print("Keys for value 1:", reverseLookup(sample_dict, 1))


    print("Keys for value 2:", reverseLookup(sample_dict, 2))


    print("Keys for value 4:", reverseLookup(sample_dict, 4))
