class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        str_cities=set()
        for path in paths:
            str_cities.add(path[0])
        for path in paths:
            if path[1] not in str_cities:
                return path[1]