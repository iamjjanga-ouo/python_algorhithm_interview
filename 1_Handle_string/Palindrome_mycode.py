import string

def isPalindrome(s : str) -> bool:
    delim = list(string.punctuation)
    delim.append(" ")
    s = s.lower()

    for d in delim:
        s = s.replace(d, "")

    if len(s) != 1:
        j = len(s) - 1
        for i in range(0, int(len(s) / 2)):
            if s[i] != s[j]:
                return False
            j -= 1
    return True

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    # s = "race a car"
    # s = "a."
    print(isPalindrome(s))

