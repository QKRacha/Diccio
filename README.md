# Diccio
Script para crear passwords a partir de una página web

Este script ha sido creado para el proyecto de final de master, es una primera fase muy simple 
pero que cumple las necesidades basicas para este proyecto.

Algunas partes estan copiadas de manuales y/o otras páginas webs.

La idea fundamental del script es extraer palabras de una página web, ordenarlas de mas a menos usadas y despues
aplicarle unos "filtros" para generar un diccionario que nos pueda valer para otras herrameintas de brute force

Opciones:

- solo passwords de palabras extraidas
- passwords de palabras extraidas con números delante
- passwords de palabras extraidas con números detras
- passwords de palabras extraidas con números delanta y detras
- passwords de palabras extraidas con números en medio de la palabra (justo en el medio, el script parte la palabra por la mitad)
- passwords de palabras extraidas con todos las opciones juntas

Parametros configurables:

      positional arguments:
        url                   Página a analizar, formato http://www.tudominio.com

      optional arguments:
        -h, --help            show this help message and exit
        -sw {es,cat,en,all}, --stopwords {es,cat,en,all}
                              Palabras tipicas del idioma que no se tendran en
                              cuenta
        -l LONG, --long LONG  longitud minima de las palabras a extraer
        -f FILE, --file FILE  Nombre del archivo que nos genera
        -t {simple,numin,numout,all}, --tipo {simple,numin,numout,all}
                              Tipo de archivo de salida simple (sin num), numin
                              (numeros dentro), numout (numeros fuera), all todos
        -ni NUMINT, --numint NUMINT
                              Número máximo dentro del password
        -no NUMOUT, --numout NUMOUT
                              Cantidad de numeros antes y despues de la palabra
                        
El archivo stopwords.py tiene un listado de las palabras mas comunes de los idiomas catalan, español e ingles.


