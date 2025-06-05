

# 实现函数 compose(f, g) 返回函数组合 f(g(x))
def compose(f,g,*args):
    return f(g(*args))

# 实现函数 partial_apply(func, *args) 返回部分应用函数
def partial_apply(func, *args1):
    def fun(*args2):
        func(*args1, *args2)
    return fun

# 创建函数 dict_diff(d1, d2) 比较两个字典的差异
def dict_diff(d1:dict, d2:dict):
    return set(d1.items()) ^ set(d2.items())

# 实现函数 deep_merge(d1, d2) 递归合并嵌套字典
def deep_merge(d1:dict, d2:dict):
    for k,v in d2.items():
        if k in d1 and isinstance(d1[k], dict) and isinstance(v, dict):
            deep_merge(d1[k], v)
        else:
            d1[k] = v
    return d1

# 定义函数 pipeline(data, *funcs) 按顺序应用多个函数
def pipeline(data, *funcs):
    for func in funcs:
        func(data)
            

# 实现函数 tree_traversal(tree) 进行二叉树层序遍历
def tree_traversal(tree):
    pass


# 编写函数 handle_exceptions(func) 捕获并打印函数异常信息
def handle_exceptions(func):
    try:
        func()
    except TypeError as e:
        print(e)
    except:
        print('Unkonw exception')

class Tree:
    class Node:
        def __init__(self,left:'Node'=None, right:'Node'=None): # type: ignore
            self.cur = None
            self.left_node = left
            self.right_node = right
            self.root = None

    root:Node|None
    cur_node:Node|None

    def __init__(self) -> None:
        self.root = self.Node()
        self.cur_node = self.root
    
    def inseart(self,v:int):
        if self.cur_node.cur == None: # type: ignore
            self.cur_node = self.Node(v)
        elif self.cur_node.left_node == None: # type: ignore
            self.cur_node.left_node = self.Node(v) # type: ignore
        elif self.cur_node.right_node == None: # type: ignore
            self.cur_node.right_node = self.Node(v) # type: ignore
        




def run():
    c:int = None # type: ignore
    print(c == None)