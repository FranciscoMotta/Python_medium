DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
    
    # FUNCIONES DE FILTRO Y MAPEO

    func_selec("language", "python") # Filtramos nombres de los que usen Py
    func_selec("organization", "Platzi") # Filtramos nombres de los que trabajen con PLATZI

    # USAMOS LOS LAMBDAS

    adultos = [worker['name'] for worker in DATA if worker["age"] >= 18]
    for worker in adultos:
        print(worker + " es mayor de edad")


# ESTA FUNCION DEVUELVE EL NOMBRE DE LAS PERSONAS QUE CUMPLAN
# CON LA CONDICIÓN DE UNA DETERMININADA CARACTERÍSTICA

def func_selec (caracteristica, condicion):
     # PYTHON DEVS - FILTER
    python_devs = list(filter(lambda worker: worker[caracteristica] == condicion, DATA))
    # aplicamos el map
    python_devs = list(map(lambda worker: worker['name'], python_devs))
    for worker in python_devs:
        print(worker + " -> " + condicion)
    print('________________________________________')   
    
if __name__ == "__main__":
    main()