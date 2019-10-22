class solution:

    def anagram(s,t):
        lst1,lst2 = list(s), list(t)
        lst2.sort()
        lst1.sort()
        return lst1 == lst2


    s = ''
    t = ''
    print(anagram(s,t))


    def FUC(s):
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i,c in enumerate(s):
            if dict[c] == 1:
                return i
        return -1

    s = 'loveleetcode'
    print(FUC(s))

    def findmissin(s):
        s.sort()
        for i in range(s[0], s[-1]+1):
            if i not in s:
                return i



    s = [1,2,3,4,6]
    print(findmissin(s))

    def firstuniq(s):
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for a,b in enumerate(s):
            if dict[b] == 1:
                return a
        return -1

    s = 'loveleetcode'
    print(firstuniq(s))


    def selfdiv(left,right):
        def check(n):
            for i in str(n):
                if i == '0' or n% int(i) > 0:
                    return False
            return True

        lst = []
        for n in range(left,right+1):
            if check(n):
                lst.append(n)
        return lst

    left,right = 1,22
    print(selfdiv(left,right))

    def romantoint(num):
        dict = dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        nex = 0
        sum = 0
        for i in num[::-1]:
            curr = dict[i]
            if nex > curr:
                sum -= curr
            else:
                sum += curr
            nex = curr
        return sum

    num = 'VII'
    print(romantoint(num))

    def isPalindrome( s):
        s_alnum = list(filter(str.isalnum, s.lower()))
        d = "".join(i for i in s if i.isalnum())
        print(d)
        mid = len(s_alnum) // 2
        for i in range(mid):
            if s_alnum[i] != s_alnum[-i - 1]:
                return False
        return True
    s = 'racecar...12121%%%'
    print(isPalindrome(s))



    def pali(s):
        mid = len(s)//2
        for i in range(mid):
            if s[i] != s[-i -1]:
                return False
        return True
    s = 'racecar'
    print(pali(s))


    def palin(s):
        s= ''.join(i for i in s if i.isalnum()).lower()
        if s == s[::-1]:
            return True
        return False


    s = 'A racecar is : nascar'
    print(palin(s))

    def anan(s,t):
        s = "".join(i for i in s if i.isalnum()).lower()
        t = "".join(i for i in t if i.isalnum()).lower()

        if len(s) != len(t):
            return False
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        dict1 = dict.fromkeys(list(alphabet),0)
        dict2 = dict.fromkeys(list(alphabet),0)


        for i in range(len(s)):
            dict1[s[i]] +=1
            dict2[t[i]] +=1
        return dict1 == dict2

    s = ''
    t = 'Malayalam'
    print(anan(s,t))







