import sklearn


def compareDatasetLive():



    return output




#This Method will be used to train the dataset
#The data from a known dataset will be read in
#if correct the dataset will be updated.
#if incorrect, the correct dataset will be updated
def compareDatasetTrain(data,ActualLanguage):

    determinedLanguage = "s"

    if(determinedLanguage==ActualLanguage):
        #UpdateLanguageDataset
        print("fd")
    elif:
        updateString = ActualLanguage+"/NormalScatter"+ActualLanguage+".txt"
        updateString2 = ActualLanguage+"/VocalExtractedScatter"+ActualLanguage+".txt"
        f = open(updateString,'a')
        f.write(to_str(data[0]))
        f.write(" ")
        f.write(to_str(data[1]))
        f.write("\n")
        f.close()

        f = open(updateString2,'a')
        f.write(to_str(data[2]))
        f.write(" ")
        f.write(to_str(data[3]))
        f.write("\n")
        f.close()
