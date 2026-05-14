#!/usr/bin/env python3
"""
Bug 2 Fix: Null/None reference error
Original bug: Calling .strip() on None causes AttributeError.
Fix: Added None check before accessing string methods.
"""


def process_input(user_input):
    if user_input is None:
        return ""
    return user_input.strip().lower()


def get_username(data):
    username = data.get("username", None)
    if username is None:
        return "anonymous"
    return username.strip()


if __name__ == "__main__":
    print(process_input("  Hello World  "))
    print(process_input(None))
    print(get_username({"username": " Alice "}))
    print(get_username({}))
