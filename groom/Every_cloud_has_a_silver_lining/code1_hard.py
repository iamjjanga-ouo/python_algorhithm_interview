import sys
import math

sys.stdin = open('Every_cloud_has_a_silver_lining/input.in', 'r')
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = math.inf
# 가장 작은 숫자가 맨 앞일 때... 맨 뒤일 때까지.
start_idx = arr.index(min(arr))

for i in range(k):
    print("i : ", i)
    cnt = 1
    front, back = arr[:start_idx-i], arr[start_idx+k-i:]

    front_cnt = len(front) // (k-1) + (1 if len(front) % (k-1) else 0)
    print("front_cnt:", front_cnt, "->",(1 if len(front) % (k-1) else 0))

    back_cnt = len(back) // (k-1) + (1 if len(back) % (k-1) else 0)
    print("back_cnt:", back_cnt, "->",(1 if len(back) % (k - 1) else 0))

    answer = min(answer, cnt + front_cnt + back_cnt)
    print("answer : ", answer)
    print("==========")
# print(answer)