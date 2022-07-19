def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    list_of_lists = [elem for elem in lst if isinstance(elem, list)]

    if len(list_of_lists) < len(lst):
        return False
    else:
        return True