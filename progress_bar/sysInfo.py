import psutil

def getCPU():
    return psutil.cpu_percent(interval=1)

while 1:
    getCPU()