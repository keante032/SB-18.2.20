def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    most_common_num = None
    m_c_n_count = 0

    for n in set(nums):
        count = nums.count(n)
        if count > m_c_n_count:
            most_common_num = n
            m_c_n_count = count
    
    return most_common_num