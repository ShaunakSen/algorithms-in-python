def rev_str(s):
    if len(s) == 1:
        return s
    return s[len(s)-1] + rev_str(s[:len(s)-1])

print rev_str("123321")
