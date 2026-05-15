# Two Sum Variant
inputs = [2, 2, 11, 7]
K = 9

def find_two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f"{i} {j}")
                return

find_two_sum(inputs, K)
# Output: 0 3

inputs = [2, 2, 11, 7]
K = 9
seen = {}
for index, num in enumerate(inputs):
    complement = K - num
    if complement in seen:
        print(f"{seen[complement]} {index}")
        break
    seen[num] = index
