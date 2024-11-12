

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        
        
        prices = []
        max_beauty_at_price = []
        max_beauty = 0
        
        for price, beauty in items:
            max_beauty = max(max_beauty, beauty)
            prices.append(price)
            max_beauty_at_price.append(max_beauty)
        
       
        def binary_search_max_price(prices, query):
            left, right = 0, len(prices) - 1
            best_idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                if prices[mid] <= query:
                    best_idx = mid   
                    left = mid + 1   
                else:
                    right = mid - 1  
            
            return best_idx  
       
        result = []
        for query in queries:
            idx = binary_search_max_price(prices, query)
            
           
            if idx >= 0:
                result.append(max_beauty_at_price[idx])
            else:
                result.append(0)
        
        return result
