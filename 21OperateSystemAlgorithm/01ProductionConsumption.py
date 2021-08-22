import time
import random
import threading

'''
1)在缓冲区为空时，消费者不能再进行消费
2)在缓冲区为满时，生产者不能再进行生产
3)在一个线程进行生产或消费时，其余线程不能再进行生产或消费等操作，即保持线程间的同步
4)注意条件变量与互斥锁的顺序
'''

Resources = 0  # 初始可用资源量
Lock = threading.Lock()  # 创建线程锁
ProduceTime = 10  # 定义一个生产次数
UseTime = 0  # 初始化使用次数


class Producer(threading.Thread):
    def run(self):
        # 全局变量
        global Resources
        global UseTime
        global ProduceTime
        while True:
            # resource1 = random.randint(100,1000)  #随机产生一个生产的资源量
            resource1 = 1
            Lock.acquire()  # 开启线程锁
            if UseTime >= ProduceTime:
                Lock.release()  # 释放线程锁
                break
            UseTime += 1
            Resources += resource1  # 生产者增加资源
            print("%s:生产者生产了%d的使用资源，现在总共还有%d的可用资源量" % (threading.current_thread(), resource1, Resources))
            Lock.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        # 全局变量
        global Resources
        global UseTime
        global ProduceTime
        while True:
            # resource2 = random.randint(100,1000)  #随机产生一个消耗资源量
            resource2 = 1
            Lock.acquire()  # 开启线程锁
            if resource2 <= Resources:
                Resources -= resource2
                print("{}:消费者目前拥有的资源量为{},使用了{}资源量，还剩余{}资源量".format(threading.current_thread(), Resources + resource2,
                                                                   resource2, Resources))
            else:
                if UseTime >= ProduceTime:  # 生产次数超过定义的次数，则退出
                    Lock.release()  # 释放线程锁
                    break
                print("{}:消费者需要使用{}的资源,目前拥有的资源量为{},所以资源不足".format(threading.current_thread(), resource2, Resources))
            Lock.release()
            time.sleep(0.5)


def main():
    for x in range(5):
        y = Producer(name='生产者%d' % (x + 1))
        y.start()

    for i in range(5):
        j = Consumer(name='消费者%d' % (i + 1))
        j.start()


if __name__ == '__main__':
    main()
