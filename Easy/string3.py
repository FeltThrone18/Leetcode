
class Solution:
    def myAtoi(s):

        s = s.replace(" ", "")
        maxa = 2147483647
        mina = -2147483648


        if s[0] == '-':
            sign = '-'
        else:
            sign = ""

        a = "."


        if a not in s:
            if s[0].isdigit() == True or s[0] == '-':
                s = "".join(i for i in s if i.isdigit())
                if int(s) in range(mina,maxa):
                    s = sign + s

                    return s
                else:
                    return mina
            return 0
        return int(float(s))



    s = '-91283472332'
    print(myAtoi(s))