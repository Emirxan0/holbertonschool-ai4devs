def is_palindrome(s):
    # Fix: Normalize string - lowercase and remove spaces
    normalized = s.lower().replace(" ", "")

    # Fix: Reverse entire string with [::-1] not [::-2]
    reversed_s = normalized[::-1]

    if normalized == reversed_s:
        return True
    else:
        return False

print(is_palindrome("Racecar"))  # Expected: True
print(is_palindrome("hello"))    # Expected: False
print(is_palindrome("A man a plan a canal Panama"))  # Expected: True
