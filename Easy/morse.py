#class solution:
    #def morse(lst):
        #lst = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]


class sl:
    def selfdivide(left, right):
        def check(n):
            for i in str(n):
                if i == '0' or n % int(i) > 0:
                    return False
            return True

        lst  =[]
        for n in range(left,right+1):
            if check(n):
                lst.append(n)
        return lst
    left,right = 1,22
    print(selfdivide(left,right))




class sn:
    def email(lst):

        s1 = [i.split('+', 1)[0] for i in lst]
        print(s1)
        s2 = [i.split('@', 1)[0] for i in lst]
        s3 = str(s2)
        s4 = str(s1)
        s5 = "."
        for i in s4:
            if s5 in i:
                s4 = s4.replace(s5,"")

        return s4, s2

    lst = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(email(lst))




