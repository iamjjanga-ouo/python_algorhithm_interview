from typing import List

# # 부루트 포스로 풀면 time limit 걸린다.
# # O(n3)
# def threeSum(nums: List[int]) -> List[List[int]]:
#     arr = []
#     if len(nums) < 3:
#         return arr
#
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             for k in range(j+1, len(nums)):
#                 if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in arr:
#                     arr.append(sorted([nums[i], nums[j], nums[k]]))
#
#     return arr

# 투 포인터의 합 계산
def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort() # O(nlogn) <- TimSort

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀가며 합 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0인 경우이므로 정답 및 스킵 처리
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # 정답을 list에 추가하고 pointer 둘다 이동
                left += 1
                right -= 1

    return results


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))