class Solution:
   def findComplement(self,num: int) -> int:
    if num == 0:
        return 1 
    
    bit_count = num.bit_length()
    bitmask = (1 << bit_count) - 1
    return num ^ bitmask