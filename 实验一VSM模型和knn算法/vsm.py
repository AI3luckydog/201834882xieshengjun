# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 13:45:53 2018
建立VSM，模型，并把向量list存到文件中去
@author: x
"""
from os import listdir,mkdir,path
import re
from nltk.corpus import stopwords
import nltk
from random import randint
from collections import Counter
import math
pa = 'E:/20news-18828'     #数据读取路径
targettrain = 'E:/dataminingdata/train' #训练数据存储路径
targettest = 'E:/dataminingdata/test'   #测试数据存储路径
vectortrainpath = 'E:/dataminingdata/trainvector'  #训练数据生成向量存储路径
vectortestpath = 'E:/dataminingdata/testvector'    #测试数据生成向量存储路径
def createFiles():       #读取文件进行预处理并写入到新的文件中去
    srcFilesList = listdir(pa)
    for i in range(len(srcFilesList)):
        dataFilesDir = pa + '/' + srcFilesList[i] # 20个文件夹每个的路径
        dataFilesList = listdir(dataFilesDir) # 每个文件夹中每个文件的路径
        for j in range(len(dataFilesList)):
            x = -1
            m = randint(1,10)
            n = randint(1,10)
            if j%10 == n or j%10 == m: #将文件分为80%的训练数据和20%的测试数据
              x = 1                  #标记为1则分为测试数据
            else:
              x = 0                   #标记为0则分为训练数据
            createProcessFile(srcFilesList[i],dataFilesList[j],x)# 调用createProcessFile()在新文档中处理文本
            print ('%s %s' % (srcFilesList[i],dataFilesList[j]))
def createProcessFile(srcFilesName,dataFilesName,x):    #将预处理完的数据存储到新文件中区，一行一个单词
    if x == 0:
       targetDir = targettrain + '/' + srcFilesName 
       targetFile= targettrain + '/' + srcFilesName\
                + '/' + dataFilesName
    else:
       targetDir = targettest + '/' + srcFilesName 
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
def lineProcess(line):          #调用nltk对数据进行预处理
    stopwords = nltk.corpus.stopwords.words('english') #去停用词
    porter = nltk.PorterStemmer()  #词干分析
    splitter = re.compile('[^a-zA-Z]')  #去除非字母字符，形成分隔
    words = [porter.stem(word.lower()) for word in splitter.split(line)\
             if len(word)>0 and\
             word.lower() not in stopwords]
    return words
def creatediccount(): #计算词频和idf
    n = filecount()  #计算文件数量
    wordMap = {}     #存储词频
    worddf = {}      #存储df
    newWordMap = {}
    fileDir = targettrain 
    sampleFilesList = listdir(fileDir)
    for i in range(len(sampleFilesList)):
        sampleFilesDir = fileDir + '/' + sampleFilesList[i]
        sampleList = listdir(sampleFilesDir)
        for j in range(len(sampleList)):
            sampleDir = sampleFilesDir + '/' + sampleList[j]
            temp = open(sampleDir).readlines()
            tempdic = Counter(temp)  #调用counter函数计算文件单词的词频
            for key,value in tempdic.items():  
                key = key.strip('\n')   #去除空格
                wordMap[key] = wordMap.get(key,0) + value  #计算词频
                worddf[key] = worddf.get(key,0) + 1       #计算原始df
    #只返回出现次数大于2的单词
    for key, value in wordMap.items():
        if value > 2:
            newWordMap[key] = worddf[key]
    sortedNewWordMap = sorted(newWordMap.items())  #将词典按字母顺序排序
    newworddf = { }
    for i in sortedNewWordMap:
         newworddf[i[0]] = math.log10(n/i[1])  #计算真实tf，
        #newworddf[i[0]] = i[1]
    #for key,value in newworddf.items():
       # print(key+str(value))
   # print ('wordMap size : %d' % len(sortedNewWordMap))
    #print (newworddf)
    return newworddf
def filecount():  #计算文件数量
    n = 0
    srcFilesList = listdir(targettrain)
    for i in range(len(srcFilesList)):
        dataFilesDir = targettrain + '/' + srcFilesList[i] 
        dataFilesList = listdir(dataFilesDir)
        n = n + len(dataFilesList)
    return n
def createvocabulary(diccount):#生成字典列表
    #diccount =  creatediccount()
    vocabulary = [ ]
    for key,value  in  diccount.items():
        vocabulary.append(key)
    print (len(vocabulary))
    return vocabulary
def computetf(dic,vocabulary): #dic是个字符串列表，计算df，vocabulary是词典
    dicVector = {}
    for i in dic:
        if i in vocabulary:  #只有在词典的单词才计算，不在词典的词语略过
          if i in dicVector.keys():
            dicVector[i]  = dicVector[i]+1
          else:
            dicVector[i]  = 1
    m = max(dicVector, key=lambda x: dicVector[x]) #求文件中出现词频最大单词的索引
    w = dicVector[m]
    for key,value in dicVector.items():
        dicVector[key] = value/w            #tf用文件中出现词频数除以文件中出现次数最大的单词次数  
    return  dicVector
def computevector(inpath,savepath):#生成向量
    idf = creatediccount()         #idf 的值 存在字典里
    classfrom = []                 #保存向量类别
    vectorclass = []              #保存向量
    vocabulary =  createvocabulary(idf)#保存词典
    srcFilesList = listdir(inpath)
    for i in range(len(srcFilesList)):
        dataFilesDir = inpath + '/' + srcFilesList[i] # 20个文件夹每个的路径
        dataFilesList = listdir(dataFilesDir) #每个文件夹中每个文件的路径
        for j in range(len(dataFilesList)):
            a = dataFilesDir+'/'+dataFilesList[j]
            b = srcFilesList[i]+'/'+dataFilesList[j]
            classfrom.append(b)
            fr = open(a,'r')
            temp = fr.readlines()
            fr.close()
            for k in range(len(temp)):
              temp[k] = temp[k].strip()
            #print (temp)  
            vector = computetf(temp,vocabulary)
            for key,value in vector.items():
                vector[key] = idf[key]*value
            vectorclass.append(vector)
    #print(vectorclass[0])
    #print(vectorclass[1])
    #print(vectorclass[2])
    for i in range(len(vectorclass)):  #将向量写到文件中去
      tpath = classfrom[i].split('/')
      fpath = savepath + '/' + classfrom[i]
      targetvectordir =  savepath + '/'+ tpath[0]
      if path.exists(targetvectordir)==False:
            mkdir(targetvectordir)
      fw = open(fpath,'w')
      for key,value in vectorclass[i].items():
          fw.write( key +'/'+ str(value)+'\n')
      fw.close()
    print('done')
    return classfrom,vectorclass   
computevector(targettrain,vectortrainpath)
computevector(targettest,vectortestpath)
#creatediccount() 
#print (filecount())