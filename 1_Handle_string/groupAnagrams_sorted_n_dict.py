## 내 코드는 TimeLimit 뜸..

from typing import List
import collections

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 장렬하여 딕셔너리 추가
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = [""]
    # strs = ["a"]
    result = groupAnagrams(strs)
    print(result)