
# 创建函数 analyze_list(lst) 返回包含列表最大值、最小值、平均值的字典
def analyze_list(L:list)->dict:
    ret_dic = dict(max=L[0], min=L[0], average=0.0)
    for i in L:
        if ret_dic['max'] < i:
            ret_dic['max'] = i
        elif ret_dic['min'] > i:
            ret_dic['min'] = i
    ret_dic['average'] = (ret_dic['max'] + ret_dic['min']) / 2.0
    return ret_dic


# 实现函数 word_frequency(text) 统计文本中单词频率（忽略大小写和标点）
def is_word(c:str)->bool:
    return ('A' <= c <= 'Z') or('a' <= c <= 'z')
def word_frequency(text:str)->dict[str,int]:
    chars = list()
    for c in text:
        if c not in chars and is_word(c):
            chars.append(c)
    
    ret_dic = dict().fromkeys(chars,0)
    for c in text:
        if c in ret_dic:
            ret_dic[c]+=1
    return ret_dic

def word_frequency_using_set(text:str)->dict[str,int]:
    char_set = {c for c in text if is_word(c)}
    ret_dic = dict().fromkeys(char_set,0)
    for c in text:
        if c in ret_dic:
            ret_dic[c]+=1
    return ret_dic


# 编写函数 process_data(data)，参数为字典列表，返回按指定键排序的新列表
def process_data(data:list[dict]):
    data.sort(key=lambda d:d['age'])
    return data


# 创建函数 calculator(operator, *nums) 实现基础计算器功能（+ - * /）
def _tuple_add(tup:tuple):
    result = 0
    for i in tup:
        result+=i
    return result
def _tuple_sub(tup:tuple):
    result = tup[0] + tup[0]
    for i in tup:
        result-=i
    return result
def _tuple_mul(tup:tuple):
    result = 1
    for i in tup:
        result*=i
    return result
def _tuple_div(tup:tuple):
    result = tup[0] * tup[0]
    for i in tup:
        if i == 0:
            raise ValueError('Divisor cannot be zero')
        result/=i
    return result
def calculator(operator, *nums):
    match operator:
        case '+':
            return _tuple_add(nums)
        case '-':
            return _tuple_sub(nums)
        case '*':
            return _tuple_mul(nums)
        case '/':
            return _tuple_div(nums)


# 实现函数 matrix_multiply(a, b) 计算两个矩阵的乘积
def _list_mul(L1:list, L2:list)->list:
    result:list = list()
    for i in range(len(L1)):
        result.append(L1[i] * L2[i])
    return result

def matrix_multiply(L1:list[list], L2:list[list])->list[list]:
    result:list[list] = list()
    for i in range(len(L1)):
        result.append(_list_mul(L1[i], L2[i]))
    return result


# 定义函数 validate_password(password) 检查密码强度（长度、大小写、数字）
def validate_password(pwd:str)->int:
    Len, Up,Low,Num  = False, False,False,False
    grade:int = 1
    Len = len(pwd) > 8
    for c in pwd:
        if c.isnumeric():
            Num=True
        if c.isupper():
            Up = True
        else:
            Low = True
    return grade + Len + Up + Low + Num

# 创建函数 group_by_key(data, key)，将字典列表按指定键分组
def group_by_key(data:list[dict], key:str):
    new_dict:dict[int, list[dict[str,int]]] = dict()
    for dic in data:
        if dic[key] in new_dict:
            new_dict[dic[key]].append(dic)
        else:
            new_dict[dic[key]] = [dic]
    return new_dict


# 实现函数 fibonacci_sequence(n) 生成斐波那契数列前n项
def fibonacci_sequence(n:int)->list[int]:
    if n == 0:
        return [0]
    result:list[int] = [0,1]
    for i in range(2, n + 1):
        result.append(result[i - 1] + result[i - 2])
    return result

# 编写函数 nested_dict_access(d, keys) 通过键列表访问嵌套字典值
def nested_dict_access(dic:dict, keys:list[str]):
    for k in keys:
        print(dic[k])
    
# 创建函数 sort_dict_by_value(d, reverse=False) 按值排序字典
def add_dic(left:dict, middle:dict, right:dict)->dict:
    left.update(middle)
    left.update(right)
    return left
def sort_dict_by_value(dic:dict, reverse=False):
    if len(dic) <= 1:
        return dic
    for i in dic:
        pivot = dic[i]
        break
    if reverse:
        left = {k:dic[k] for k in dic if dic[k] > pivot} # type: ignore
        middle = {k:dic[k] for k in dic if dic[k] == pivot} # type: ignore
        right = {k:dic[k] for k in dic if dic[k] < pivot} # type: ignore
        return add_dic(
            sort_dict_by_value(left,reverse),
            middle,
            sort_dict_by_value(right, reverse)
            )
    else:
        left = {k:dic[k] for k in dic if dic[k] < pivot} # type: ignore
        middle = {k:dic[k] for k in dic if dic[k] == pivot} # type: ignore
        right = {k:dic[k] for k in dic if dic[k] > pivot} # type: ignore
        return add_dic(
            sort_dict_by_value(left,reverse),
            middle,
            sort_dict_by_value(right, reverse)
            )

    



def run():
    d= {"jiang1":2,"jiang2":3,"jiang3":1,"jiang4":989,"jiang5":14,"jiang6":0}
    print(
        sort_dict_by_value(d, True)
        
    )