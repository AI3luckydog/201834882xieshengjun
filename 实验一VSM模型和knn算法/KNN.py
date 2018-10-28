<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 13:34:07 2018

@author: x
"""
from os import listdir,path
import math
from collections import Counter
vectortrainpath = 'E:/dataminingdata/trainvector'
vectortestpath = 'E:/dataminingdata/testvector'
def creatvector(vectorpath):  #从文件中读取向量
    testFilesList = listdir(vectorpath)
    vsm = []     #存储向量
    vfrom = [ ]  #存储类别
    for i in range(len(testFilesList)):
        testdir = vectortestpath +'/'+testFilesList[i]
        testdatalist = listdir(testdir)
        for j in range(len(testdatalist)):
            testdata = testdir + '/'+ testdatalist[j]
            testvector = {}
            vfrom.append(testFilesList[i])
            temp = open(testdata,'r').readlines()
            for k in range(len(temp)):
                temp[k] = temp[k].strip()
                b = temp[k].split('/')
                testvector[b[0]] = float(b[1])
            vsm.append(testvector) 
    return vsm, vfrom
def knn():
   testvsm ,testvfrom =  creatvector(vectortestpath)
   trainvsm ,trainvfrom =  creatvector(vectortrainpath) 
   testmo = [ ]  #存储测试向量的模长
   trainmo = [ ] #存储训练向量的模长
   k = 3        #knn的k的取值
   result = [ ]  #存储识别结果
   accurate = [ ]#存储是否识别正确
   for i in range(len(testvsm)): #计算模长
      tempsum = 0
      for key,value in testvsm[i].items():
          tempsum = tempsum +value*value
      testmo.append(math.sqrt( tempsum ))  
   for i in range(len(trainvsm)):
      tempsum = 0
      for key,value in trainvsm[i].items():
          tempsum = tempsum +value**2
      trainmo.append(math.sqrt( tempsum ))
   #print(trainmo)          
   for i in range(len(testvsm)):
       topk = []
       classfrom = []
       for j in range(len(trainvsm)):
           tempv = 0#用来计算两个向量的积
           for key,value in testvsm[i].items():
               if key in trainvsm[j].keys():
                   tempv = tempv + value*trainvsm[j][key]
           cosine = tempv/(trainmo[j]*testmo[i])  #计算cos值  
           if len(topk)<k :
               topk.append(cosine)
               classfrom.append(trainvfrom[j])
           elif cosine >= min(topk):  #去前k个最大的cosine值
               topk[topk.index(min(topk))] = cosine
               classfrom[topk.index(min(topk))] = trainvfrom[j]
       a = Counter(classfrom)
       '''if len(a) >= 3: #看k个备选类里出现最多的前三个类，有一个满足则命中
         res = a.most_common(3)
         if res[0][0] == testvfrom[i] or res[1][0] == testvfrom[i] or res[2][0] == testvfrom[i]:
           accurate.append(1)
         else:
           accurate.append(0)
       else:
         res = a.most_common(1)  
         if res[0][0] == testvfrom[i] :#or res[1][0] == testvfrom[i] :
           accurate.append(1)
         else:
           accurate.append(0)'''
       res = a.most_common(1)  #看k个备选类里出现最多的类，有一个满足则命中
       if res[0][0] == testvfrom[i] :#or res[1][0] == testvfrom[i] :
           accurate.append(1)
       else:
           accurate.append(0)    
       result.append(res[0])
      #print (topk)
      #print (classfrom)
   s = 0
   for i in range(len(accurate)):
       if accurate[i] == 1:
          s = s + 1
   f = s/ len(accurate)
   print(result)           
   print(f)          
knn()               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
       
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 13:34:07 2018

@author: x
"""
from os import listdir,path
import math
from collections import Counter
vectortrainpath = 'E:/dataminingdata/trainvector'
vectortestpath = 'E:/dataminingdata/testvector'
def creatvector(vectorpath):  #从文件中读取向量
    testFilesList = listdir(vectorpath)
    vsm = []     #存储向量
    vfrom = [ ]  #存储类别
    for i in range(len(testFilesList)):
        testdir = vectortestpath +'/'+testFilesList[i]
        testdatalist = listdir(testdir)
        for j in range(len(testdatalist)):
            testdata = testdir + '/'+ testdatalist[j]
            testvector = {}
            vfrom.append(testFilesList[i])
            temp = open(testdata,'r').readlines()
            for k in range(len(temp)):
                temp[k] = temp[k].strip()
                b = temp[k].split('/')
                testvector[b[0]] = float(b[1])
            vsm.append(testvector) 
    return vsm, vfrom
def knn():
   testvsm ,testvfrom =  creatvector(vectortestpath)
   trainvsm ,trainvfrom =  creatvector(vectortrainpath) 
   testmo = [ ]  #存储测试向量的模长
   trainmo = [ ] #存储训练向量的模长
   k = 3        #knn的k的取值
   result = [ ]  #存储识别结果
   accurate = [ ]#存储是否识别正确
   for i in range(len(testvsm)): #计算模长
      tempsum = 0
      for key,value in testvsm[i].items():
          tempsum = tempsum +value*value
      testmo.append(math.sqrt( tempsum ))  
   for i in range(len(trainvsm)):
      tempsum = 0
      for key,value in trainvsm[i].items():
          tempsum = tempsum +value**2
      trainmo.append(math.sqrt( tempsum ))
   #print(trainmo)          
   for i in range(len(testvsm)):
       topk = []
       classfrom = []
       for j in range(len(trainvsm)):
           tempv = 0#用来计算两个向量的积
           for key,value in testvsm[i].items():
               if key in trainvsm[j].keys():
                   tempv = tempv + value*trainvsm[j][key]
           cosine = tempv/(trainmo[j]*testmo[i])  #计算cos值  
           if len(topk)<k :
               topk.append(cosine)
               classfrom.append(trainvfrom[j])
           elif cosine >= min(topk):  #去前k个最大的cosine值
               topk[topk.index(min(topk))] = cosine
               classfrom[topk.index(min(topk))] = trainvfrom[j]
       a = Counter(classfrom)
       '''if len(a) >= 3: #看k个备选类里出现最多的前三个类，有一个满足则命中
         res = a.most_common(3)
         if res[0][0] == testvfrom[i] or res[1][0] == testvfrom[i] or res[2][0] == testvfrom[i]:
           accurate.append(1)
         else:
           accurate.append(0)
       else:
         res = a.most_common(1)  
         if res[0][0] == testvfrom[i] :#or res[1][0] == testvfrom[i] :
           accurate.append(1)
         else:
           accurate.append(0)'''
       res = a.most_common(1)  #看k个备选类里出现最多的类，有一个满足则命中
       if res[0][0] == testvfrom[i] :#or res[1][0] == testvfrom[i] :
           accurate.append(1)
       else:
           accurate.append(0)    
       result.append(res[0])
      #print (topk)
      #print (classfrom)
   s = 0
   for i in range(len(accurate)):
       if accurate[i] == 1:
          s = s + 1
   f = s/ len(accurate)
   print(result)           
   print(f)          
knn()               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
       
>>>>>>> f4fcde3c184354f4f307c9553d2b1bdf89f093bc
