from typing import List


# # Bruce force(무차별 대입)
# def twoSum(nums: List[int], target: int) -> List[int]:
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     list(zip(nums, nums[1:] + [nums[0]]))


# # in을 이용한 탐색
# def twoSum(nums: List[int], target: int) -> List[int]:
#     for i, n in enumerate(nums):
#         complement = target - n         # target에서 n을 뺀 값을 구해서
#
#         if complement in nums[i+1:]:    # 그 값이 n보다 오른쪽에 위치한 배열에 있는지 확인
#             return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

# # 첫번째 수를 뺀 결과 조회
# def twoSum(nums: List[int], target: int) -> List[int]:
#     nums_map = {}
#     # 키와 값을 바궈서 딕셔너리에 저장
#     for i, num in enumerate(nums):
#         nums_map[num] = i
#
#     # 타겟에서 첫 번째 수를 뺀 결과로 키를 조회
#     for i, num in enumerate(nums):
#         if target - num in nums_map and i != nums_map[target - num]:
#             return [nums.index(num), nums_map[target - num]]

# 조회 구조 개선
# def twoSum(nums: List[int], target: int) -> List[int]:
#     nums_map = {}
#     # 하나의 for문으로 통합
#     for i, num in enumerate(nums):
#         if target - num in nums_map:
#             return [nums_map[target - num], i]
#         nums_map[num] = i

# 투포인터 사용 -> X
# 정렬이 안되있는 상태면 정렬을 해야하는데, 그러면 기존의 index가 무너져 버림
def twoSum(nums: List[int], target: int) -> List[int]:
    nums.sort()
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return left, right



if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 18
    result = twoSum(nums, target)
    print(result)