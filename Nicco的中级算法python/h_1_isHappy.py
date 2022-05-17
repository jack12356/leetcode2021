def is_happy(x: int):
    x = abs(x)
    used: set = set()
    used.add(x)
    while x != 1:
        x = sum([int(i) ** 2 for i in str(x)])
        if x in used and x != 1:
            return False
    return True


print(is_happy(19))