#!/usr/bin/python3

import os

apath = os.path.expanduser("~/a.log")
print("chemin etendu en", apath)
with open(apath) as fd:
    for line in fd:
        # print(line)
        # print(line.split())
        # print(line.split(None, 11))
        ip, login, passws, date, zone, reqtype, \
        url, httptype, status, size, referer, \
        uagenttrash = line.split(None, 11)
        print(ip)
        print(date)
        print(uagenttrash)
        break

# 63.143.42.252 - - [29/Oct/2019:06:25:25 +0100] "HEAD /login HTTP/1.1" 200
# 0 "https://riskstarter.arengibox.com/login"
# "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"
# 0.422 0.424 .
