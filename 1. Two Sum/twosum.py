def two_sum(nums, target):
    hash_table = dict([(nums[i], i) for i in range(len(nums))])
    for i in range(len(nums)):
        if target - nums[i] in hash_table and hash_table[target - nums[i]] != i:
            return [hash_table[target - nums[i]], i]
