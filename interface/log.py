import logging,os,arrow,threading,sys
from functools import wraps

log_path="H:\之前项目\pythonstudy\pythonstudy\python3\log"
class Log:
    def __init__(self,filename):
        # CurrentPath = os.getcwd()
        # print (CurrentPath)
        # print (os.path)
        # print (sys.argv[0])
        # print (os.path.split(os.path.realpath(sys.argv[0]))[1])
        # filename=os.path.split(os.path.realpath(sys.argv[0]))[1]
        time = arrow.now().format('YYYYMMDDHHmmss')
        self.logname=os.path.join(log_path,'%s.log'%(str(time)))
        # print (os.path.abspath(log_path))
        # print (self.logname)
        self.logger=logging.getLogger('Uenpaylog')    #设置log名称
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - '+str(filename)+'-%(message)s ')
        # self.formatter = logging.Formatter(
        #     '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # def getwenjian(self):
    #     script_path = os.path.realpath(__file__)
    #     script_dir = os.path.dirname(script_path)
    #     filename = os.path.split(script_path)[1]
    #     return filename


    def __console(self,level,message):
        #创造本地的日志
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        #创造控制台日志
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if  level =='info':
            self.logger.info(message)
        elif    level =='debug':
            self.logger.debug(message)
        elif    level =='warning':
            self.logger.warning(message)
        elif    level =='error':
            self.logger.error(message)
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()


    def debug(self,message):
        self.__console('debug',message)
    def info(self,message):
        self.__console('info',message)
    def warning(self,message):
        self.__console('warning',message)
    def error(self,message):
        self.__console('error',message)

# def logger():
#     """ fcuntion from logger meta """
#     def wrap(function):
#         """ logger wrapper """
#         @wraps(function)
#         def _wrap(*args, **kwargs):
#             """ wrap tool """
#             Log.info('5552222')
#             # Log.info("当前模块 {}".format(param))
#             # Log.info("全部args参数参数信息 , {}".format(str(args)))
#             # Log.info("全部kwargs参数信息 , {}".format(str(kwargs)))
#             return function(*args, **kwargs)
#         return _wrap
#     return wrap
if __name__ == '__main__':

    Log(666).info('111')

# import os
# import logbook
# from logbook.more import ColorizedStderrHandler
# from functools import wraps
# check_path='.'
# LOG_DIR = os.path.join(check_path, 'log')
# file_stream = False
# if not os.path.exists(LOG_DIR):
#     os.makedirs(LOG_DIR)
#     file_stream = True
# def get_logger(name='jiekou', file_log=file_stream, level=''):
#     """ get logger Factory function """
#     logbook.set_datetime_format('local')
#     ColorizedStderrHandler(bubble=False, level=level).push_thread()
#     logbook.TimedRotatingFileHandler(
#         os.path.join(LOG_DIR, '%s.log' % name),
#         date_format='%Y-%m-%d-%H', bubble=True, encoding='utf-8').push_thread()
#     return logbook.Logger(name)
# LOG = get_logger(file_log=file_stream, level='INFO')
# def logger(param):
#     """ fcuntion from logger meta """
#     def wrap(function):
#         """ logger wrapper """
#         @wraps(function)
#         def _wrap(*args, **kwargs):
#             """ wrap tool """
#             LOG.info("当前模块 {}".format(param))
#             LOG.info("全部args参数参数信息 , {}".format(str(args)))
#             LOG.info("全部kwargs参数信息 , {}".format(str(kwargs)))
#             return function(*args, **kwargs)
#         return _wrap
#     return wrap
