import asyncio as loop
import threading as thd
from time import sleep
# from typing import Self
from learn_socket import start

def task1 ():
    while 1:
        sleep(1.0)
        print('hello')

def task2 ():
    while 1:
        sleep(1.0)
        print('async')

async def test_async():
    t1 = thd.Thread(target=task1)
    t2 = thd.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

class File_io:
    def __init__(self, filename:str,mod = 'r') -> None:
        self.file = open(filename,mode=mod,encoding='utf-8')
    def __enter__(self)->'File_io':
        return self
    def __exit__(self,exc_type, exc_val,exc_tb)->None:
        self.file.close()
    def read(self):
        return self.file.read()
def open_file(name:str, mod='r')->File_io:
    return File_io(name,mod=mod)

async def run():
    await test_async()



def test1():
    s = 'asssetbattboipo'
    s1 = set(s)
    s2 = ''.join(s1)
    print(s2)

def cj():
    s=[1,23,2,3,21,9,4,5,6]
    lenght = len(s)    
    for i in range(lenght):
        target = True
        for j in range(0, lenght - i - 1):
            if s[j] > s[j+1]:
                s[j],s[j+1] = s[j+1], s[j]
                target = False
        if target:
            break
    print(s)
            

def main():
    print(cj())


if __name__ == '__main__':
    main()