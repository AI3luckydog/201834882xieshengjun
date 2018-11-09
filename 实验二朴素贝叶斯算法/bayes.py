# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 14:59:55 2018

@author: x
"""
from os import listdir,mkdir,path
from collections import Counter
targettrain = 'E:/dataminingdata/train' #训练数据存储路径
targettest = 'E:/dataminingdata/test'   #测试数据存储路径
def creatediccount(sampleFilesDir): #计算词频和idf
    n = 0
    wordMap = {}     #存储词频
    sampleList = listdir(sampleFilesDir)
    dfcount = len(sampleList)
    for j in range(len(sampleList)):
            sampleDir = sampleFilesDir + '/' + sampleList[j]
            temp = open(sampleDir).readlines()
            tempdic = Counter(temp)  #调用counter函数计算文件单词的词频
            for key,value in tempdic.items():  
                key = key.strip('\n')   #去除空格
                wordMap[key] = wordMap.get(key,0) + value  #计算词频
                n = n + value
    return wordMap, n ,dfcount         
def creatall():
    diccount = []  #存20个类的词典和词频，大小为20
    count = []    #存每个类的单词总数
    lendic = []   #存每个类词典的单词数量
    dcount = []  # 存每个类的文件总数
    p = []  #存储计算好的概率
    nll=[]
    
    fileDir = targettrain 
    sampleFilesList = listdir(fileDir)
    for i in range(len(sampleFilesList)):
        sampleFilesDir = fileDir + '/' + sampleFilesList[i]
        a,b,c = creatediccount(sampleFilesDir)
        diccount.append(a)
        count.append(b)
        dcount.append(c)
        lendic.append(len(a))
    for i in range(len(count)):
        temp = { }
        for key,value in diccount[i].items():
            temp[key] = (value+1)/(count[i]+lendic[i]) 
        p.append(temp)
        nll.append(1/(count[i]+lendic[i]))
    return p,nll,dcount
def bayes():
    p,nll,dcount = creatall()
    classname = listdir(targettrain)
    docusum = 0
    for i in range(len(dcount)):
        docusum = docusum + dcount[i]
    test,testfrom = opentest(targettest)
    result = []
    for i in range(len(test)):
        temp = []
        for j in range(len(p)):
            s = 1
            for k in range(len(test[i])):
               if test[i][k] in p[j].keys():
                   s = s*p[j][test[i][k]]
               else:
                   s =s*nll[j]
            s = s*(dcount[j]/docusum)
            temp.append(s) 
        result.append(classname[temp.index(max(temp))])
    print(result)
    x = 0
    for i in range(len(result)):
        if result[i] == testfrom[i]:
            x = x+1
    accurate = x/len(result) 
    print (accurate)           
def opentest(vectorpath):  #从文件中读取向量
    testFilesList = listdir(vectorpath)
    vsm = []     #存储向量
    vfrom = [ ]  #存储类别
    for i in range(len(testFilesList)):
        testdir = targettest +'/'+testFilesList[i]
        testdatalist = listdir(testdir)
        for j in range(len(testdatalist)):
            testdata = testdir + '/'+ testdatalist[j]
            testvector = []
            vfrom.append(testFilesList[i])
            temp = open(testdata,'r').readlines()
            for k in range(len(temp)):
                temp[k] = temp[k].strip()
                testvector.append(temp[k])
            vsm.append(testvector) 
    return vsm, vfrom   
bayes()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    