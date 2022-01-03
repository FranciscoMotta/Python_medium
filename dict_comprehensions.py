def main():
    #    my_dict = {} # Creamos un diccionario

    # for i in range (1,101):
    #     my_dict[i] = i**3
    # print(my_dict)
    my_dict = {i: i**3 for i in range(1,101) if i%3!=0}
    print(my_dict)

    # Para cada elemento en un iterable voy a colocar una llave
    # y un valor sí se cumple una condicion

    my_root = {i : i**0.5 for i in range(1,101)}
    print(my_root)

if __name__ == '__main__':
    main()