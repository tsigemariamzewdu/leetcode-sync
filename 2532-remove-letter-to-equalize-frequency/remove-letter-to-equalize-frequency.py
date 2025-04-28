class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        values = sorted(freq.values())
        
       
        if all(v == 1 for v in values):
            return True
            
        
        if len(set(values)) == 1:
            return values[0] == 1 or len(values) == 1
            
      
        if values[0] == 1 and all(v == values[1] for v in values[1:]):
            return True
            
       
        if values[-1] - values[-2] == 1 and all(v == values[0] for v in values[:-1]):
            return True
            
        return False