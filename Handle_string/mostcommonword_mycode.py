from collections import Counter
from typing import List
from string import punctuation
import re


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    paragraph = re.sub(r'[^0-9a-z\s]', ' ', paragraph.lower())

    if len(paragraph.split()) > 1:
        c = Counter(paragraph.split()).most_common()

        for counter in c:
            if counter[0] in banned:
                continue
            return counter[0].strip()
    else:
        return paragraph.strip()


if __name__ == '__main__':
    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # banned = ["hit"]

    paragraph = "a."
    banned = []

    # paragraph = "Bob"
    # banned = []

    # paragraph = "Bob. hIt, baLl"
    # banned = ["bob", "hit"]

    # paragraph =  "a, a, a, a, b,b,b,c, c"
    # banned = ["a"]

    mcw = mostCommonWord(paragraph, banned)
    print(mcw)