def is_palindrome(s):
    normalized = "".join(s.split()).lower()
    reversed_s = normalized[::-1]
    if normalized == reversed_s:
        return True
    else:
        return False
print(is_palindrome("Racecar"))
