#!/usr/bin/env python
# coding: utf-8

# In[20]:


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


root = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')


root.children = [nodeB, nodeC]
nodeB.children = [nodeD, nodeE]
nodeC.children = [nodeF, nodeG]


def dfs_with_node(visited, node, goal):
    if node not in visited:
        visited.append(node)
        if node.value == goal:
            return "Goal achieved."

       
        for child in node.children:
            result = dfs_with_node(visited, child, goal)
            if result:
                return result
visited_nodes = []
result = dfs_with_node(visited_nodes, root, 'F')
print("Visited Nodes:", [node.value for node in visited_nodes])
if result:
    print(result)
else:
    print("Goal not found.")


# In[ ]:




