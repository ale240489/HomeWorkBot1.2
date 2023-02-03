import time

def createNewLogFile (info: str):
    newLog = []
    timeNow = time.localtime()
    strTimeNow = time.strftime('%H: %M: %S:', timeNow) + ' '
    newLog.append(strTimeNow)
    newLog.append(info)
    with open('log.txt', 'a') as file:
        file.writelines(newLog )

def addInfoInLog(info: str):
    log = []
    log.append(info)
    with open('log.txt', 'a') as file:
        file.writelines(log)

