class Solution:
    def intToRoman(self, num: int) -> str:
        n=len(str(num))-1
        nums=list(map(int,list(str(num))))
        result=[]
        intToRoman = {
            1:"I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        for num in nums:
            p=pow(10,n)
            if num*p in intToRoman:
                result.append(intToRoman[num*p])
            elif num*p==40:
                result.append("XL")
            elif num*p==400:
                result.append("CD")
            elif num*p==4:
                result.append("IV")
            elif num*p==90:
                result.append("XC")
            elif num*p==900:
                result.append("CM")
            elif num*p==9:
                result.append("IX")

            elif num<5:
                result.append(intToRoman[p]*num)
            elif num>5:
                result.append(intToRoman[5*p])
                result.append((num-5)*intToRoman[p])
            n-=1
        return "".join(result)





        