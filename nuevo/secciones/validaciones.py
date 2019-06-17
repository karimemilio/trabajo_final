import PySimpleGUI as sg
from wiktionaryparser import WiktionaryParser
from pattern.text.es import tag

def validarPattern(pal):
	tipo = (tag(palabra))[0][1]
	if tipo:
		tup = (True,tipo[1])
	else:
		tup = (False,tipo[1])
	return tup

def validarWiki(pal):
    wik = WiktionaryParser()
    wik.set_default_language('spanish')
    word = (parser.fetch(dat))[0]
    data = word['etymology']
    tipo = 'VB'
    if (len(data) > 1):
		tup = (True,tipo,data)
	else:
		tup = (False,tipo,data)   ##Se recupera el tipo con la key partOfSpeech
	return tup
	
def reporte(titu):     

	sg.PopupError(titu)


def validar(dat):    #Retorna tupla (bool,tipo,definicion)
    vw = validarWiki(dat) #IMPLEMENTAR recuperar tipo
    vp = validarPattern(dat) 
    if vw[0]:
        if vp[0]:
            if vw[1] != vw[1]:
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
            return (vp[0],vp[1],definicion)
		else:
			return (False,0,0)    ##No se encontro ni en wikidictionary ni en pattern
