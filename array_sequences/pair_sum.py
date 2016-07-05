def pair_sum(list, sum):
    seen = set()
    output = set()
    for item in list:
        target = sum - item
        if target in seen:
            output.add((item, target))
            print output
        else:
            seen.add(item)


pair_sum([1, 2, 3, 4, 5], 7)
