# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 13:45:53 2018

@author: x
"""


from os import listdir,mkdir,path
import re

import nltk
from random import randint
pa = 'E:/20news-18828'
targettrain = 'E:/dataminingdata/train'
targettest = 'E:/dataminingdata/test'
def createFiles(): #将原文件分成测试数据和训练数据到新的位置
   
    srcFilesList = listdir(pa)
    for i in range(len(srcFilesList)):
        dataFilesDir = pa + '/' + srcFilesList[i] # 20个文件夹每个的路径
        dataFilesList = listdir(dataFilesDir) #每个文件夹中每个文件的路径
        for j in range(len(dataFilesList)):
            x = -1
            m = randint(1,10)
            n = randint(1,10)
            if j%10 == n or j%10 == m: #将文件分为80%的训练数据和20%的测试数据
              x = 1
            else:
              x = 0
            createProcessFile(srcFilesList[i],dataFilesList[j],x)# 调用createProcessFile()在新文档中处理文本
            print ('%s %s' % (srcFilesList[i],dataFilesList[j]))
                       
def createProcessFile(srcFilesName,dataFilesName,x): #生成复制文件，并写入
    if x == 0:
       targetDir = targettrain + '/' + srcFilesName # 20个新文件夹每个的路径
       targetFile= targettrain + '/' + srcFilesName\
                + '/' + dataFilesName
    else:
       targetDir = targettest + '/' + srcFilesName # 20个新文件夹每个的路径
       targetFile= targettest + '/' + srcFilesName\
                + '/' + dataFilesName
    if path.exists(targetDir)==False:
            mkdir(targetDir)
    else:
            print ('%s exists' % targetDir)
    
    srcFile = pa +'/'+ srcFilesName + '/' + dataFilesName
    
    fw = open(targetFile,'w')
    fr =  open(srcFile,'r',errors = 'replace')
    dataList = fr.readlines()
    fr.close()
    for line in dataList:
        
        resLine = lineProcess(line) # 调用lineProcess()处理每行文本
        for word in resLine:
        #for word in line:
            fw.write('%s\n' % word) #一行一个单词
    
    fw.close()
def lineProcess(line):  #用nltk进行预处理
    stopwords = nltk.corpus.stopwords.words('english') #去停用词
    porter = nltk.PorterStemmer()  #词干分析
    splitter = re.compile('[^a-zA-Z]')  #去除非字母字符，形成分隔
    words = [porter.stem(word.lower()) for word in splitter.split(line)\
             if len(word)>0 and\
             word.lower() not in stopwords]
    return words
def creatediccount(): #产生词典字典，并记录每个单词的频率
    wordMap = {}
    newWordMap = {}
    fileDir = targettrain
    sampleFilesList = listdir(fileDir)
    for i in range(len(sampleFilesList)):
        sampleFilesDir = fileDir + '/' + sampleFilesList[i]
        sampleList = listdir(sampleFilesDir)
        for j in range(len(sampleList)):
            sampleDir = sampleFilesDir + '/' + sampleList[j]
            for line in open(sampleDir).readlines():
                word = line.strip('\n')
                wordMap[word] = wordMap.get(word,0.0) + 1.0
                
    #只返回出现次数大于10的单词
    for key, value in wordMap.items():
        if value > 10:
            newWordMap[key] = value
    sortedNewWordMap = sorted(newWordMap.items())
    #for item in  sortedNewWordMap:
     #   dic.append(item.key)
    print ('wordMap size : %d' % len(sortedNewWordMap))
    return sortedNewWordMap
def createdic():  #返回词典列表
    diccount =  creatediccount()
    dic = [ ]
    for key,value  in  diccount:
        dic.append(key)
        print (key)
    return dic



createdic()