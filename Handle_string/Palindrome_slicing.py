# 32ms
# 내부적으로 C로 빠르게 구현되어 있어 훨씬 더 좋은 속도를 기대할 수 있음.
import re

def isPalindrome(s : str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] # 슬라이싱


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    # s = "race a car"
    # s = "a."
    print(isPalindrome(s))

