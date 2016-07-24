def permutations(s):
    output = []
    if len(s) == 1:
        output = [s]
    else:
        for i, letter in enumerate(s):
            for perm in permutations(s[:i] + s[i + 1:]):
                output += [letter + perm]

    return output


print permutations("abc")
print enumerate("abc")