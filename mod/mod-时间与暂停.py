import time,datetime
time.sleep(1)
TIME = datetime.datetime.now()
print(TIME.strftime("%Y.%m.%d %H-%M-%S"))