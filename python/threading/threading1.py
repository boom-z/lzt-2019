import threading
import time

def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')
    
def main():
    added_thread=threading.Thread(target=thread_job)
    added_thread.start()
    print('all done\n')
if __name__=='__main__':
    main()
