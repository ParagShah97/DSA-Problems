# https://leetcode.com/problems/lru-cache/
# Time Complexity: O(1)
# Space Complexity: O(N)

# Node class to create doubly linked list.
class Node:
    def __init__(self, key, val):
        self.key =key
        self.val =val
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap =  capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # We can remove the node by getting the prev and next node and join
    # prev next to next node and next node's prev to prev node.
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev 
    
    # Here the main idea is insering a node between right and prev to right node.
    # So we take ptr point to the prev to right and right.
    # Then we put the new node b/w them
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        prev.next = node
        nxt.prev = node
    
        
    '''
    get()
    If the key present(check in cache) then `remove` the node from DLL and
    `insert` again from the right side showing as recently accessed.
    Though, if the key not present return -1.
    '''
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    '''
    put()
    Here if the key is already present(in cache) then we need to update the
    value of the node, so my approach is remove the node from DLL.
    Create a new Node with key and value, even if the key is already present.
    Now, insert the the new Node to DLL.
    Here we check if the cache size > cap then we remove the LRU node.
    We know that left will point to the LRU node, we take that node
    and remove it from DLL and cache.
    '''
    def put(self, key: int, value: int) -> None:
        # Here if key already exists then we need to update the value.
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)