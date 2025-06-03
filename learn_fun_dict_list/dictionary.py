
# 定义函数 merge_dicts(dict1, dict2) 合并两个字典
def merge_dicts(dic1:dict, dic2:dict)->dict:
    new_dic = dic1.copy()
    new_dic.update(dic2.items())
    return new_dic


# 实现函数 invert_dict(d) 交换字典的键和值
def invert_dict(dic:dict)->dict:
    new_dic = dict()
    for k,v in dic.items():
        new_dic[v]=k
    return new_dic

# 创建函数 count_chars(string) 统计字符出现频率
def count_chars(string:str)->dict[str,int]:
    dic:dict[str,int] = dict()
    keys:set[str] = set()
    for s in string:
        keys.add(s)
    dic= dic.fromkeys(keys,0)
    for s in string:
        dic[s] +=1
    return dic


# 编写函数 get_max_value(d) 返回字典中最大值对应的键
def get_max_value(dic:dict[str,int])->str:
    max_str:str = ''
    max_value:int =-1
    L:list = list(dic.values())
    for k in dic:
        if dic[k] > max_value:
            max_value = dic[k]
            max_str = k
    return max_str


# 实现函数 filter_dict(d, threshold) 过滤值大于阈值的键值对
def filter_dic(dic:dict, threshold)->dict:
    return {k:dic[k] for k in dic if dic[k] > threshold}

# 定义函数 dict_to_list(d) 将字典转换为(key, value)元组列表
def dict_to_list(dic:dict)->list[tuple]:
    return list(dic.items())

# 创建函数 sum_dict_values(d) 计算字典所有值的和
def sum_dict_vlaues(dic:dict)->int:
    L:list[int] = list(dic.values())
    return sum(L)


# 实现函数 add_key_value(d, key, value) 安全添加新键值对（存在则跳过）
def add_key_value(dic:dict, key:str, value:int):
    if key not in dic:
        dic[key] = value

# 编写函数 deep_update(d, key, value) 递归更新嵌套字典
def deep_update(dic:dict, key, value) -> dict:
    if isinstance(value, dict):
        new_dic = dict()
        for k in value:
            deep_update(new_dic, k, value[k])
        dic[key] = new_dic
    dic[key] = value
    return dic


# 创建函数 find_key_by_value(d, value) 根据值查找键（多个结果返回列表）
def find_key_by_value(dic:dict, value:int):
    ret_str_or_list = [k for k in dic if dic[k] == value]
    if len(ret_str_or_list) == 1:
        return ret_str_or_list[0]
    return ret_str_or_list



def run():
    d:dict[str,int] = {'jiang':1,'hao':1,'xiang':2}
    d2 = {'hao':2,'xiang':3,'all':{'jianghaoxiang':123,"nihao":{'hello':'world'}}}
    print(
        find_key_by_value(d, 2)

    )