# from decimal import Decimal

# 定义一个函数 greet(name)，返回字符串 "Hello, [name]!"
def greet(name:str)->str:
    return f'Hello, [{name}]!'

# 创建函数 calculate_area(radius)，计算并返回圆的面积（π取3.14）
def calculate_area(radius:int)->float:
    return 3.14 * (radius**2)

# 实现函数 is_even(num)，判断数字是否为偶数
def is_even(num:int)->bool:
    return (num % 2 == 0)

# 编写带默认参数的函数 create_user(name, age, city="Unknown")，返回用户信息字典
def create_user(name:str, age:int, city='Unknown')->dict:
    return {'name':name, 'age':age, 'city':city}

# 用 *args 实现函数 sum_all(*numbers)，计算任意数量参数的和
def sum_all(*numbers)->int:
    sum:int = 0
    for i in numbers:
        sum += i
    return sum

# 用 **kwargs 实现函数 print_info(**info)，打印键值对信息
def print_info(**info):
    print(info)

# 创建函数 apply_discount(price, discount=0.1)，计算打折后价格
def apply_discount(price:float, discount=0.1)->float:
    return price * (1 - discount)

# 实现函数 find_max(a, b, c)，返回三个数中的最大值
def _max(num1:int, num2:int)->int:
    if num1 >= num2:
        return num1
    else:
        return num2
def find_max(num1:int, num2:int, num3:int)->int:
    return _max(_max(num1, num2),num3)


# 编写递归函数 factorial(n) 计算阶乘
def factorial(n:int)->int:
    if n == 1:
        return 1
    return n * factorial(n -1)

# 创建函数 format_text(text, upper=False)，根据参数决定是否返回大写文本
def format_text(text:str, upper:bool=False)->str:
    if upper:
        return text.upper()
    return text












def run():
    print(
        format_text('jiang',True)
        )