import threading
import time

def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def T2_job():
    print('T2 start\n')
    print('T2 finish\n')
def main():
    added_thread=threading.Thread(target=thread_job)
    thread2=threading.Thread(target=T2_job,name='T2')
    added_thread.start()
    thread2.start()
    #added_thread.join()#上面运行完了才能运行下面的
    #thread2.join()
    print('all done\n')
if __name__=='__main__':
    main()
