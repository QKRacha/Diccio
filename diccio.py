#!/usr/bin/python/env
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import requests,obo

"""posibles argumentos que se le puedden pasar:
-h -> mostrar esta informacion
u -> url a analizar
-sw "es/en/cat/all" -> escogemos su queremos sacar algun tipo de stopwords o todos
-l "1,2,3,4,..."-> decidimos que longitud minima queremos tener en cuenta (default 2)
-f -> archivo de salida passwords sin tratar (default pass.txt)
-fi -> archivo de salida passwords con numeros en centro
-fs -> archivo de salida passwords delante / detras
-ni -> numero maximo interior
-ns -> numero màximo delante / detras"""

parser = ArgumentParser(description='%(prog)s Sirve para crear un diccionario a partir de una web')
parser.add_argument('url', help='Página a analizar, formato http://www.tudominio.com')#argumento posicional obligatorio
parser.add_argument('-sw','--stopwords', choices=['es', 'cat','en', 'all'],help='Palabras tipicas del idioma que no se tendran en cuenta')#argumento opcional con 4 valores posibles
parser.add_argument('-l','--long',help='longitud minima de las palabras a extraer',default=2,type=int)
parser.add_argument('-f','--file',help='Nombre del archivo que nos genera',required=True)
parser.add_argument('-t','--tipo',choices=['simple','numin','numout','all'],help='Tipo de archivo de salida simple (sin num), numin (numeros dentro), numout (numeros fuera), all todos',required=True)
parser.add_argument('-ni','--numint',help='Número máximo dentro del password',type=int,required=True)
parser.add_argument('-no','--numout',help='Cantidad de numeros antes y despues de la palabra',type=int,required=True)
args = parser.parse_args()

statusCode=0
try:
    r = requests.get(args.url) #cargamos la respuesta de GET de la pàgina
    statusCode = r.status_code
except:
    print("Formato de la web erroneo, debe ser del estilo http://www.google.com")

if statusCode == 200:
    text = obo.stripTags(r.text) #quitamos las etiquetas y pasamos a minuscula
    fullwordlist = obo.stripNonAlphaNum(text)#quitamos los que no son alfanumericos
    if args.stopwords:
        fullwordlist = obo.removeStopwords(fullwordlist,args.stopwords)#eliminamos las palabras de uso comun segun el idioma
    if args.long:
        fullwordlist = obo.excludeTwo(fullwordlist,args.long)#eliminamos las palabras con menos de 2 caracteres
    dictionary = obo.wordListToFreqDict(fullwordlist)#nos devuelve un diccionario palabra - frequencia
    sorteddict = obo.sortFreqDict(dictionary)#ordena las palabras por su frequencia (nos han devuelto una lista de listas)
    if args.tipo == 'simple':
        obo.makePassfile(sorteddict,args.file) #crea el primer archivo de pass.txt
        print('Archivo simple creado correctamente:'+args.file)
    elif args.tipo == 'numin':
        obo.makePassfile(sorteddict,args.file) #crea el primer archivo de pass.txt
        obo.numInside(args.file,args.numint) #crea el archivo passInt.txt
        print('Archivo con numeros en el interior creado correctamente:',args.file)
    elif args.tipo == 'numout':
        obo.makePassfile(sorteddict,args.file) #crea el primer archivo de pass.txt
        obo.passNumeracion(args.file,args.numout) #crea el archivo passNum.txt
        print('Archivo con numeros en el exterior creado correctamente:',args.file)
    elif args.tipo == 'all':
        obo.makePassfile(sorteddict,args.file) #crea el primer archivo de pass.txt
        obo.passNumeracion(args.file,args.numout) #crea el archivo passNum.txt
        obo.numInside(args.file,args.numint) #crea el archivo passInt.txt
        print('Archivo completo creado correctamente:',args.file)
else:
    print('Error al abrir la web, status code:',statusCode)
