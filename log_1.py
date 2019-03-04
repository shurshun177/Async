import logging

logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

fh = logging.FileHandler('imed_app.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)

def main():
    logger.info("MY FIRST STATEMENT")

main()