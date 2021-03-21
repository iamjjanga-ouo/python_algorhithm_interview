## 내 코드는 TimeLimit 뜸..

from typing import List
import collections

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    s = sorted(strs)
    res_list = []
    idx = 0
    for i in s:
        group = []
        group.clear() # flush list

        group.append(i)
        for j in s[idx+1:]:
            a = collections.Counter(i)
            b = collections.Counter(j)
            if a == b:
                group.append(j)
                s.remove(j)
        res_list.append(group)
        idx += 1

    return sorted(res_list, key=lambda x: -len(x))

if __name__ == '__main__':
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = [""]
    strs = ["a"]
    result = groupAnagrams(strs)

    print(result)