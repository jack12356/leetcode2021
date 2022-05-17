def titleToNumber(s: str):
    cnt = 0
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for c in s:
        cnt = cnt*26 + letters.index(c)+1
    return cnt


if __name__ == '__main__':
    print(titleToNumber('az'))
