def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    unique_chars = set(phrase)

    letter_count = {char: 0 for char in unique_chars}

    for k in letter_count.keys():
        letter_count[k] = phrase.count(k)
    
    return letter_count