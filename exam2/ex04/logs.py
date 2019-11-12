from datetime import datetime


def logthis(msg):
    open("python.log", "a+").write(str(datetime.strftime(datetime.now(), '%d-%b-%Y %H:%M:%S ')) + msg + "\n")
