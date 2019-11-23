

import os


locationEnglish = "/home/russell/SingIT/English"
locationGerman = "/home/russell/SingIT/German"
locationJapanese = "/home/russell/SingIT/Japanese"
locationFrench = "/home/russell/SingIT/French"

dirEnglish =  os.listdir(locationEnglish)
dirGerman =   os.listdir(locationGerman)
dirJapanese = os.listdir(locationJapanese)
dirFrench   = os.listdir(locationFrench)


for i in dirJapanese:
    name, ext = os.path.splitext(i)
    print(ext)
    if(ext=='.wav'):
        name = os.path.splitext(i)[0]
        name2 = name[-3:]
        if (name2=="Out"):
                os.remove(locationJapanese+"/"+i)
                print("Delete: ")
                print(i)
