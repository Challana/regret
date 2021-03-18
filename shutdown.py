import os
t = input("введи время")
t = int(t)
t = t*60
os.system("shutdown /s /f /t {}".format(t))