from secciones import modulos

def main():
    dicc = modulos.cargarInfo()
    if dicc:
        modulos.jugar(dicc)

if __name__=='__main__':	#Esta condicion se cumple si el módulo no es importado
    main()