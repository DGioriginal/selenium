import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %{levelname}s - %{message}s') # 1 аргумент на запись сообщений в файл
# logging.disable(logging.CRITICAL) АБСОЛЮТНОЕ ОТКЛЮЧЕНИЕ СООБЩЕНИЙ 
logging.debug('Start Programm')

def factorial(n):
    logging.debug('Start factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i = ' + str(i) + ', total = ' + str(total))
    logging.debug('End factorial(%s%%)' % (n))
    return total
print(factorial(5))
logging.debug('End programm')