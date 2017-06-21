# coding:utf-8

f = open("目录.txt", "rw")
while True:
    line = f.readline()
    if line:
        pass    # do something here
        line=line.strip('./')
        line=line.strip('',1)
        print "%s"%line
    else:
        break
f.close()
