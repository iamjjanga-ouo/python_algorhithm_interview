import collections
from typing import List
from string import punctuation
import re


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    # Data Cleansing
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split() if word not in banned]
    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫번째 인덱스 리턴
    return counts.most_common(1)[0][0]

    ### defaultDict를 이용하고 maxarg에 대해서 찾음
    # counts = collections.defaultdict(int)   # {'None':0} 이렇게 초기화 되는 느낌
    # for word in words:
    #     counts[word] += 1
    #
    # return max(counts, key=counts.get)



if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    # paragraph = "a."
    # banned = []

    # paragraph = "Bob"
    # banned = []

    # paragraph = "Bob. hIt, baLl"
    # banned = ["bob", "hit"]

    # paragraph =  "a, a, a, a, b,b,b,c, c"
    # banned = ["a"]

    mcw = mostCommonWord(paragraph, banned)
    print(mcw)