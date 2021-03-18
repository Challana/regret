import os

flag = True
while flag:
    q = input("(З)апланировать или (O)тменить:\n").lower()
    if q in ("отменить", "о", "запланировать", "з"):
        flag = False
    if q == "отменить" or q == "о":
        os.system("shutdown /a")
    elif q == "запланировать" or q == "з":
        t = input("Введи время (мин): ")
        if not t.isnumeric():
            print("пиши правильно козел")
            continue
        t = int(t)
        t = t*60
        os.system("shutdown /a")
        os.system("shutdown /s /f /t {}".format(t))
    else:
        print("пиши правильно козел")