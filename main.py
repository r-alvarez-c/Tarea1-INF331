import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S', filename='Logs.log',
                    level=logging.DEBUG)

def encoding(text):
    return str(text.encode("UTF-8"))[2:-1]

def main():
    logging.info('Inicializando Programa')
    pila = list()
    while True:
        print('\n'*4+'-'*9+' Menu '+'-'*9)
        if len(pila) > 0:
            print('Cantidad de cadenas almacenadas: '+str(len(pila)))
        else:
            print('Pila Vacía\n')
        menu = input('Opciones:\n' +
                     '1. Agregar cadena de caracteres\n' +
                     '2. Ver pila de caracteres\n' +
                     '3. Comparar 2 ultimas cadenas\n' +
                     '4. Cerrar Programa\n' +
                     'Opcion: ')
        print('\n'*2)
        if menu == '4':
            logging.info('Finalizando Programa')
            break
        elif menu == '1':
            new_str = input('Ingrese cadena de caracteres: ').strip()
            if len(new_str) < 1:
                print('Cadena de caracteres no valida...' +
                      'Volviendo a menu principal')
                logging.error('Cadena de caracteres vacia ingresada')
            else:
                print('Cadena de caracteres ingresada! Indice: ' +
                      str(len(pila)))
                pila.append(new_str)
                logging.info(encoding('"'+new_str+'" ingresado a pila. Indice: ' +
                              str(len(pila))))

        elif menu == '2':
            if len(pila) < 1:
                print('PILA VACIA')
            else:
                for i in range(len(pila)):
                    print(i+1, ": "+pila[i])
            logging.info('Imprimiendo pila')
        elif menu == '3':
            if len(pila) < 2:
                print('Cantidad minima (2) de cadenas no disponibles en pila (' +
                      str(len(pila)) + ')... Volviendo a menu principal')
                logging.warning('Solicitud de comparacion no valida, dimension' +
                                ' actual de la pila: '+str(len(pila)))
            else:
                c1 = pila[len(pila)-1]
                pila.pop()
                c2 = pila[len(pila)-1]
                pila.pop()
                print('Analizando ultimas dos cadenas')
                print('Cadena 1: '+c1)
                print('Cadena 2: '+c2)
                logging.info('Analizando ultimas dos cadenas...')
                if c1 == c2:
                    print('Cadenas iguales')
                    logging.info(encoding('Cadena 1: "' + c1+'" , Cadena 2: "' +
                                  c2+'", iguales'))
                else:
                    print('Cadenas diferentes')
                    logging.info(encoding('Cadena 1: "' + c1+'" , Cadena 2: "' +
                                  c2+'", diferentes'))
        else:
            print('Opcion ingresada no valida, pruebe nuevamente')


if __name__ == '__main__':
    main()
