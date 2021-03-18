# 304ms

def isPalindrome(s : str) -> bool:
    strs  = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower()) # ['a', 'b', 'c']

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop(): # 맨앞과 맨뒤를 비교
            return False

    return True
if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    # s = "race a car"
    # s = "a."
    print(isPalindrome(s))

