# https://leetcode.com/problems/insert-delete-getrandom-o1/description
# Time Complexity O(1)
# Space Complexity O(N)
import random


class RandomizedSet:
    """
    Intuition:
    The solution is interesting, we cannot take hashset as set is not indexable so
    we have to keep a hashmap and a list. 
    Hashmap will store the element and the index where it is stored in the list.
    For inserting we just need to add the ele to the map with respective index pos
    in the list.
    For remmoving we have to do following steps.
    First get the index of the element we need to remove.
    get the last value
    at list[index] put last index
    remove last index from the list
    update the map for last index ele to new assigned index.
    delete the removed index from map
    """

    def __init__(self):
        self.numMap = {}
        self.numList = []        

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.numMap[val] = len(self.numList)
        self.numList.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        idx = self.numMap[val]
        lastVal = self.numList[-1]
        self.numList[idx] = lastVal
        self.numList.pop()
        self.numMap[lastVal]=idx
        del self.numMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()