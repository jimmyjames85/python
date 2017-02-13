import time
import sys
def printf(str):
    sys.stdout.write('%s' % (str))
    # print('%s' % (str), "") ---- python3 way
    return


def output(str, file=None):
    printf(str)
    if (file is not None):
        file.write(str)
    return


def signOf(num):
    if (num > 0):
        return 1
    elif (num < 0):
        return -1
    return 0

def localtimeString():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime
