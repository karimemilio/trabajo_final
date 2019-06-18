import PySimpleGUI as sg
from pattern.web import Wiktionary as wik
from wiktionaryparser import WiktionaryParser
from pattern.text.es import tag

def validarPattern(pal): #Devuelve J,N,B
	tipo = (tag(pal))[0][1]
	if tipo:
		return (True,tipo[1])
	else:
		return (False)

def validarWiki(pal): #Devuelve adjective,noun,verb
    wik = WiktionaryParser()
    wik.set_default_language('spanish')
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
        return (False)   ##Se recupera el tipo con la key partOfSpeech
    
def reporte(titu):     

	sg.PopupError(titu)


def validar(dat):
    vw = validarWiki(dat) #Retorna tupla (bool,tipo,definicion)
    vp = validarPattern(dat) #Devuelve tupla (boolean,tipo)
    if vw[0]:
        if vp[0]:
            if vw[1] != vp[1]:
                titu = "Diferentes tipo de palabra"
                reporte(titu) #reporte que son distintos tipos, tomamos wiki
        else:
            titu = "Pattern invalido"
            reporte(titu) #reporte de que pattern no valido, tomamos wiki
        return vw
    else:
        if vp[0]:
            titu = "Wikidictionary invalido"
            reporte(titu)
            defi = 'Ingrese una definicion para la palabra:',dat    
            text = sg.PopupGetText(defi, 'Definicion')  
            return (vp[0],vp[1],defi)
        else:
            titu = "No se encontro la palabra. No se ingresa"
            reporte(titu)
            return (False,1)    #No se encontro ni en wikidictionary ni en pattern
