class solution:
    def findmissing(nums):
        nums.sort()
        while i < len(nums):
            if nums[i] != i:
                return i
            return i+1
