import simplejson as json
import pandas as pd
from tempfile import TemporaryFile
# 【写文件】 将字符串"Hello, File I/O!"写入新文件greeting.txt。
def file_io():
    with open('greeting.txt', 'a', encoding='utf-8') as f:
        f.write('\nAppending a new line.')
    with open('greeting.txt', 'w', encoding='utf-8') as f:
        f.write('Hello,File I/O!')
    with open('greeting.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def read_data():
    with open('data.txt', 'r',encoding='utf-8') as f:
        for data in f.readlines():
            print(data)

def deal_csv():
    Li = [['Name','Age'],['Alice',30],['Bob',25]]
    f =  pd.DataFrame(Li)
    f.to_csv('people.csv',index=False)

def json_io():
    d = {'name':'Alice', 'age':30}
    s = json.dumps(d)
    with open('user.json', 'w',encoding='utf-8') as f:
        json.dump(s,f,indent=4,sort_keys=True)
    
    with open('user.json','r',encoding='utf-8') as f:
        s = json.load(f)
        print(s)


def read_except():
    try:
        f = open('lalala')
        raise FileNotFoundError('no find file')
    except FileNotFoundError as exc:
        print(f'function read_except throw an exception:{exc}')

def copy_file():
    with open('source.txt','r',encoding='utf-8')as f1:
        with open('dest.txt','w',encoding='utf-8')as f2:
            for data in f1.readlines():
                f2.write(data)

def binary_io():
    with open('image.jpg','rb') as f1:
        with open('copy.jpg', 'wb') as f2:
            for data in f1.readlines():
                f2.write(data)


def temp_file():
    with TemporaryFile('w+t', encoding='utf-8') as tm:
        tm.write('temp file')
    
    
def run():
    binary_io()