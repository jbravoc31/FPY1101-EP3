import os

libros = []

def registrar():
    #Título, Autor, Año de Publicación, SKU
    titulo = input('*****************************************************\nIngrese el nombre del libro:\n')
    autor = input('*****************************************************\nIngrese el nombre del auto del libro:\n')
    anopubli = int(input('*****************************************************\nIngrese el año de publicacion del libro:\n'))
    sku = input('*****************************************************\nIngrese el SKU\n***NOTA***\nlas 6 primeras letras del título del libro, las 3 primeras letras del autor y año de publicación.\nejemplo: ABCDEF-ABC-2024\n********** S K U **********\n')
    libro = {
        'titulo' : titulo,
        'autor' : autor,
        'anopubli' : anopubli,
        'sku' : sku
    }
    
def prestar():
    usuario = input('Ingrese nombre del usuario al que se le prestara el libro:\n')
    prestamo = input('Ingrese el SKU del libro que se desea prestar:\n')
    if prestamo == libros.sku:
        print(f'Libro prestado a {usuario} el libro prestado tiene el sku {prestamo}')
    else:
        print('Libro no encontrado por favor reintente')


def listar():
    print('TITULO\t\t\t\tAUTOR\t\t\t\tAÑO DE PUBLICACIÓN\t\t\t\tSKU')
    for libro in libros:
        print(f'{libros['titulo']}\t\t\t\t{libros['autor']}\t\t\t\t{libros['anopubli']}\t\t\t\t{libros['sku']}')
        
def imprimir():
    #reportes de prestamos
    with open('Lista de Libros.txt','w') as archivo:
        archivo.write(f'{libros['titulo']}\t\t\t\t{libros['autor']}\t\t\t\t{libros['anopubli']}\t\t\t\t{libros['sku']}')



def menu():
    while True:
        try:
            print('Menu de opciones libro')
            print('1. Registrar libro')
            print('2. Prestar libro')
            print('3. Listar todos los libros')
            print('4. Imprimir reporte de préstamos')
            print('5. Salir del Programa')
            opcion = int(input('Ingrese la opcion que desea:\n'))

            if opcion == 1:
                registrar()
            elif opcion == 2:
                prestar()
            elif opcion == 3:
                listar()
            elif opcion == 4:
                imprimir()
            elif opcion == 5:
                print('Programa Finalizado...\nDesarrollado por Javier Bravo\nRUN 20.238.575-3')
                os.system('pause')
                break
            else:
                print('Ud ha ingresado una opcion invalida porfavor reintente')

        except ValueError:
            print('opcion no valida')
            
