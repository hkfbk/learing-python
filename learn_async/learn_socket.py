import socket as sokt
import threading as thd
from time import sleep

def test_socket():
    sock = sokt.socket(sokt.AF_INET, sokt.SOCK_STREAM)
    sock.setsockopt(sokt.SOL_SOCKET, sokt.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1',8080))
    sock.listen(5)
    
    while 1:
        client_sock, client_address = sock.accept()
        data = client_sock.recv(1024)
        if data:
            print(f'receive data is {data.decode()}')

def test_client():
    client = sokt.socket(sokt.AF_INET, sokt.SOCK_STREAM)
    client.connect(('127.0.0.1',8080))
    message = 'hello network'
    for _ in range(10):
        sleep(2)
        client.sendall(message.encode())
    client.close()

def start():
    th1 = thd.Thread(target=test_socket)
    th2 = thd.Thread(target=test_client)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
