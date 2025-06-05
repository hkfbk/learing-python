import sys
import os
# 将项目根目录添加到 sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from RunTime import runtime # type: ignore
from Exercise3.Part1 import run

def get_formatted_name(first:str, last:str)->str:
    full_name = first + " " + last
    return full_name

def is_prime_number(num:int)->bool:
    if num <= 1:
        return False
    for value in range(2, num):
        if (num % value == 0):
            return False
    return True

def print_9X9():
    columns:list[int] = [i for i in range(1,10)]
    for column in columns:
        for rows in range(0,column):
            if rows != 10:
                row =  rows+ 1
                print(f'{row}x{column}={column*row:<3}',end='\t')
        print()
            
def fbnq(num:int)->list[int]:
    if num == 0:
        return [0]
    result:list[int] = [0,1]
    for i in range(2, num + 1):
        result.append(result[i-1] + result[i-2])
    return result
            
def reversed_int(num:int):
    s = str(num)
    s = s[::-1]
    print(s)

def check_str(s:str):
    num_count:int = 0
    str_count:int = 0
    other_count:int = 0
    for i in s:
        if (48 <= ord(i) <= 57):
            num_count+=1
        elif (69 <= ord(i) <= 90):
            str_count+=1
        elif (97 <= ord(i) <= 122):
            str_count+=1
        else:
            other_count+=1
    print(f'num:{num_count}, str:{str_count}, other:{other_count}')
            
def guess_numb():
    from random import randint
    num = randint(1,100)
    for i in range(5):
        user_num = \
            int(input(f'请输入您猜测的数字，您还有{5-i}次机会\n'))
        if (user_num > num):
            print('大了')
        elif (user_num < num):
            print('小了')
        else:
            print('答对了')
            break
            
def rhombus(hight:int):
    column:int = hight //2 + 1 # 纵向中线
    for i in range(1,column):
        print(' '*(column - i) + '*'*i + '*'*(i-1) )
    for i in range(column,0,-1):
        print(' '*(column - i) + '*'*i + '*'*(i-1) )

def unique_list():
    l:list[int] = [1, 2, 3, 2, 4, 1, 5]
    new_list:list[int] = []
    for i in l:
        if i not in new_list:
            new_list.append(i)
    print(new_list)
    
def gcd(num1:int, num2:int)->int:
    if (num2 != 0):
        return gcd(num2, num1 % num2)
    return num1

def check_pwd():
    import re
    while True:
        password = input("请输入密码（至少 8 位，包含字母和数字）： ")
        
        # 检查是否符合要求
        if len(password) >= 8 and re.search(r'[A-Za-z]', password) and re.search(r'\d', password):
            print("密码设置成功！")
            break
        else:
            print("密码不符合要求，请重新输入！")
    
def check_year(num:int):
    return (num % 4 == 0 and num % 100 != 0) or num % 400 == 0

@runtime
def sort_():
    count:int = 0
    l = [
    456, 123, 789, 654, 321, 987, 234, 876, 543, 765,
    111, 222, 333, 444, 555, 666, 777, 888, 999, 101,
    202, 303, 404, 505, 606, 707, 808, 909, 100, 200,
    300, 400, 500, 600, 700, 800, 900, 150, 250, 350,
    450, 550, 650, 750, 850, 950, 120, 220, 320, 420,
    520, 620, 720, 820, 920, 140, 240, 340, 440, 540,
    640, 740, 840, 940, 160, 260, 360, 460, 560, 660,
    760, 860, 960, 180, 280, 380, 480, 580, 680, 780,
    880, 980, 190, 290, 390, 490, 590, 690, 790, 890,
    990, 210, 310, 410, 510, 610, 710, 810, 910, 110
]
    for i in range(len(l)):
        for j in range(len(l)):
            count+=1
            if l[i] < l[j]:
                l[j], l[i] = l[i],l[j]
    print(l)
    print(count)

@runtime
def sort_2():
    count:int = 0
    l = [
    456, 123, 789, 654, 321, 987, 234, 876, 543, 765,
    111, 222, 333, 444, 555, 666, 777, 888, 999, 101,
    202, 303, 404, 505, 606, 707, 808, 909, 100, 200,
    300, 400, 500, 600, 700, 800, 900, 150, 250, 350,
    450, 550, 650, 750, 850, 950, 120, 220, 320, 420,
    520, 620, 720, 820, 920, 140, 240, 340, 440, 540,
    640, 740, 840, 940, 160, 260, 360, 460, 560, 660,
    760, 860, 960, 180, 280, 380, 480, 580, 680, 780,
    880, 980, 190, 290, 390, 490, 590, 690, 790, 890,
    990, 210, 310, 410, 510, 610, 710, 810, 910, 110
]
    for i in range(len(l)):
        for j in range(len(l) -1 -i):
            count+=1
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1],l[j]
    print(l)
    print(count)

@runtime
def bubble_sort():
    arr = [
    456, 123, 789, 654, 321, 987, 234, 876, 543, 765,
    111, 222, 333, 444, 555, 666, 777, 888, 999, 101,
    202, 303, 404, 505, 606, 707, 808, 909, 100, 200,
    300, 400, 500, 600, 700, 800, 900, 150, 250, 350,
    450, 550, 650, 750, 850, 950, 120, 220, 320, 420,
    520, 620, 720, 820, 920, 140, 240, 340, 440, 540,
    640, 740, 840, 940, 160, 260, 360, 460, 560, 660,
    760, 860, 960, 180, 280, 380, 480, 580, 680, 780,
    880, 980, 190, 290, 390, 490, 590, 690, 790, 890,
    990, 210, 310, 410, 510, 610, 710, 810, 910, 110
]
    n = len(arr)
    count:int = 0
    # 遍历所有数组元素
    for i in range(n):
        swapped = False  # 用来标记本轮是否发生交换
        # 最后 i 个元素已经在正确位置，不需要再比较
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                count+=1
        # 如果没有发生交换，说明数组已经有序
        if not swapped:
            break
    print(arr)
    print(count)

@runtime
def quick_sort():
    arr_:list[int] = [
    456, 123, 789, 654, 321, 987, 234, 876, 543, 765,
    111, 222, 333, 444, 555, 666, 777, 888, 999, 101,
    202, 303, 404, 505, 606, 707, 808, 909, 100, 200,
    300, 400, 500, 600, 700, 800, 900, 150, 250, 350,
    450, 550, 650, 750, 850, 950, 120, 220, 320, 420,
    520, 620, 720, 820, 920, 140, 240, 340, 440, 540,
    640, 740, 840, 940, 160, 260, 360, 460, 560, 660,
    760, 860, 960, 180, 280, 380, 480, 580, 680, 780,
    880, 980, 190, 290, 390, 490, 590, 690, 790, 890,
    990, 210, 310, 410, 510, 610, 710, 810, 910, 110
]

    def quick(arr:list[int])->list[int]:
        if len(arr) <= 1:
            return arr
        pivot:int = arr[0]
        left:list[int] = [i for i in arr if i < pivot]        
        middle:list[int] = [i for i in arr if i == pivot]        
        right:list[int] = [i for i in arr if i > pivot]
        return quick(left) + middle + quick(right)
    print(quick(arr_))   

def print_prime_num():
    num1:int = 10
    num2:int = 50
    for i in range(num1, num2+1):
        if is_prime_number(i):
            print(i)

def print_jzt(n:int = 5):
    for index in range(1,n+1):
        list_str = [str(i) for i in range(1, index +1)]
        s:str = ''.join(list_str)
        list_str.pop()
        list_str = list_str[::-1]
        s+=''.join(list_str)
        print(' '*(n-index) + s)
    
def user_get_money():
    initial_money:int = 10_000
    withdraw:int = 0
    input_tip:str = '请输入要取走的金额,输入q/Q退出\n'
    user_in = input()
    while initial_money != 0:
        if user_in == 'q' or user_in == 'Q':
            return
        elif not user_in.isnumeric():
            print('请根据提示输入')
            user_in = input(input_tip)
            continue
        withdraw = int(user_in)
        if withdraw > initial_money:
            print('余额不足')
            return
        initial_money-= withdraw
        print(f'您成功取走{withdraw}元')
        while initial_money != 0:
            con = input('还要继续吗, Y/N\n')
            if (con == 'n' or con == 'N'):
                return
            elif(con == 'Y' or con == 'y'):
                user_in = input(input_tip)
                break
            else:
                print('请根据提示正确输入')
            
def monkey_picking_peaches():
    initial:float = 1.0
    for day in range(1, 10): # type: ignore
        initial+=1.5
    print(f'第一天摘了{initial:.0f}个桃子')
    
def monkey_picking_peaches_p():
    initial:float = 1
    for day in range(1, 10): # type: ignore
        initial+=1
        initial*=2
    print(f'第一天摘了{initial}个桃子')


def main():
    run()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    main()