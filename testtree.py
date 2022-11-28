class TreeNode:

    def __init__(self,data: int):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
                    self.left.parent = self
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
                    self.right.parent = self
        else:
            self.data = data
            
def height(root):
    if not root:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1

def get_level_item(root, level, res=[], level_res=[], curr_depth=0):
    if not root:
        return res, level_res
    if level == 0:
        res.append(root.data)
        level_res.append(curr_depth)
        return res, level_res
    elif level > 0:
        get_level_item(root.left, level - 1, res, level_res, curr_depth + 1)
        get_level_item(root.right, level - 1, res, level_res, curr_depth + 1)
        
# def bfs(root):
#     result = []
#     h = height(root)
    
#     for i in range(h):
#         result.append(get_level_item(root, i))

#     #print("LEVEL items: ", )
#     return result[0]
def bfs(root):
    level_order_keys = []
    levels = []
    h = height(root)
    #result.append(get_level_item(root, 0))

    for i in range(h):
        curr = get_level_item(root, i)
        if(curr):
            level_order_keys.append(curr[0])
            levels.append(curr[1])
    #print("LEVEL items: ", )
    return level_order_keys[0], levels[0]
def get_level_order_keys_and_levels(arr):
    root = TreeNode(arr.pop(0))
    for elem in arr:
        root.insert(elem)
    level_order_keys, levels = bfs(root)
    return level_order_keys, levels

def solution():
    preorder_keys = list(map(int, input().split()))
    level_order_keys, levels = get_level_order_keys_and_levels(preorder_keys)
    #print(level_order_keys)
    print(' '.join(map(str, level_order_keys)))
    print(' '.join(map(str, levels)))

solution()