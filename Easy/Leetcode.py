class solution:
    def findmissing(lst):
        for i in range(lst[0],lst[-1]+1):
            if i not in lst:
                return i
    print(("\n"))

    print("The missing number in the list is ", findmissing(lst= [1,2,3,4,6]))

print("\n")


class solution2:
    def findpos(lst, target):
        for i in range(len(lst)):
            if lst[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        for j in range(len(lst)-1,-1,-1):
            if lst[j] == target:
                right_idx = j
                break

        return [left_idx,right_idx]

    lst = [1,2,3,4,5,6,6,7]
    target = 6
    print("The first and last position of the target in the list are", findpos(lst, target))

print("\n")

class solution3:
    def twosum(num,target):
        dict = {}
        for i in range(len(num)):
            if target-num[i] not in dict:
                dict[num[i]] = i
            else:
                return [dict[target-num[i]], i]

    num = [1,2,3,4,9]
    target = 7
    print("The target can be found by adding the following positions in the list" , twosum(num, target))


print("\n")


