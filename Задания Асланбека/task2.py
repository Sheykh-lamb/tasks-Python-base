def max_subarray_sum(nums: list) -> int:
    max_sum = sum(nums)
    
    for i in range(len(nums)):
        total = nums[i] 
        for j in range(i + 1, len(nums)):

            total += nums[j]

            if total >= max_sum:
                max_sum = total
       
    return max_sum


# Тест

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))  # 6 (подмассив [4,−1,2,1])

# Тест 2 

nums = [4, 1, -3, -2, -1, 2, 1, -5, 4, -1, 5, -1]
print(max_subarray_sum(nums))  # 5 (подмассив [4, -1, 5])