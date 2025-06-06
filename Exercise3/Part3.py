import re


# 【基础匹配】 使用re检查字符串"Python"是否包含"thon"。
def check_python():
    pattern = r'thon$'
    result = re.search(pattern, 'Python')
    if result is not None:
        print('has thon')
    else:
        print('not find thon')

# 【查找所有】 在"a1b2c3"中查找所有数字，返回列表['1','2','3']。
def search_num()->list[str]:
    pattern = re.compile(r'([0-9]).([0-9]).([0-9])')
    result = pattern.search('a1b2c3')
    re_list = list()
    if result is not None:
        re_list = list(result.groups())  
    return re_list

# 【分组提取】 从"2023-10-05"中提取年、月、日。
def match_date():
    pattern = re.compile(r'([0-9]+).([0-9]+).([0-9]+)')
    result = pattern.search('2023-10-05')
    if result is not None:
        t = result.groups()
        print(f'{t[0]}年{t[1]}月{t[2]}日')

# 【替换】 将"apple, banana; cherry"中的标点替换为空格。
def replace_space():
    pattern = re.compile(r'[,|;]')
    result = pattern.sub(' ','apple, banana; cherry')
    print(result)
    
# 【分割】 用正则分割"Alice99Bob78"，返回['Alice', 'Bob']（按数字分割）。
def split_by_re():
    pattern = re.compile(r'[0-9]+[\r\n]?')
    result = pattern.split('Alice99Bob78')
    print(result)


# 【邮箱验证】 编写正则验证邮箱格式（简单版：xxx@xxx.xxx）。
def pattern_email():
    pattern = re.compile(r'[\w]*@[\w]*\.[\w]*')
    result = pattern.match('1346546546@qq.com')
    if result is not None:
        print(result.group())
    else:
        print('is not email')


# 【贪婪非贪婪】 对比贪婪模式r'a.c'和非贪婪模式r'a.?c'在"abcabc"中的匹配结果。
def compare_str():
    pattern = re.compile(r'a.c')
    result = pattern.search('abcabc')
    if result is not None:
        print(result.group())
    result2 = re.search(r'a.?c', 'abcabc')
    if result2 is not None:
        print(result2.group())

# 【单词边界】 查找字符串"cat in a cathedral"中独立的"cat"（不匹配"cathedral"）。
def find_unique_cat():
    pattern = re.compile(r'^cat ')
    result = pattern.search('cat in a cathedral')
    if result is not None:
        print(result.group())

# 【前瞻后顾】 提取"100°C, 200°F"中单位前的数字（不包含°符号）。
def extract_num():
    pattern = re.compile(r'[^0-9]+')
    result = pattern.split("100°C, 200°F")
    if result is not None:
        print(result)

# 【编译重用】 编译正则r"\d+"，多次匹配不同字符串提高效率。
def compile_regex():
    pattern = re.compile(r'.+')
    result1 = pattern.search('jfeiosjfoiej')
    result2 = pattern.search('jfsefesej')
    result3 = pattern.search('fqrqrqrqrq')
    result4 = pattern.search('jfeiosjwwwwwwwwwfoiej')
    print(result1.group())
    print(result2.group())
    print(result3.group())
    print(result4.group())
    
    
def run():
    compile_regex()