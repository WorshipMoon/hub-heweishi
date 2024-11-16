import logging
import multiprocessing
# 绑定地址和端口
bind = '0.0.0.0:8000'

# 工作进程数
workers = 3  # 或者 multiprocessing.cpu_count() * 2 + 1

# 指定每个进程开启的线程数
threads = 2

# 工作模式
worker_class = 'gthread'
# worker_class = 'sync'  # 不支持多线程

# 访问日志文件
accesslog = '-'

# 错误日志文件
errorlog = '-'

# 日志级别
loglevel = 'debug'

# 超时设置
timeout = 30         # 增加超时时间到 300 秒
graceful_timeout = 60 # 优雅关闭超时
keepalive = 2        # 降低 keepalive 时间

# 每个工作进程的最大请求数
max_requests = 1000


# 错误处理
def worker_int(worker):
    """处理工作进程中断"""
    worker.log.info("worker received INT or QUIT signal")
    import threading, sys, traceback
    id2name = dict([(th.ident, th.name) for th in threading.enumerate()])
    code = []
    for threadId, stack in sys._current_frames().items():
        code.append("\n# Thread: %s(%d)" % (id2name.get(threadId,""), threadId))
        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('File: "%s", line %d, in %s' % (filename, lineno, name))
            if line:
                code.append("  %s" % (line.strip()))
    worker.log.debug("\n".join(code))

def worker_abort(worker):
    """处理工作进程异常终止"""
    worker.log.info("worker received SIGABRT signal")