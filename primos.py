def primo(number):
    valor=0
    for i in range(2,number):
        if number % i==0:
            valor=valor+1
    if valor!=0:
        print('El número no es primo')
    else:
        print('El número es primo')



if __name__ == '__main__':
    mensaje='Programa del número primo'
    print(mensaje)
    print(len(mensaje)*'_')
    print('')
    number=int(input('Ingrese el número: '))
    print('')
    primo(number)
