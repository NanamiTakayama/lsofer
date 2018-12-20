import datetime
import time
import subprocess
from time import sleep

cmd = ["sudo", "lsof", "-nP", "-iTCP"]

file = open('new.txt','a')
file.write('new file\n')

while True:
    print(datetime.datetime.now())
    subprocess.call(cmd)
    sleep(20)
