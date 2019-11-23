from sklearn.cluster import KMeans
import librosa
import numpy as np
import os

def to_str(var):
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]

def kClustering(song,Language):
    print(song)
    print("")
    fileName = "kClustering"+Language+".txt"
    X,sr = librosa.load(song)
    Kmean = KMeans(n_clusters=20)
    X = np.reshape(X, (-1, 2))
    Kmean.fit(X)
    kCluster=Kmean.cluster_centers_
    rows = kCluster.shape[0]
    cols = kCluster.shape[1]
    f = open(fileName,'a')
    for x in range(0,rows):
        f.write("\n")
        for y in range(0,cols):
            f.write(to_str(kCluster[x,y]))
            f.write(" ")
    f.close()


locationEnglish = "/home/russell/SingIT/English"
locationGerman = "/home/russell/SingIT/German"
locationJapanese = "/home/russell/SingIT/Japanese"
locationFrench = "/home/russell/SingIT/French"

dirEnglish =  os.listdir(locationEnglish)
dirGerman =   os.listdir(locationGerman)
dirJapanese = os.listdir(locationJapanese)
dirFrench = os.listdir(locationFrench)

#for i in dirEnglish:
#    name, ext = os.path.splitext(i)
#    out = name[-3:]
#    if(ext=='.wav' and out == "Out"):
#        kClustering(locationEnglish+"/"+i,"English")

#for j in dirGerman:
#     name, ext = os.path.splitext(j)
#     out = name[-3:]
#     if(ext=='.wav' and out == "Out"):
#         kClustering(locationGerman+"/"+j,"German")

for k in dirJapanese:
    name, ext = os.path.splitext(k)
    out = name[-3:]
    if(ext=='.wav' and out == "Out"):
        kClustering(locationJapanese+"/"+k,"Japanese")

#for h in dirFrench:
#     name, ext = os.path.splitext(h)
#     out = name[-3:]
#     if(ext=='.wav' and out == "Out"):
#         kClustering(locationFrench+"/"+h,"French")
