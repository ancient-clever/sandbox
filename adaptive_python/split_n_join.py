def split_n_join(name):
    """
    (str) -> str

    Return file name without spaces

    split_n_join('my file name.txt')
    >>> 'my_file_name.txt'
    split_n_join('string     with        multi spaces')
    >>> 'string_with_multi_spaces'
    split_n_join('single')
    >>> 'single'
    """

    return '_'.join(name.split())


print(split_n_join(input()))
