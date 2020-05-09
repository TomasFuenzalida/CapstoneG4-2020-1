
def transformar_lista(archivo):
    with open(archivo, 'r', encoding="utf-8") as f:
        lineas = [linea.split(",") for linea in f]
    for linea in lineas:
        linea[len(linea)-1] = linea[len(linea)-1].strip("\n")
    return lineas

def asignar_valores(lista):
    barco = lista[0]
    Mvto = lista[1]
    ID = lista[2].split('_')
    numero = ID[1]
    tipo = ID[2]
    print(f'el barco {barco}, su Mvto {Mvto}, su numero {numero}, tipo {tipo}')

lista_de_lista = transformar_lista('lista_container_enviado.csv')

for lista in lista_de_lista:
    asignar_valores(lista)