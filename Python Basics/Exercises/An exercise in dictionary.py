def the_only_one(l):
    
    # Build a dictionary
    d = {}
    
    # A for loop to count the number appears from the list, if it is the number first time appears, build a new key, if not, add 1 to the current value.
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
            
    # A for loop to loop into the dictionary and find the key with value: 1
    for key, item in d.items():
        if item == 1:
            return key
