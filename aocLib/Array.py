def JumpIndexRollingBuffer(index, n, lengthOfArray):
    """
    Return the Index after jumping n steps. If the index reaches the end start at the front of
    the array (rolling buffer).

    Example:
     array = [0, 1, 2, 3, 4, 5]

     JumpIndexRollingBuffer(1, 2, 6) --> 3
     JumpIndexRollingBuffer(1, 3, 6) --> 4
     JumpIndexRollingBuffer(5, -2, 6) --> 1

    :param index: current index
    :type index: int
    :param n: steps
    :type n: int
    :param lengthOfArray: length of the array
    :type lengthOfArray: int
    :return: index after jump
    :rtype: int
    """
    return (index + n) % lengthOfArray
