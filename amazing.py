# coding=utf-8


def while_bug():
    a = 1
    b = 2
    while a > 1 and b > 2:
        b -= 1
    else:
        a = 3
    return a


def try_finally():
    try:
        1 / 0
    except ZeroDivisionError:
        return 0
    finally:
        return 1


if __name__ == '__main__':
    """
    else always run
    finally is finally return
    """
    print while_bug()
    print try_finally()
