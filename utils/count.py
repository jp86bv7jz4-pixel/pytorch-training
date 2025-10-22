from .function import add


def count_word(s, w):
    counter = 0
    for ch in s:
        if w == ch:
            counter = add(counter, 1)

    assert isinstance(s, str) and len(w) == 1
    return counter

