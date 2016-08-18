def balanced_check(s):
    if len(s) % 2 != 0:
        return False
    opening = set('([{')
    matches = [('(', ')'), ('{', '}'), ('[', ']')]

    stack = []

    for item in s:
        if item in opening:
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            top_item = stack.pop()
            if (top_item, item) not in matches:
                return False
    if len(stack) != 0:
        return False

    return True


print balanced_check('[]()[{()}][}')
