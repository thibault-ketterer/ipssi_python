from datetime import datetime


def logthis(msg):
    open("python.log", "a+").write(str(datetime.now()) + msg + "\n")
