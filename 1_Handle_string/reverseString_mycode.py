
def reverseString(s: list[str]) -> None:
    # strs = s[:]
    #
    # i = 0
    # for c in strs[::-1]:
    #     s[i] = c
    #     i += 1
    s = s[::-1]

    print(s)

if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    # s = ["H", "a", "n", "n", "a", "h"]
    reverseString(s)