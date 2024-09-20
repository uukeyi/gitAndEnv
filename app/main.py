def is_valid_brackets(sequence):
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    pairs_values = pairs.values()

    stack = []

    for char in sequence:
        if char in pairs_values:
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0
