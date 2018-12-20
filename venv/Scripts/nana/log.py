import logging

# logging.basicConfig(level=logging.DEBUG)
LOG_FORMAT = "%(asctime)s======%(levelname)s++++++%(message)s" #时间 级别 信息
logging.basicConfig(filename = "logtry.log", level = logging.DEBUG,format = LOG_FORMAT)

logging.debug("this is a debug log")
logging.info("this is a info log")
logging.warning("this is a warning log")
logging.error("this is a error log")
logging.critical("this is a critical log")

#另一种写法
logging.log(logging.DEBUG,"this is a debug log")
logging.log(logging.INFO,"this is a info log")
logging.log(logging.WARNING,"this is a warning log")
logging.log(logging.ERROR,"this is a error log")
logging.log(logging.CRITICAL,"this is a critical log")

#实例
#根据需求分析


import logging
import logging.handlers
import datetime

logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler("all.log", when = 'midnight', interval=1, backupCount=7)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler("error.log")
f_handler.setLevel(logging.ERROR)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))


logger.addHandler(rf_handler)#把相应的处理器组装到Logger
logger.addHandler(rf_handler)