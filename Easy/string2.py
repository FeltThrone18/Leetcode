
from collections import Counter
class solution:
    def romantoint(s):
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        prev = 0

        for i in s[::-1]:
            curr = dict[i]
            if prev < curr:
                sum += curr
            else:
                sum -= curr
            prev = curr
        return sum


    s = 'IV'
    print(romantoint(s))



    def missing(nums):
        nums.sort()
        for i in range(nums[0], nums[-1]+1):

            if i not in nums:
                return i
            elif nums == [0]:
                return 1

    nums = [1,2,3,5]
    print(missing(nums))


    def reverseint(x):
        if x > 0:
            a = int(str(x)[::-1])
        elif x <= 0:
            a = -1* int(str(x*-1)[::-1])
        mina = -2**31
        maxa = 2**31 -1
        if a not in range(mina, maxa):
            return 0
        else:
            return a

    x = -123
    print(reverseint(x))



    def uniq(s):
        dict = {}
        for i in s:
            if i in dict:
                dict[i] +=1
            else:
                dict[i] = 1
        for i,c in enumerate(s):
            if dict[c] == 1:
                return  i
        return -1
    s = 'loveleetcodee'
    print("The first unique character is: ",uniq(s))



    def FUC(s):
        dict = {}
        for i in s:
            if i in dict:
                dict[i] +=1
            else:
                dict[i] = 1

        for c,i in enumerate(s):
            if dict[i] == 1:
                return c

        return -1

    s = 'loveleetcode'
    print(FUC(s))


    def ispalindrome(s):
        s = "".join(i for i in s if i.isalnum()).lower()
        for i in range(len(s)):
            if s == s[::-1]:
                return True
            elif s == "":
                return True
        return False

    s = ""
    print(ispalindrome(s))

    def strStr(haystack, needle):
        for i in range(len(haystack)):
            if needle in haystack:
                return i
            elif needle == "":
                return 0
            return -1

    haystack = "hello"
    needle = "hello"
    print(strStr(haystack,needle))

    def numJewelsInStones( J, S):
        setJ = set(J)
        for i in range(len(S)):
            return (s[i] in setJ for s in S)

    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones(J, S))

    def length(z):
        if len(z) == 0:
            return ("tatti khalo kutte ki")

    z = ""
    print(length(z))


    def anagram(s,t):
        lst =[]

        for i in range(len(s)-1):
            if i not in lst:
                lst.append(i)
        for j in range(len(t)-1):
            if j in lst:
                return True
        return False

    s = "a"
    t = "a"
    print(anagram(s,t))



    def ana(s,t):
        lst =[]
        for j in range(len(t)):
            if j not in lst:
                lst.append(j)
        for i in range(len(s)):
            if i not in lst:
                print(i)



    s,t  = "rat", "car"
    print(ana(s,t))
