def is_palindrome(s):
    normalized = "".join(s.split()).lower()
    return normalized == normalized[::-1]

if __name__ == "__main__":
    print(is_palindrome("Racecar"))
