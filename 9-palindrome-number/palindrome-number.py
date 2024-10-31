class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversedNum=0
        myNum=x
        while myNum>0:
            digit=myNum%10
            reversedNum=reversedNum*10+digit
            myNum=myNum//10
        value= x==reversedNum
        return value

        