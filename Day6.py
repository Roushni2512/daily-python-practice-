nums = [0,1,0,3,12]

non_zero = []

# Add non-zero elements
for num in nums:
    if num != 0:
        non_zero.append(num)

# Count zeros
zero_count = nums.count(0)

# Add zeros at end
result = non_zero + [0]*zero_count

print(result)
