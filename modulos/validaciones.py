"""Validaciones se encarga de validar cada una de las palabras ingresadas , primero con wikitionary y despues con Pattern, y partir de sus resultados
    hacer diferentes comparaciones para generar el reporte deseado"""
import PySimpleGUI as sg
from pattern.web import Wiktionary as wiki
from pattern.web import SEARCH
from wiktionaryparser import WiktionaryParser
from pattern.text.es import tag

def agregar(texto,reporte):
    reporte.append(texto)
    print('--------REPORTE----------')
    for each in reporte:
        print(each)
        print()

def validarPattern(pal): #Devuelve J,N,B
    tipo = (tag(pal))[0][1]
    print("Palabra ingresada: ", tag(pal))
    if tipo:
        return (True,tipo[1])
    else:
        return (False)

def validarWiki(pal): #Devuelve adjective,noun,verb
    wik = WiktionaryParser()
    wik.set_default_language('spanish')
    try:
        word = (wik.fetch(pal))[0]
        defi = word['etymology']
        tipo = word['definitions'][0]['partOfSpeech']
        if (len(defi) > 1):
            if tipo == 'adjective':
                tipo = 'J'
            elif tipo == 'noun':
                tipo = 'N'
            else:
                tipo = 'B'
            return (True,tipo,defi[:-2])
        else:
            return (False,False,False)   ##Se recupera el tipo con la key partOfSpeech
    except:
        return(False,False,False)

def validar(dat,reporte,boton):
    vw = validarWiki(dat) #Retorna tupla (bool,tipo,definicion)
    vp = validarPattern(dat) #Devuelve tupla (boolean,tipo)
    if vw[0]:
        if boton == 'Agregar palabra':
            if vp[0]:
                if vw[1] != vp[1]:
                    titu = dat + ": La clasificación de Wiktionary no coincide con la de Pattern. Tomamos como válida la clasificación de Wiktionary"
                    agregar(titu,reporte) #reporte que son distintos tipos, tomamos wiki
            else:
                titu = dat + ": La clasificación de Pattern es inváida. Tomamos como válida la clasificación de Wiktionary"
                agregar(titu,reporte) #reporte de que pattern no valido, tomamos wiki
        return vw
    else:
        if vp[0]:
            text = None
            if boton == 'Agregar palabra':
                titu = dat + ": La clasificación de Wiktionary es inváida. Tomamos como válida la clasificación de Pattern"
                agregar (titu,reporte)
                defi = 'Ingrese una definicion para la palabra: ' + str(dat)    
                text = sg.PopupGetText(defi, 'Definicion')
            return (vp[0],vp[1],text)
        else:
            if boton == 'Agregar palabra':
                titu = dat + ": No se encontró la palabra. No se ingresa"
                agregar(titu,reporte)
            return (False,1,None)    #No se encontro ni en wikidictionary ni en pattern