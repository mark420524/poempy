import threading
import time
import schedule

a=0
def job():
    global a
    a+=1
    print("111111\n")
    if a==10:
        print('cacel 1111job')
        schedule.clear('1111job')
def job2():
    print("222222\n")

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every(2).seconds.do(run_threaded, job).tag('1111job')
schedule.every(2).seconds.do(run_threaded, job2).tag('2222job')



while 1:
    schedule.run_pending()
    time.sleep(1)