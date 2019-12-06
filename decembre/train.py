#!/usr/bin/python3
import sys
def show_train(size):
    wagon = "[__________]"
    # alist = [ wagon for i in range(int(sys.argv[1]))]
    alist = []
    for i in range(size):
        alist.append(wagon)
    alist.append(" []===o")
    out = " - ".join(alist)
    return out
# wagon = "[__________] - "
# print(wagon * int(sys.argv[1]), "[]===o")
if __name__ == "__main__":
    # print(show_train(int(sys.argv[1])))
    out = show_train(int(sys.argv[1]))
    print(out)
