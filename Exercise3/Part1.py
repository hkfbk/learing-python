from RunTime import runtime
from typing import override
from datetime import datetime

# 1【类基础】 定义一个Person类，包含属性name和age，以及方法introduce()，返回自我介绍字符串。实例化并调用方法。
class Person:
    def __init__(self, name:str, age:int)->None:
        if isinstance(name, str):
            raise TypeError(f'{__name__} argument name is not str type')
        self.m_name:str = name # type: ignore
        if isinstance(age, int):
            raise TypeError(f'{__name__} argument age is not int type')
        self._age:int = age # type: ignore
    def introduce(self)->str:
        return f'My name is {self.m_name}, age is {self._age}'

# 【类方法】 在Person类中添加类方法from_birth_year(cls, name, birth_year)，根据出生年份计算年龄并返回实例。
    @classmethod
    def from_birth_year(cls, name:str, birth_year:int)->'Person': 
        if isinstance(birth_year, int):
            raise TypeError(f'{__name__} argument birth_year is not int type')
        if isinstance(name, str):
            raise TypeError(f'{__name__} argument name is not str type')
        now_year = datetime.now().year
        if birth_year > now_year:
            raise ValueError(f'{__name__} argument birth_year greater than this year')
        return cls(name, now_year - birth_year)
# 【静态方法】 添加静态方法is_adult(age)，判断是否成年（≥18岁） 
    @staticmethod
    def is_adult(age:int)->bool:
        if isinstance(age, int):
            raise TypeError(f'{__name__} argument age is not int type')
        return age >= 18
# 【封装】 修改Person的age属性为私有，提供get_age()和set_age()方法进行访问和修改。
    def get_age(self)->int:
        return self._age
    def set_age(self, age:int):
        if isinstance(age, int):
            raise TypeError(f'{__name__} argument age is not int type')
        self._age = age

# 【属性装饰器】 使用@property为Person实现一个email属性，格式为name@example.com。
    @property
    def email(self)->str:
        return self.email
    @email.setter
    def email(self, name:str):
        if isinstance(name, str):
            raise TypeError(f'{__name__} argument name type is not str')
        self.email = name+'@example.com'
    @email.getter
    def email(self)->str:
        return self.email
    
    

# 【继承】 创建Student类继承Person，新增属性student_id。重写introduce()方法，包含学号信息。
class Student(Person):
    def __init__(self, student_id:int, name: str, age: int) -> None:
        if isinstance(name, str):
            raise TypeError(f'{__name__} argument name is not str type')
        if isinstance(age, int):
            raise TypeError(f'{__name__} argument age is not int type')
        if isinstance(student_id, int):
            raise TypeError(f'{__name__} argument student_id is not int type')
        super().__init__(name, age)
        
        self.m_student_id:int = student_id
    
    @override
    def introduce(self) -> str:
        return f'My student id is {self.m_student_id}, name is {self.m_name}, age is {self.m_age}'
    






@runtime
def run():
    p1 = Person('jianghaoxiang',23)
    p2 = p1.from_birth_year('jiang',2000)
    print(p2.introduce())