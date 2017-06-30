from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('ro'))

with open(r"C:\Users\Mihai\Desktop\tests\data_test_20.06.2017.txt",'r') as inFile, open(r"C:\Users\Mihai\Desktop\tests\data_test_20.06.2017_cleaned.txt",'w') as outFile:
    words = word_tokenize(inFile)
    for w in words:
        if w not in stop_words:
            outFile.write(w)
outFile.close()