# Handy functions:
# .upper() - uppercases a string
# .lower() - lowercases a string
# .title() - titlecases a string
# There is no function to reverse a string.
# Maybe you can do it with a slice?

def stringcases(s):
    return (s.upper(), s.lower(), s.title(), s[::-1])
