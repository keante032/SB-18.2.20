def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    digit_counter1 = {}
    digit_counter2 = {}

    for char in str(num1):
        digit_counter1[char] = digit_counter1.get(char, 0) + 1
    
    for char in str(num2):
        digit_counter2[char] = digit_counter2.get(char, 0) + 1
    
    return digit_counter1 == digit_counter2