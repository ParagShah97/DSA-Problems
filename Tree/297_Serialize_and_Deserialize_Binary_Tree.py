# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Time Complexity: O(N)
# Space Complexity: O(N)

# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:


    """
    Intuition:
    In Serialze function, we first get the root of the tree, here I am doing a level order traversal.
    First take a queue and add the root element to it.
    Till the queue is not empty, pop the element out, if node is not None then append the node.val else "N"
    If the node (left node) then we have to add the None values to the queue, so at last we will be having 
    ser array as [1,2,3, N, N, 4,5,N,N,N,N] return the arr as joined string.

    In Deserailize function:
    First we check if the str is not empty (if empty return None)
    Then again convert it to an array using split.
    Here to reconstruct tree we need to have a queue.
    First add the 1st element from the arr by creating the treenode to queue.
    Take a pointer start from 0.
    While queue not empty. (pop the node from the queue)
    Then we create a node for next 2 element from the arr (if not 'N')
    then add the node_l and ndoe_r to the queue and attach it to left & 
    right ptr of node (popped ele).
    At last return the root element.
    """
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
    #    Base case in case the root is empty.
        if not root:
            return ""
        
         # Let's go with level order traversal.
        que = deque()
        que.append(root)
        ser = []

        while que:
            # if not self.checkQue(que):
            #     break
            que_len = len(que)
            for _ in range(que_len):
                node = que.popleft()
                if node:
                    ser.append(str(node.val))
                else:
                    ser.append("N")
                if node:
                    que.append(node.left)
                    que.append(node.right)
        # print(ser)
        return ",".join(ser)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print("-->",data)
        if not data:
            return None
        arr = data.split(",")
        que = deque()

        root = TreeNode(arr[0])
        que.append(root)
        ptr = 0

        while que:
            node = que.popleft()

            node_l = None
            node_r = None

            ptr+=1
            if arr[ptr] != 'N':
                node_l = TreeNode(arr[ptr])
                que.append(node_l)

            ptr+=1
            if arr[ptr] != 'N':
                node_r = TreeNode(arr[ptr])
                que.append(node_r)

            node.left = node_l
            node.right = node_r
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))