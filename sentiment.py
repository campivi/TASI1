from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator
import re
import csv

'''analyzer = SentimentIntensityAnalyzer()
translator = Translator()
contador = 0
with open('libre.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        oraciones = row[0].split('.')
        contador += 1
        print(contador,oraciones)
        for oracion in oraciones:
            if (len(oracion) > 1):
                oracion = re.sub('[\W]', ' ', oracion)
                oracion = oracion.replace('\n', ' ')
                oracion = oracion.replace('\t', ' ')
                traducido = translator.translate(oracion)
                vs = analyzer.polarity_scores(traducido.text)
                print("{:-<65} {}".format(traducido.text, str(vs)))
                #print (traducido.text)
        #print(row[0])
        #print(row[1])'''

from textblob import TextBlob

analyzer = SentimentIntensityAnalyzer()
translator = Translator()
contador = 0
with open('libre.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        oraciones = row[0].split('.')
        contador += 1
        print(contador,oraciones)
        for oracion in oraciones:
            if (len(oracion) > 1):
                oracion = re.sub('[\W]', ' ', oracion)
                oracion = oracion.replace('\n', ' ')
                oracion = oracion.replace('\t', ' ')
                traducido = translator.translate(oracion)
                blob = TextBlob(traducido.text)
                for sentence in blob.sentences:
                    print(sentence + " => " + str(sentence.sentiment.polarity))
                
