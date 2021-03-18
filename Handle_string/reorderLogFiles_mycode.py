from typing import List
import re

def reorderLogFiles(logs: List[str]) -> List[str]:
    # rlogs = []
    # for log in logs:
    #     type = log.split()[0]
    #     r = re.compile(r'let*')
    #     matchobj = r.search(type)
    #     if matchobj != None:
    #         rlogs.insert(0, log)
    #     else:
    #         rlogs.append(log)
    #
    # for log in rlogs:
    #
    #     # sorted(log.split(), key=lambda x: x[1])

    # print(rlogs)
    for log in logs:
        sorted(log.split(), key=lambda x: [1])
        print(log)


if __name__ == '__main__':
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    reorderLogFiles(logs)