import traceback
try:
    raise Exception('This is an error message.')
except:
    errorFile = open('errorInfo.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.write('\n')
    errorFile.close()
    print('The call stack is recorded in the errorInfo.txt.')