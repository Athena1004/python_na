import multiprocessing
from time import ctime

def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull ", item, "out of q")#此处替换为有用的工作
        input_q.task_done()#发出信号通知任务完成
    print("Out of consumer:", ctime())

def producer(sequence, output_q):
    print("Into producer:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put ", item, "into q")

    print("Out of producer:", ctime())

#建立进程
if __name__ == "__main__":
    q = multiprocessing.Queue()
    cons_p1= multiprocessing.Process(target= consumer,args=(q,))#运行消费者进程
    cons_p1.start()

    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))  # 运行消费者进程
    cons_p2.start()

    sequence = [1,2,3,4]#生成多个项，sequence代表要发送给消费者的项序列
    producer(sequence,q)

    q.put(None)
    q.put(None)

    cons_p1.join()
    cons_p2.join()