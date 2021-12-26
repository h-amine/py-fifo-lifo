import string


DEFAULT_LIST_LEN = 10_000

TEST_LISTS = [
    # integers
    [x for x in range(0, DEFAULT_LIST_LEN)],
    # alphanumeric strings
    [x for x in list(string.ascii_lowercase + string.ascii_uppercase + string.digits)]
]
