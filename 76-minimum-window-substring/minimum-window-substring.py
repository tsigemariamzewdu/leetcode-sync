from collections import Counter
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t=Counter(t)
        required=len(dict_t)
        left=0
        n=len(s)
        acquired=0

        
        window_freq=defaultdict(int)
        maximumlength=n+1
        rleft=0
        rright=0

        for right in range(n):
            cur=s[right]
            window_freq[cur]+=1

            if cur in dict_t:
                if window_freq[cur]==dict_t[cur]:
                    acquired+=1
            while acquired==required:
                left_cur=s[left]
                
                if  right -left+1 < maximumlength:
                    maximumlength=right-left+1
                    rleft=left
                    rright=right

                    
                window_freq[left_cur] -= 1
                if left_cur in t:
                    if window_freq[left_cur]<dict_t[left_cur]:
                        acquired -= 1

                left += 1
            



        if maximumlength==n+1:
            return ""
        else:
            return s[rleft:rright+1]


        