import logging
import logging.handlers as handlers
import time
import sys

logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

# here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# interval parameter is the number of minutes
# if 1, it will then create the new log file
# every minute. backupCount is number of files.
# In RotatingFileHandler there us maxBytes parameter (maxBytes=500)
logHandler = handlers.TimedRotatingFileHandler('normal.log', when='M', interval=1, backupCount=0)
logHandler.setLevel(logging.INFO)
# here we set our logHandlers formatter
logHandler.setFormatter(formatter)

errorLogHandler = handlers.RotatingFileHandler('error.log', maxBytes=5000, backupCount=0)
errorLogHandler.setLevel(logging.ERROR)
errorLogHandler.setFormatter(formatter)

logger.addHandler(logHandler)
logger.addHandler(errorLogHandler)

def main():
    while True:
        time.sleep(1)
        logger.info("A Sample Log Statement")
        logger.error('An error log statement')

main()