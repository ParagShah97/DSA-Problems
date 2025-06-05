# https://leetcode.com/problems/binary-search-tree-iterator
# Time Complexity: AmortizedO(1)
# Space Complexity: O(H) Where H Is The Height Of The Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class BSTIterator:
    """
    Intuition:
    Approach 1: Not implemented
    We can call the inorder traversal from the constructor and store
    the inorder in the list, then we can normally make the hasnext and
    next function, but the time complexity will be O(N) and space O(N).

    Approach 2:
    We can do inorder using iteration method.
    The main idea is in the constructor move to the left nodes and add
    them to the stack.
    In hasNext function we check if the stack is not empty then return
    True else False.
    In next function, we first pop the top element from the stack(node)
    then we check if right node exists, if yes then we add that node
    to the stack and all the left nodes from that right node to the
    stack., at last return the val of the current node popout from stack.
    """

    def __init__(self, root: Optional[TreeNode]):
        self.stack= []

        while root:
            self.stack.append(root)
            root = root.left
        

    def next(self) -> int:
        ret = self.stack.pop()
        itr = ret.right
        while itr:
            self.stack.append(itr)
            itr = itr.left
        return ret.val
        

    def hasNext(self) -> bool:
        return self.stack != []
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()