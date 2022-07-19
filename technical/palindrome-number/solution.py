def is_palindrome(x: int) -> bool:
    original_x = x
    reversed_x = 0
    while x > 0:
        last_digit = x % 10
        reversed_x = (reversed_x * 10) + last_digit
        x //= 10
    return reversed_x == original_x


if __name__ == '__main__':
    assert is_palindrome(121) is True
    assert is_palindrome(123) is False
    assert is_palindrome(12455421) is True
