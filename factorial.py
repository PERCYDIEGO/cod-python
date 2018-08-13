def factorial(number):
    for i in range(1,number):
            number=number*i
    return(number)


if __name__ == '__main__':
    number=int(input('Ingrese el número: '))
    result=factorial(number)
    print("El número tiene como factorial a: {}".format(result))
