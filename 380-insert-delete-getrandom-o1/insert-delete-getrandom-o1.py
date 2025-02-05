class RandomizedSet:

    def __init__(self):
        self.index_map = {}
        self.list_elements = []

    def insert(self, val: int) -> bool:
        if not (val in self.index_map):
            self.index_map[val] = len(self.list_elements)
            self.list_elements.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            remove_index = self.index_map[val]
            self.index_map[self.list_elements[-1]] = remove_index
            self.list_elements[-1], self.list_elements[remove_index] = self.list_elements[remove_index], self.list_elements[-1]

            del self.index_map[self.list_elements[-1]]
            self.list_elements.pop()

            return True
        
        return False

    def getRandom(self) -> int:
        random_index = randint(0,len(self.list_elements)-1)

        return self.list_elements[random_index]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
