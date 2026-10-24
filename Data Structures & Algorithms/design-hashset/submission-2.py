class MyHashSet:

    def __init__(self):
        self.slots = [None] * 1000000
        

    def add(self, key: int) -> None:
        if key == 0:
            self.slots[0] = key
        self.slots[key-1] = key

    def remove(self, key: int) -> None:
        self.slots[key-1] = None

    def contains(self, key: int) -> bool:
        if self.slots[key-1] is None:
            return False
        return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)