import random
import array


DEFAULT_LIST_LEN = 1_000_000

TEST_LISTS = [
    # integers
    [x for x in range(0, DEFAULT_LIST_LEN)],
    # floats
    [float(x) for x in range(0, DEFAULT_LIST_LEN)],
    # strings
    [str(x) for x in range(0, DEFAULT_LIST_LEN)],
    # booleans
    [bool(random.getrandbits(1)) for x in range(0, DEFAULT_LIST_LEN)],
    # arrays
    [array.array("I", [x]) for x in range(0, DEFAULT_LIST_LEN)],
    # lists
    [[x] for x in range(0, DEFAULT_LIST_LEN)],
    # tuples
    [(x, x-1) for x in range(0, DEFAULT_LIST_LEN)],
    # dictionaries
    [{str(x): x} for x in range(0, DEFAULT_LIST_LEN)],
    # sets
    [set(str(x)) for x in range(0, DEFAULT_LIST_LEN)]
]
