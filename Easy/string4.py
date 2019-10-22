import math

class solution:
    def st(s):
        a = "."
        if a in s:
            return int(float(s))
        return s
    s = "3.13"
    print(st(s))


    def cnt(s):
        b = s
        s = list(dict.fromkeys(s))

        if len(b) != len(s):
            return True
        else:
            return False






    s = [1,2,3,4]
    print(cnt(s))


    def removed(nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] != nums[count]:
                count +=1
                nums[count] = nums[i]

        return count+1

    nums = [1,1,2]
    print(removed(nums))

    def removeele(nums,val):
        for i in range(len(nums)):
            if val in nums:
                nums[i] = +1

                return len(nums)
            return len(nums)

    nums = [0,1,2,2,3,0,4,2]
    val = 2


    def mysqrt(x : int):
        start = 1
        right = x/2
        if x < 2:
            return x
        while start <= right:
            mid = start + (right -start)//2
            if mid > x/mid:
                right = mid -1
            else:
                start = mid +1
        return start -1


    x = 25
    print(mysqrt(x))


    def twosum(x,target):
        dict = {}
        for i in range(len(x)):
            if target - x[i] not in dict:
                dict[x[i]] = i
            else:
                return [dict[target-x[i]],i]

    x= [1,2,4,5]
    target = 6
    print(twosum(x,target))




