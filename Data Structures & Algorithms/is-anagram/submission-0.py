class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        num=[]
        for i in s:
            num.append(i)
        num = sorted(num)
        num1=[]
        for i in t:
            num1.append(i)
        num1 = sorted(num1)
        if num==num1 :
            return True
        else :
            return False
        



        