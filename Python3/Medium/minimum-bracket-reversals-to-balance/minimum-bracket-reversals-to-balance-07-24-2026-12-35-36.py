def countMinReversals(s):
    stack = []
    opening_brack = 0
    closing_brack = 0

    for char in s:
        if char == "}":
            if stack and stack[-1] == "{":
                stack.pop()
                opening_brack -= 1
            else:
                if char == "}":
                    closing_brack += 1
                stack.append(char)

        else:
            if char == "}":
                closing_brack += 1
            else:
                opening_brack += 1

            stack.append(char)

    if len(stack) % 2 == 1:
        return -1

    return ((opening_brack + 1) // 2) + ((closing_brack + 1) // 2)
