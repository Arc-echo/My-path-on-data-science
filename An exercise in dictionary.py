def the_only_one(l):
    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for key, item in d.items():
        if item == 1:
            return key
