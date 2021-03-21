import sys

def black(n: int, k: int, arr: list) -> int:
    idx = 0
    answer = 0
    while True:
        if idx >= n:
            break
        if idx == 0:
            idx += k
        else:
            idx += k-1
        answer += 1

    return answer



if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    answer = black(n, k, arr)
    print(answer)



# l_cnt = len(left) // (k-1) + (1 if len(left) % (k-1) else 0)
# r_cnt = len(right) // (k-1) + (1 if len(right) % (k-1) else 0)