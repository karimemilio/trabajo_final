import PySimpleGUI as sg



def validar(dat):    #Retorna tupla (bool,tipo,definicion)
    vw = validarWiki(dat) #IMPLEMENTAR
    vp = validarPattern(dat) #IMPLEMENTAR
    if vw[0]:
        if vp[0]:
            if vw[1] != vw[1]:
                reporte #IMPLEMENTAR reporte que son distintos tipos, tomamos wiki
        else:
            reporte #IMPLEMENTAR reporte de que pattern no valido, tomamos wiki
        return vw
    else:
        if vp[0]:
            reporte #IMPLEMENTAR reporte que wiki no valido pero pattern si
            defi = ingresa defi #IMPLEMENTAR avisar q se ingresa
            return (vp[0],vp[1],defi)
    
    parser = WiktionaryParser()
    parser.set_default_language('spanish')
    word = (parser.fetch(dat))[0]
    data = word['etymology']
    if (len(data) > 1):
        return True
    else:
        return False