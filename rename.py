#!C:\Users\spfhy\AppData\Local\Programs\Python\Python36-32\python.exe
#coding=gbk
import os
def rename():
    count = 0
    path = r"C:\Users\spfhy\Desktop\rename"
    filelist = os.listdir(path)
    for file in filelist:
        oldDir = os.path.join(path,file)
        if os.path.isdir(oldDir): #if it is folder,countinue
            continue
        filetype = os.path.splitext(file)[1] #extension
        newDir = os.path.join(path,'cell'+str(count)+filetype)
        os.renames(oldDir, newDir)
        count += 1
rename()
print('rename success ---git')
# github 20180225
# git commit
