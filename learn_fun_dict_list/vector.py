

# 定义函数 reverse_list(lst) 返回反转后的列表
def reverse_list(Li:list)->list:
    return Li[::-1]

# 实现函数 remove_duplicates(lst) 去除列表重复项
def remove_duplicates_set(Li:list)->list:
    s = set(Li)
    return list(s)

def remove_duplicates(Li:list)->list:
    L = []
    for i in Li:
        if i not in L:
            L.append(i)
    return L

# 创建函数 count_occurrences(lst, item) 统计元素出现次数
def count_occurrences(L:list, item:int)->int:
    return L.count(item)

# 编写函数 flatten_list(nested_list) 展开嵌套列表（单层嵌套）
def flatten_list(Li:list[list])->list:
    new_list = list()
    for i in Li:
        new_list.extend(i)
    return new_list

# 实现函数 rotate_list(lst, n) 将列表元素循环右移n位
def rotate_list(Li:list, n:int)->list:
    if n == 0 or len(Li) <= 1 or len(Li) == n:
        return Li
    if n > len(Li):
        n = n % len(Li)
    new_list = Li[n:]
    print(new_list)
    new_list.extend( Li[:n])
    return new_list

# 定义函数 chunk_list(lst, size) 将列表分割成指定大小的子列表
def chunk_list(Li:list, size:int)->list[list]:
    if size >= len(Li):
        return [Li]
    if size == 0:
        return [[]]
    new_list = list()
    current, end  = 0,0
    while current + size < len(Li):
        end = current + size
        new_list.append(Li[current:end])
        current = end
    new_list.append(Li[current:])
    return new_list


# 创建函数 find_common(a, b) 返回两个列表的交集
def find_common(L1:list, L2:list)->list:
    new_list = list()
    for i in L1:
        if i in L2:
            new_list.append(i)
    return new_list

# 实现函数 add_matrices(a, b) 计算两个二维列表的矩阵加法
def add_matrices(L1:list[list], L2:list[list])->list[list]:
    new_list = list()
    for i1,i2 in zip(L1, L2):
        t_list = list()
        for v1,v2 in zip(i1,i2):
            t_list.append(v1 + v2)
        new_list.append(t_list)
    return new_list

# 编写函数 swap_min_max(lst) 交换列表中最小值和最大值
def swap_min_max(L:list):
    L.sort()
    L[0],L[len(L) - 1] = L[len(L) - 1], L[0]
    # return L

# 创建函数 shift_zeros(lst) 将列表所有零移动到末尾
def shift_zeros(L:list[int]):
    zero_count = 0
    i = 0
    while i < len(L):
        if L[i] == 0:
            del L[i]
            zero_count+=1
        else:
            i+=1
    for _ in range(zero_count):
        L.append(0)
    print(L)

def shift_zeros_new_list(L:list[int]):
    new_list = [i for i in L if i != 0]
    new_list += [0 for _ in range(len(L) - len(new_list))]
    print(new_list)

def run():
    L1 = [[1,2,3],[4,5,6]]
    L2 = [[1,2,3],[4,5,6]]
    L3 = [1,2,3,4,5,6]
    shift_zeros([0,0,0,0,1,2,0,3])
    print(
    )