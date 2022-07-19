def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_lst = []

    for i in range(len(lst)):
        if bool(lst[i]):
            new_lst.append(lst[i])
    
    return new_lst