import sys
import os
# 将项目根目录添加到 sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)
from RunTime import runtime # type: ignore

class Node:
    cur_value:int
    left_node:'Node'
    right_node:'Node'
    import json
    def __init__(self) -> None:
        self.cur_value = None # type: ignore
        self.left_node = None # type: ignore
        self.right_node = None # type: ignore
    
    def has_value(self):
        return  self.cur_value is not None

class Tree:
    def __init__(self) -> None:
        self.root:Node = Node()
    @runtime
    def insert(self,v:int):
        if not self.root.has_value():
            self.root.cur_value = v
        else:
            cur_node:Node = self.root
            while cur_node.has_value():
                if cur_node.cur_value > v:
                    if cur_node.left_node is None:
                        cur_node.left_node = Node()
                    cur_node = cur_node.left_node
                else:
                    if cur_node.right_node is None:
                        cur_node.right_node = Node()
                    cur_node = cur_node.right_node
            cur_node.cur_value = v
    def print_(self, node:Node):
        if node.has_value():
            print(node.cur_value, end='  ')
        if node.left_node is not None:
            self.print_(node.left_node)
        if node.right_node is not None:
            self.print_(node.right_node)

    def print_all(self):
        if self.root.has_value():
            self.print_(self.root)


@runtime
def tree_traversal(tree:Tree):
    from collections import deque
    if tree is None or not tree.root.has_value():
        return
    que = deque([tree.root])
    s = ''
    while que:
        node = que.popleft()
        s+= (str(node.cur_value)+' ')
        if node.left_node is not None:
            que.append(node.left_node)
        if node.right_node is not None:
            que.append(node.right_node)
    print(s)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    older:bool = True
    func_ = None
    def __hash__(self): 
        return hash((self.name, self.age))  # 组合 name 和 age 进行哈希

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name and self.age == other.age

    def __str__(self) -> str:
        return f'<name:{self.name}>, <age:{self.age}>'
    
    def __format__(self, format_spec: str) -> str:
        match format_spec:
            case 'name':
                return f'<name:{self.name}>'
            case 'age':
                return f'<age:{self.age}>'
            case _:
                return f'<name:{self.name}>, <age:{self.age}>'
    def __repr__(self) -> str:
        return self.__str__()
        
    
def test(self):
    print(f'test:{self}')

def test_tree():
    # from random import randint
    # tree = Tree()
    # # x = [94,10,77,61,1,62,4,27,81,49]
    # for i in range(100000):
    #     x = randint(1,10000)
    #     tree.insert(x)
    #     # print(x, end=',')
    # print('\n=====================================')
    # tree_traversal(tree)
    
    # 测试哈希存储
    p1 = Person("Alice", 30)
    p2 = Person("Bob", 25)
    p3 = Person("Alice", 30)  # 和 p1 相同
    print(p1.older)
    Person.older = False
    print(p1.older)
    p1.func_ = test # type: ignore
    p1.func_(p1) # type: ignore








if __name__ == '__main__':
    from dis import dis
    # dis(test_tree)  
    test_tree()    