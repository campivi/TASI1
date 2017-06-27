"""Archivo con el preprocesamiento de archivos en inglés y español para el proyecto"""
import csv
import re
import nltk
from googletrans import Translator

lista_palabras = [
    "processor", "ram", "storage", "memory", "battery", "screen", "camera", "display"
    ]

def tiene_palabra_importante(oracion):
    tokens = nltk.word_tokenize(oracion.lower())
    for token in tokens:
        if token in lista_palabras:
            return True
    return False

def texto_traducir(archivo):
    """
    Función que traduce el texto a inglés
    """
    translator = Translator()
    contador = 0
    salida  = open('Oraciones_Sony.csv', "w")
    writer = csv.writer(salida, delimiter =',',quotechar ='"',quoting=csv.QUOTE_MINIMAL)
    with open(archivo, 'r') as abierto:
        reader = csv.reader(abierto)
        for row in reader:
            oraciones = row[0].split('.')
            contador += 1
            print(contador)
            lenguaje = translator.detect(oraciones[0])
            if lenguaje.lang == "es":
                for oracion in oraciones:
                    if len(oracion) > 1:
                        oracion = re.sub(r'[\W]', ' ', oracion)
                        oracion = oracion.replace('\n', ' ')
                        oracion = oracion.replace('\t', ' ')
                        traducido = translator.translate(oracion)
                        if tiene_palabra_importante(traducido.text):
                            writer.writerow([traducido.text])
            else:
                for oracion in oraciones:
                    if len(oracion) > 1:
                        oracion = re.sub(r'[\W]', ' ', oracion)
                        oracion = oracion.replace('\n', ' ')
                        oracion = oracion.replace('\t', ' ')
                        if tiene_palabra_importante(oracion):
                            writer.writerow([oracion])

texto_traducir('Sony.csv')
