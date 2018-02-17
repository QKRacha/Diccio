#!/usr/bin/python
# -*- coding: utf-8 -*-
import stopwords
import os

"""Funcion que me elimine las palabras de 2 o menos caracteres"""
def excludeTwo(wordlist,largo):#le paso una lista de palabras
    wordend=[]
    for w in wordlist:#bucle para recorrer la lista
        if len(w)>=largo:
            wordend.append(w)#añadimos a la nueva lista si es mayor de 2
    return wordend

"""Esta funcion se le pasara el contenido de una web y devolvera el texto de
la misma sin tags"""
def stripTags(pageContents):# le pasamos el contenido de una web
    inside = 0
    text = ''
    for char in pageContents:#comprobamos si estamos dentro de una etiqueta HTML
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char
    return text

"""Dado un texto quitar todos los caracteres que no son alfanumericos"""
def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

"""Dada una lista de palabras, devuelve un diccionario de
palabras / frequencia"""
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

"""ordena un diccionario de palabras-frequencia
en orden ascendiente por frequencia"""
def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

"""Dada una lista de palabras eliminar las que son tipicas del idioma
Las palabras a quitar estan en el archivo stopwords.py, estan para
catalan, español y ingles"""
def removeStopwords(wordlist,idioma):
    if idioma == 'es':
        stop = stopwords.palabrastop
    elif idioma == 'cat':
        stop = stopwords.paraulestop
    elif idioma == 'en':
        stop = stopwords.stopwords
    elif idioma == 'all':
        stop = stopwords.stopwords
        stop += stopwords.palabrastop
        stop += stopwords.paraulestop
    return [w for w in wordlist if w not in stop]

"""Funcion a la que le pasamos una lista de listas y nos crea un archivo
de  texto con las palabras que hay en cada posicion"""
def makePassfile(wordlist,fichero):
    file = open(fichero,"w")
    i=0
    for s in wordlist:
        file.write(wordlist[i][1])
        file.write("\n")
        i+=1
    file.close()


"""Funcion que lee un fichero y por cada palabra crea una combinacion
de la misma con numeros por delante y por detras (todas las combinacione
posibles)"""
def passNumeracion(archivo,itera):
    origen = open(archivo,"r") #fichero origne
    destino = open("passNum.txt","w") #fichero destino
    for linea in origen:
        i = 0
        f = 0
        x = 0
        z = 0
        destino.write(linea)
        for i in range(itera):#bucle que crea todas las combinaciones por delante
            destino.write(str(i))
            destino.write(linea)
        for f in range(itera):#bucle que crea todas las combinaciones por detras
            destino.write(linea.strip('\n'))
            destino.write(str(f))
            destino.write('\n')
        for x in range(itera):#bucles anidados que crean todas las combinaciones por delante y por detras
            line = str(x)
            line += linea.strip('\n')
            for z in range(itera):
                destino.write(line)
                destino.write(str(z))
                destino.write('\n')
    origen.close()
    destino.close()
    os.rename('./passNum.txt','./'+archivo)


"""Funcion que le pasaremos un fichero con palabras y que las partira
y añadirà numeros en la mitad generando un nuevo fichero de passwords"""
def numInside(archivo,itera):
    origen = open(archivo,"r") #fichero origen
    destino = open("passInt.txt","w") #fichero destino
    for linea in origen:
        destino.write(linea) #escribimosel primer password sin modificar
        line = linea.strip('\n')#quitamos salto de linea
        largo = len(line)#calculamos la longitud del string
        mitad = 0
        if largo % 2 == 0:#si es un numero par guardamos la mitad
            mitad = largo / 2
        else:#si es impar guardamos la mitad+1
            mitad = int(largo/2)+1
        m1 = int(mitad)
        l1 = line[:m1]
        l2 = line[m1:]
        for i in range(itera):
            destino.write(l1)#escribimos primera parte del password
            destino.write(str(i))#escribimos el numeral
            destino.write(l2)#escribimos la segunda parte del password
            destino.write('\n')#hacemos salto de linea
    origen.close()
    destino.close()
    os.rename('./passInt.txt','./'+archivo)
