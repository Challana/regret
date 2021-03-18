import os
q = input ("Залпнирвоать или отменить")
if q == "отменить":
    os.system("shutdown /a")
elif q == "запланировать":
    t = input("Введи время (мин): ")
    t = int(t)
    t = t*60
    os.system("shutdown /s /f /t {}".format(t))
else:
    print("пиши правильно козел")