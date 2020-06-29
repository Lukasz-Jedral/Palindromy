def is_palindrome(word):
    """
        Checks if given word is palindrome.
        Accepts only strings as arguments.
        Returns True of False.
    """
    if type(word) == str:
        rev_word = word[::-1]
        if word.capitalize() == rev_word.capitalize():
            return True
        else:
            return False
    else:
        print("Invalid input\nFunction works only with strings")

print(is_palindrome('Anna'))