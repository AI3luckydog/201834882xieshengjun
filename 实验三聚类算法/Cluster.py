# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 15:28:32 2018

@author: x
"""
from sklearn.cluster import KMeans
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import SpectralClustering

from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import sklearn.metrics
from sklearn.cluster import MeanShift, estimate_bandwidth 
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.cluster import Birch
fr =  open('E:/Tweets.txt','r')
sf = fr.read()
fr.close()
datalist = sf.split('}\n{')
tem1 = datalist[0].split('{')
datalist[0] = tem1[1]
tem2 = datalist[len(datalist)-1].split('}')
datalist[len(datalist)-1] = tem2[0]
text = []
cluster = []
for i in range(len(datalist)):
    t1= datalist[i].split('"text": "')
    t2 = t1[1].split('", "cluster": ')
    text.append(t2[0])
    cluster.append(int(t2[1]))#读文件
#print(text)
tfidfdict = { }    
vectorizer=CountVectorizer()
transformer=TfidfTransformer()
tfidf=transformer.fit_transform(vectorizer.fit_transform(text))
word=vectorizer.get_feature_names()
weight=tfidf.toarray()#生成tfidf矩阵
#print(weight)
def Kmeans(weight):
  kMresult =  KMeans(n_clusters=110,n_init=10, max_iter= 300, init='k-means++').fit_predict(weight)
  print(kMresult)
  rkmean = sklearn.metrics.normalized_mutual_info_score(cluster,kMresult , average_method='warn')
  print (rkmean)
def Affinity(weight):
  Affresult=AffinityPropagation(damping=0.5, max_iter=200, convergence_iter=15, copy=True, preference=None, affinity='euclidean', verbose=False).fit_predict(weight)
  rAff = sklearn.metrics.normalized_mutual_info_score(cluster,Affresult , average_method='warn')
  print (rAff)
def mean(weight):
  bandwidth = estimate_bandwidth(weight, quantile = 0.2, n_samples = 500)
  mean = MeanShift(bandwidth = bandwidth, bin_seeding = True).fit_predict(weight)
  rmean = sklearn.metrics.normalized_mutual_info_score(cluster,mean , average_method='warn')
  print(rmean)
def spect(weight):
  spectresult = SpectralClustering(n_clusters=110).fit_predict(weight)

  rspectresult = sklearn.metrics.normalized_mutual_info_score(cluster,spectresult , average_method='warn')
  print(rspectresult)
def agglomerative_clustering(tfidf_matrix):
    ac_cluster = AgglomerativeClustering(linkage='average', n_clusters=110)
    
    result = ac_cluster.fit_predict(tfidf_matrix)
    ragg = sklearn.metrics.normalized_mutual_info_score(cluster,result , average_method='warn')
    print (ragg)

def dbscan(tfidf_matrix):
    db_cluster = DBSCAN(eps=1, min_samples=1)
    
    result = db_cluster.fit_predict(tfidf_matrix)
    rdbscan = sklearn.metrics.normalized_mutual_info_score(cluster,result , average_method='warn')
    print(rdbscan)


def birch(tfidf_matrix):
    b_cluster = Birch(n_clusters=90, threshold=0.7)
    
    result = b_cluster.fit_predict(tfidf_matrix)
    rbirch = sklearn.metrics.normalized_mutual_info_score(cluster,result , average_method='warn')
    print(rbirch)
Kmeans(weight)
Affinity(weight)
mean(weight)
spect(weight)
agglomerative_clustering(weight)
dbscan(weight)
birch(weight)