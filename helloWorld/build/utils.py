import time
def printf(str):
    print('%s' % (str), end="")
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