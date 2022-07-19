def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase = list(phrase)
    for i in range(len(phrase)):
        if phrase[i] == to_swap.upper():
            phrase[i] = phrase[i].lower()
        elif phrase[i] == to_swap.lower():
            phrase[i] = phrase[i].upper()
    phrase = ''.join(phrase)
    return phrase