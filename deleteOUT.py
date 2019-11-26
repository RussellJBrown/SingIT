

import os


locationEnglish = "/media/russell/775C-44EC/English"
locationGerman = "/media/russell/775C-44EC/German"
locationJapanese = "/media/russell/775C-44EC/Japanese"
locationFrench = "/home/russell/SingIT/testFrench"

#dirEnglish =  os.listdir(locationEnglish)
#dirGerman =   os.listdir(locationGerman)
#dirJapanese = os.listdir(locationJapanese)
dirFrench   = os.listdir(locationFrench)


for i in dirFrench:
    name, ext = os.path.splitext(i)
    print(ext)
    if(ext=='.wav'):
        name = os.path.splitext(i)[0]
        name2 = name[-3:]
        if (name2=="Out"):
                os.remove(locationFrench+"/"+i)
                print("Delete: ")
                print(i)
