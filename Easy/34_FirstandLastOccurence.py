class solution:
    
    def searchRange(nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        for j in range(len(nums)-1,-1,-1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx,right_idx]

    

