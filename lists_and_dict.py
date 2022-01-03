def main():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'nombre': 'Julio', 'apellido': 'Motta'}

    super_list = [
        {'nombre': 'Julio', 'apellido': 'Motta'},
        {'nombre': 'Jose', 'apellido': 'Motta'},
        {'nombre': 'Juan', 'apellido': 'Motta'},
        {'nombre': 'Jhom', 'apellido': 'Motta'},
    ]

    super_dict = {
        "nums_natural" : [1, 2, 3, 4, 5],
        "nums_enteros": [-1, -2, 0, 1 ,2],
        "nums_float": [1.1, 1.2, 1.3],
    }

    for key, valor in super_dict.items():
        print(key, "-", valor)


if __name__ == '__main__':
    main()