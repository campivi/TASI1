"""Archivo con el preprocesamiento de archivos en inglés y español para el proyecto"""
import csv
import re
from googletrans import Translator


def texto_traducir(archivo):
    """
    Función que traduce el texto a inglés
    """
    translator = Translator()
    contador = 0
    with open(archivo, 'r') as abierto:
        reader = csv.reader(abierto)
        for row in reader:
            oraciones = row[0].split('.')
            contador += 1
            print(contador, oraciones)
            for oracion in oraciones:
                if len(oracion) > 1:
                    oracion = re.sub(r'[\W]', ' ', oracion)
                    oracion = oracion.replace('\n', ' ')
                    oracion = oracion.replace('\t', ' ')
                    traducido = translator.translate(oracion)
                    print(traducido.text)

texto_traducir('Sony.csv')
