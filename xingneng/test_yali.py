#coding:utf8
__time__ = '2018/8/2 9:55'
__author__ = 'SYJ'

from locust import HttpLocust, TaskSet, task
import queue,subprocess

class test_taskset(TaskSet):

    @task
    def register1(self):
        try:
            data = self.locust.queueData.get()  #获取队列里的数据
            print("register1:%s"%(data))
        except queue.Empty:                     #队列取空后，直接退出
            print('no data exist')
            exit(0)

    @task
    def register2(self):
        try:
            data = self.locust.queueData.get()  #获取队列里的数据
            print("register2:%s" % (data))
        except queue.Empty:                     #队列取空后，直接退出
            print('no data exist')
            exit(0)


class test_run(HttpLocust):
    host = 'http://192.168.1.232'
    task_set = test_taskset
    queueData = queue.Queue()  #队列实例化
    for i in range(3):   #循环数据生成
        # data = ['13700008838', '15922220012', '13770000001', '13760000027', '13760000062', '13700002298',
        #            '13700005414', '13700004929', '13700003784', '13700009140', '13700009350', '13760000026',
        #            '13760000025', '13760000090', '18000000001', '13700001629', '13700004338', '13700004161',
        #            '13700001590', '13700001596', '13700003717', '13700007345', '13700002412', '13700008843',
        #            '13700002782', '13700003602', '13700001035', '13700007591', '13000000022', '13764906433',
        #            '13000000088', '13000000099', '13760000098', '13760000092', '13760000091', '13760000080',
        #            '13700001055', '13000000021', '13764906434', '13760000002', '13764906432', '13761917640',
        #            '13700008839'][i-1]
        data = ['13700008838', '15922220012'][i - 1]
        print (data)
        queueData.put_nowait(data)

if __name__ == '__main__':
    subprocess.Popen('locust -f H:\之前项目\pythonstudy\pythonstudy\python3\\xingneng\\test_yali.py', shell=True)