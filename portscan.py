import socket
import threading

hosts = ['192.168.224.150', '192.168.224.149']
ports = [21, 22, 23, 80, 81, 88, 135, 443, 445, 1080, 1433, 3389, 5900, 6379, 7001, 8080]
socket.setdefaulttimeout(1)


def portscan(ip, port):
    s = socket.socket()
    try:
        s.connect((ip, port))
        print('  [+] Port %s is open!' % port)
    except Exception:
        pass
    finally:
        s.close()


if __name__ == '__main__':
    for i in hosts:
        threads = []
        print('[+]Starting portscan for %s' % i)
        for j in ports:
            t = threading.Thread(target=portscan, args=(i, j))
            threads.append(t)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
