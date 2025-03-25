class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        path=[]
        ans=[]
        if len(digits)==0:
            return ans
        def backtrack(idx):
            if idx>=len(digits):
                ans.append("".join(path[:]))
                return




            for i in range(len(mapp[digits[idx]])):
                path.append(mapp[digits[idx]][i])
                backtrack(idx+1)
                path.pop()
        backtrack(0)
        return ans


        