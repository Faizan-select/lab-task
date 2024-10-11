#!/usr/bin/env python
# coding: utf-8

# In[7]:


def BFS(root):
    queue = []
    queue.append(root)
    
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.pop(0)
            print(node.val)
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
  


# In[27]:


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def BFS(root):
    if not root:
        return
    
    queue = []
    queue.append(root)     
    
    while queue:
        node = queue.pop(0) 
        print(node.value)      
        
        
        if node.left:
            queue.append(node.left)  
        if node.right:
            queue.append(node.right)  

root = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')

root.left = nodeB
root.right = nodeC
nodeB.left = nodeD
nodeB.right = nodeE
nodeC.left = nodeF
nodeC.right = nodeG

BFS(root)


# In[ ]:




