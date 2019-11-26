

def returnEnglish():
    f= open("EnglishHist.txt","r")
    contents = f.read()
    f.close()
    return contents

def returnGerman():
    f= open("GermanHist.txt","r")
    contents = f.read()
    f.close()
    return contents

def returnFrench():
    f= open("FrenchHist.txt","r")
    contents = f.read()
    f.close()
    return contents

def returnJapanse():
    f= open("JapaneseHist.txt","r")
    contents = f.read()
    f.close()
    return contents
