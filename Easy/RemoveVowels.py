class solution:
    def remv(s,lst):
        for i in s:
            if i in lst:
                s = s.replace(i,"")
        return s

    s = "GeeksforGeeks - A Computer Science Portal for Geeks"
    lst = ["a", "e", "i", "o", "u"]


    print(remv(s,lst))


print("\n")

class solution2:
    def IP(address):
        a = "."
        for i in address:
            if a in i:
                a = "[.]"
                address = address.replace(i, a)


        return address

    address = "1.1.1.1"
    print(IP(address))
print("\n")

class sol4:
    def jewels(J,S):
        return sum(S.count(j) for j in J)


    J = "aA"
    S = "aAAbbbb"
    print(jewels(J,S))


class spli:
    def rough(d):
        lst = []
        countLR, count = 0,0
        for i in d:
            countLR +=1 if i == "L" else -1
            if countLR == 0:
                count +=1




        return count


    d = "RLRRLLRLRL"
    lst = [1,2,3,4,5]
    print(lst[::-1])


    print(rough(d))


class Solution6:
    def flipAndInvertImage(A):
        # flipping horizontally
        #return [[1 - i for i in row[::-1]] for row in A]
        return A.reverse()


    A = [1,2,3,4,5]
    print(flipAndInvertImage(A))


class new:
    def twosum(nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
                print(dict)
            else:
                return [dict[target - nums[i]],i]


    target = 9
    nums = [1,2,4,5,7]
    print(twosum(nums, target))


    def twosumbrute(nums,target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i,j]


    target = 9
    nums = [1, 2, 4, 5]
    print(twosumbrute(nums,target))

class Solution9:
    def reverseString( s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

            helper(0, len(s) - 1)

    s = ["h","e","l","l","o"]
    print(reverseString(s))



