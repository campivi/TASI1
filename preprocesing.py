import csv
from googletrans import Translator
import re

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
                print (traducido.text)
        #print(row[0])
        #print(row[1])
