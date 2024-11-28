class Solution:
    def isPalindrome(self, x: int) -> bool:
        xtest = str(x)
        if len(xtest) == 0 and x >= 0:
            return ("true")
        else :
            if xtest == xtest[::-1] and x >= 0 :
                return ("true")
            else:
                print("false")