from RunTime import runtime
from typing import override
from datetime import datetime

# 1【类基础】 定义一个Person类，包含属性name和age，以及方法introduce()，返回自我介绍字符串。实例化并调用方法。
class Person:
    # 【类变量】 在Person中添加类变量count，统计实例化的对象数量。
    count:int = 0
    def __init__(self, name:str, age:int)->None:
        if not isinstance(name, str):
            raise TypeError(f'{__name__} argument name is not str type')
        self.m_name:str = name # type: ignore
        if not isinstance(age, int):
            raise TypeError(f'{__name__} argument age is not int type')
        self.__age:int = age # type: ignore
        self.__email:str = ''
        Person.count+=1
    def introduce(self)->str:
        return f'My name is {self.m_name}, age is {self.__age}'
# 【运算符重载】 为Person实现__eq__方法，当年龄相同时返回True。
    def __eq__(self, value: 'Person') -> bool: # type: ignore
        return self.__age == value.__age

# 【类方法】 在Person类中添加类方法from_birth_year(cls, name, birth_year)，根据出生年份计算年龄并返回实例。
    @classmethod
    def from_birth_year(cls, name:str, birth_year:int)->'Person': 
        if not isinstance(birth_year, int):
            raise TypeError(f'{__name__} argument birth_year is not int type')
        if not isinstance(name, str):
            raise TypeError(f'{__name__} argument name is not str type')
        now_year = datetime.now().year
        if birth_year > now_year:
            raise ValueError(f'{__name__} argument birth_year greater than this year')
        return cls(name, now_year - birth_year)
# 【静态方法】 添加静态方法is_adult(age)，判断是否成年（≥18岁） 
    @staticmethod
    def is_adult(age:int)->bool:
        if not isinstance(age, int):
            raise TypeError(f'{__name__} argument age is not int type')
        return age >= 18
# 【封装】 修改Person的age属性为私有，提供get_age()和set_age()方法进行访问和修改。
    def get_age(self)->int:
        return self.__age
    def set_age(self, age:int):
        if not isinstance(age, int):
            raise TypeError(f'{__name__} argument age is not int type')
        self.__age = age

# 【属性装饰器】 使用@property为Person实现一个email属性，格式为name@example.com。
    @property
    def email(self)->str:
        return self.__email
    @email.setter
    def email(self, name:str):
        if not isinstance(name, str):
            raise TypeError(f'{__name__} argument name type is not str')
        self.__email = name+'@example.com'
    @email.getter
    def email(self)->str:
        return self.__email

# 【特殊方法】 为Person实现__str__方法，打印姓名:年龄。
    def __str__(self) -> str:
        return f'{self.m_name}:{self.__age}'



# 【继承】 创建Student类继承Person，新增属性student_id。重写introduce()方法，包含学号信息。
class Student(Person):
    def __init__(self, student_id:int, name: str, age: int) -> None:
        if not isinstance(name, str):
            raise TypeError(f'{__name__} argument name is not str type')
        if not isinstance(age, int):
            raise TypeError(f'{__name__} argument age is not int type')
        if not isinstance(student_id, int):
            raise TypeError(f'{__name__} argument student_id is not int type')
        super().__init__(name, age)
        
        self.m_student_id:int = student_id
    
    @override
    def introduce(self) -> str:
        return f'My student id is {self.m_student_id}, name is {self.m_name},age is {self.__age}'




# 【多重继承】 创建Teacher类（继承Person），新增属性subject。再定义Assistant类同时继承Student和Teacher。
class Teacher(Person):
    def __init__(self, name: str, age: int) -> None:
        if not isinstance(name, str):
            raise TypeError(f' argument name is not str type')
        self.m_name:str = name # type: ignore
        if not isinstance(age, int):
            raise TypeError(f' argument age is not int type')
        super().__init__(name, age)
        self.subject:str = ''

class Assistant(Student,Teacher):
    pass






@runtime
def run():
    p1 = Person('jianghaoxiang',25)
    p2 = p1.from_birth_year('jiang',2000)
    p2.email = 'jiang'
    print(p1 == p2)