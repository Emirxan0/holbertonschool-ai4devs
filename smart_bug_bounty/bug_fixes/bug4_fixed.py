def is_palindrome(s):
# Bug: Only reverses up to the second to last character
    s = s.lower().replace(" ", "")
    reversed_s = s[::-1]# Bug: Doesn't normalize string (case/spaces)
    if s == reversed_s:
        return True
    else:
        return False
print(is_palindrome("Racecar")) # Should be True but returns False
