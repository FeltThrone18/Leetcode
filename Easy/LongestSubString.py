def longestSS(s):
    lst = []
    max_length  = 0
    for i in s:
        if i in lst:
            lst = lst[lst.index(i)+1:]

        lst.append(i)
        max_length = max(max_length, len(lst))


    return max_length

s = "aab"
print(longestSS(s))




class sol:
    def IP(s):
        a = "."
        for i in s:
            if a in i:
                a = "[.]"
                s = s.replace(i,a)
        return s
    s = "1.1.1.1"
    print(IP(s))

class sol1:
    def LL(s):
        count1, count2 = 0,0
        for i in s:
            count1 +=1 if i == "L" else -1
            if count1 == 0:
                count2 +=1
        return count2

    s = "RLRRLLRLRL"
    print(LL(s))


class sol3:
    def uniqe(arr):
        lst = []
        num = set(arr)
        for i in num:
            cnt =  arr.count(i)
            if cnt in lst:
                return False
            lst.append(cnt)
        return True

    arr = [1,2,2,1,1,3]
    print(uniqe(arr))


#Input: J = "aA", S = "aAAbbbb"

    def numJewelsInStones( J, S):
        setJ = set(J)
        return sum(s in setJ for s in S)

    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones(J, S))


    def findmissing(lst):
        for i in range(lst[0], lst[-1]+1):
            if i not in lst:
                return i
    lst = [1,2,3,4,5,6,7,8,10]
    print(findmissing(lst))

    def remvowels(s):
        lst = ["a","e","i","o","u"]
        for i in s:
            if i in lst:
                s = s.replace(i,"")
        return s
    s= "hello"
    print(remvowels(s))

class haha:
    def morse():
        mydict = { 'a':".-", 'b': "-...", 'c': "-.-.",'d': "-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':".."}
        return mydict['b','e','a']
    print(morse())