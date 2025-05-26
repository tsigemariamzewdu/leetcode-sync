class Solution:
    def bitwiseComplement(self, n: int) -> int:
       
        if n== 0:
            return 1 
        bit_count = n.bit_length()
        bitmask = (1 << bit_count) - 1
        return n ^ bitmask