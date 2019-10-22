class Solution:

    def reme(nums,val):
        nextpos = 0
        for i in nums:
            if i != val:
                nums[nextpos] = i
                nextpos +=1
        return nextpos

    nums = [1,1,2,3,4]
    val = 1
    print(reme(nums,val))

    def movezeroes(nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count +=1

        for i in range(count, len(nums)):
            nums[i] = 0
        return nums









    nums = [0,1,0,3,12]
    print(movezeroes(nums))


    def FUC(s):
        dict = {}
        for i in s:
            if i in dict:
                dict[i] +=1
            else:
                dict[i] =1

        for i,c in enumerate(s):
            if dict[c] == 1:
                return i


    s = 'leetcodelove'
    print(FUC(s))

    def maj(nums):
        dict = {}
        for i in nums:
            if i in dict:

                dict[i] +=1
            else:
                dict[i] = 1
        for i,c  in enumerate(nums):
            if dict[c] > len(nums)//2:
                return nums[i]

    nums = [2,2,1,1,1,2,2]
    print(maj(nums))

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits


if __name__ == "__main__":
    print(Solution().plusOne([9, 9, 9]))


    def findmissin(nums):

        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] +1:
                return nums[i-1] +1

    nums  = [9,6,4,2,3,5,7,0,1]
    print(findmissin(nums))




