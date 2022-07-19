def roman_to_int(s: str) -> int:
    table = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    # For keeping track of the immediate previous letter
    prev = s[0]

    total = table[prev]
    for c in s[1:]:
        # Special cases to handle. If we found one, we just undo
        # the previous addition (by sustracting it) and add the
        # value of the special case
        if (c == 'V' or c == 'X') and prev == 'I':
            total = total - table[prev] + (table[c] - table[prev])
        elif (c == 'L' or c == 'C') and prev == 'X':
            total = total - table[prev] + (table[c] - table[prev])
        elif (c == 'D' or c == 'M') and prev == 'C':
            total = total - table[prev] + (table[c] - table[prev])
        else:
            # Otherwise, just add the letter value
            total += table[c]
        prev = c
    return total


if __name__ == '__main__':
    assert roman_to_int('III') == 3
    assert roman_to_int('LVIII') == 58
    assert roman_to_int('MCMXCIV') == 1994
